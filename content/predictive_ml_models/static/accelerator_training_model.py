# Databricks notebook source
# MAGIC %md 
# MAGIC # Propensity to Convert ML Model Training
# MAGIC 
# MAGIC In this notebook we will be using sample behavioural data collected by Snowplow's Javascript tracker from Snowplow's [snowplow.io](https://snowplow.io/) website.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configuration
# MAGIC 
# MAGIC Please use a cluster with **11.2 ML CPU** Runtime.

# COMMAND ----------

# DBTITLE 1,Import libraries
import pandas as pd
import mlflow
import lightgbm as lgb
from imblearn.over_sampling import SMOTENC
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, fbeta_score, average_precision_score
from sklearn.pipeline import Pipeline
from hyperopt import fmin, tpe, rand, hp, Trials, STATUS_OK, SparkTrials, space_eval
from hyperopt.pyll.base import scope
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split

# COMMAND ----------

# DBTITLE 1,Load user features
df = spark.table("snowplow_samples.samples.first_touch_user_features").toPandas()

ref_cols = ["refr_urlhost", "refr_medium"]
mkt_cols = ["mkt_medium", "mkt_source", "mkt_term"]
geo_cols = ["geo_country", "geo_region", "br_lang"]
dev_cols = ["device_family", "os_family"]
url_cols = ["first_page_title"]
engagement_cols = ["engaged_time_in_s", "absolute_time_in_s", "vertical_percentage_scrolled"]

discrete_col = ref_cols + mkt_cols + geo_cols + dev_cols + url_cols
continues_col = engagement_cols
all_features = discrete_col + continues_col

# Input missing data
for col in discrete_col:
    df[col].fillna("N/A", inplace=True)
for col in continues_col:
    df[col].fillna(df[col].mean(), inplace=True)
    
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model Selection
# MAGIC 
# MAGIC Boosting trees perform better than neural networks on categorical data sets, such as this one. Another great property is their ability to work with noisy data, LightGBM could do all preprocessing internally, but this isn’t used in this notebook. The most popular ones are XGBoost, LightGBM and CatBoost, each with different strengths. For this example we will use LightGBM.
# MAGIC 
# MAGIC **LightGBM** is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with the following advantages:
# MAGIC 
# MAGIC * Faster training speed and higher efficiency
# MAGIC * Lower memory usage
# MAGIC * Better accuracy
# MAGIC * Support of parallel, distributed, and GPU learning
# MAGIC * Capable of handling large-scale data
# MAGIC 
# MAGIC 
# MAGIC **Resources:** 
# MAGIC - [Full LightGBM Documentation](https://lightgbm.readthedocs.io/en/v3.3.2/)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Train Model

# COMMAND ----------

print(f"Users: {len(df)}")
print(df["converted_user"].value_counts(normalize=True))

# COMMAND ----------

# MAGIC %md
# MAGIC The provided training data is relativley small in size and combined with a low conversion rate, we consider it to be imbalanced. Therefore we will balance the dataset with SMOTE, which will oversample the data by introducing new synthetic converted user samples.

# COMMAND ----------

# DBTITLE 1,Reduce number of categorical features
# Reduce number of categorical features so `SMOTENC` doesn't run out of memory. 
class TakeTopK(BaseEstimator, TransformerMixin):
    def __init__(self, k=20):
        self.largest_cat = {}
        self.k = k
        
    def fit(self, X, y=None):
        for col in discrete_col:
            self.largest_cat[col] = df[col].value_counts().nlargest(self.k).index
        return self
    
    def transform(self, X, y=None):
        Xt = pd.DataFrame()
        for col in discrete_col:
            Xt[col] = pd.Series(np.where(X[col].isin(self.largest_cat[col]), X[col], 'Other'), dtype='category')
        Xt[continues_col] = X[continues_col].astype(float)
        return Xt

# COMMAND ----------

