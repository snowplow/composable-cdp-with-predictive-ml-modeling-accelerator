# Databricks notebook source
# MAGIC %md 
# MAGIC # Propensity to Convert ML Model Deployment
# MAGIC 
# MAGIC In this notebook we will be using sample behavioural data collected by Snowplow's Javascript tracker from Snowplow's [snowplow.io](https://snowplow.io/) website.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configuration
# MAGIC 
# MAGIC Please use a cluster with **11.2 ML CPU** Runtime.

# COMMAND ----------

# DBTITLE 1,Load the model from registry as UDF
import mlflow

#                                 Stage/version
#                       Model name       |
#                           |            |
model_path = 'models:/demo_ccdp_lgbm/Production'
predict_propensity = mlflow.pyfunc.spark_udf(spark, model_path, result_type='float')

# COMMAND ----------

# DBTITLE 1,Perform inference
model_features = predict_propensity.metadata.get_input_schema().input_names()
df = spark.table("snowplow_samples.samples.first_touch_user_features")

predictions = df.withColumn('propensity_score', predict_propensity(*model_features))

display(predictions.orderBy("propensity_score", ascending=False))

# COMMAND ----------

# DBTITLE 1,Add propensity deciles and labels
import pandas as pd

df = predictions.toPandas()
df["propensity_decile"] = pd.qcut(df["propensity_score"], 10, labels=False)
df["propensity_label"] = pd.cut(df["propensity_score"], [0., 0.33, 0.66, 1.0], include_lowest=True,
                                labels=['Low', 'Medium', 'High'])

# COMMAND ----------

# DBTITLE 1,Propensity score distribution
import plotly.express as px

fig = px.histogram(df, x="propensity_score", color="propensity_label", nbins=50, log_y=True)
fig.show()

# COMMAND ----------

# DBTITLE 1,Save scores to table
df_spark = spark.createDataFrame(df[["domain_userid", "propensity_score", "propensity_decile", "propensity_label"]])
df_spark.write.mode("overwrite").saveAsTable("snowplow_samples.samples.snowplow_user_propensity_scores")