# DBTITLE 1,Create train and test data sets
cat_index = [ pd.Index(all_features).get_loc(col) for col in discrete_col ] 
df_train, df_test = df.iloc[:df.shape[0]//10*8,:],  df.iloc[df.shape[0]//10*8:,:]
smote_nc = SMOTENC(categorical_features=cat_index, k_neighbors=5,  random_state=0, n_jobs=-1)
topk = TakeTopK(50)
X_res, y_res = smote_nc.fit_resample(topk.fit_transform(df_train[all_features]), df_train.converted_user)

# COMMAND ----------

# DBTITLE 1,Define model evaluation for hyperopt
def evaluate_model(params):
  # instantiate model
  model = Pipeline([
        ('top_20', TakeTopK(50)),
        ('clf', lgb.LGBMModel(
             max_depth=int(params["max_depth"]),
            n_jobs=-1,
            scale_pos_weight=2,
            objective=params["objective"],
            metric=params["metric"],
            n_estimators=int(params["n_estimators"]),
            num_leaves=int(params["num_leaves"]),
            min_child_samples = int(params["min_child_samples"])
        ))    
  ])
  
  #train
  model.fit(X_res, y_res.astype(int))
  
  #predict
  y_pred = model.predict(df_test[all_features])
  
  #score
  precision = average_precision_score(df_test['converted_user'], y_pred)
  mlflow.log_metric('avg_precision', precision)  # record actual metric with mlflow run
  
  # return results (negative precision as we minimize the function)
  return {'loss': -precision, 'status': STATUS_OK, 'model': model}

# COMMAND ----------

# define hyperopt search space
search_space = {
    'max_depth': scope.int(hp.quniform('max_depth', 2, 8, 1)),
    'objective': hp.choice('objective', ['binary']),
    'metric': hp.choice("metric", ["binary_logloss"]),  
    'n_estimators':  scope.int(hp.quniform('n_estimators', 50, 200, 1)),
    'num_leaves': scope.int(hp.quniform('num_leaves', 20, 200, 10)),
    'min_child_samples': hp.quniform('min_child_samples', 5, 100, 5)
}

# COMMAND ----------

# DBTITLE 1,Perform evaluation to optimal hyperparameters
# perform evaluation
with mlflow.start_run(run_name='LightGBM') as run:
  trials = SparkTrials(parallelism=4)
  argmin = fmin(fn=evaluate_model, space=search_space, algo=tpe.suggest, max_evals=20, trials=trials)
  #log the best model information
  model = trials.best_trial['result']['model']
  signature = infer_signature(df_test[all_features], model.predict(X_res))
  mlflow.sklearn.log_model(trials.best_trial['result']['model'], 'model', signature=signature, input_example=df_test[all_features].iloc[0].to_dict())
  #add hyperopt model params
  for p in argmin:
    mlflow.log_param(p, argmin[p])
  mlflow.log_metric("avg_precision", trials.best_trial['result']['loss'])
  run_id = run.info.run_id

# COMMAND ----------

y_pred = np.where(model.predict(df_test[all_features]) > 0.5, 1, 0)
cm = confusion_matrix(df_test['converted_user'].fillna(False),   y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['not converted', 'converted'])
print(f"model score {fbeta_score(df_test['converted_user'].fillna(False),  y_pred, beta=2)}")
print(classification_report(df_test['converted_user'].fillna(False),   y_pred))
disp.plot()

# COMMAND ----------

lgb.plot_importance(model.steps[1][1], max_num_features=15)

# COMMAND ----------

# DBTITLE 1,Save our new model to the registry as a version
model_registered = mlflow.register_model("runs:/"+run_id+"/model", "demo_ccdp_lgbm")

# COMMAND ----------

# DBTITLE 1,Flag this version as production ready
client = mlflow.tracking.MlflowClient()
print("registering model version "+model_registered.version+" as production model")
client.transition_model_version_stage(name = "demo_ccdp_lgbm", version = model_registered.version, stage = "Production", archive_existing_versions=True)
