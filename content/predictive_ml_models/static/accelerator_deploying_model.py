# Databricks notebook source
# MAGIC %md 
# MAGIC # Propensity to Convert ML Model Usage
# MAGIC 
# MAGIC In this notebook we will be using sample behavioral data collected by Snowplow's Javascript tracker from Snowplow's [website](https://snowplow.io/). 
# MAGIC 
# MAGIC Using our production propensity model, we will perform predictions on users from this dataset and save the output to a new table to feed into marketing campaigns. 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configuration
# MAGIC 
# MAGIC Please use a cluster with **11.2 ML CPU** Runtime.

# COMMAND ----------

# DBTITLE 1,Import libraries
import mlflow
import pandas as pd
import plotly.express as px

# COMMAND ----------

# MAGIC %md
# MAGIC ### Perform predictions
# MAGIC Load and use your model to predict propensity to convert.

# COMMAND ----------

# DBTITLE 1,Load the model from MLflow registry as a UDF
#                                 Stage/version
#                       Model name       |
#                           |            |
model_path = 'models:/demo_ccdp_lgbm/Production'
predict_propensity = mlflow.pyfunc.spark_udf(spark, model_path, result_type='float')

# COMMAND ----------

# DBTITLE 1,Perform predictions
model_features = predict_propensity.metadata.get_input_schema().input_names()
df = spark.table("snowplow_samples.samples.first_touch_user_features")
predictions = df.withColumn('propensity_score', predict_propensity(*model_features))

display(predictions.orderBy("propensity_score", ascending=False))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Save predictions
# MAGIC 
# MAGIC Depending on your use case, it can be useful to bucket these propensity scores using deciles or cut them into labels like *High*, *Medium* and *Low* propensity. This makes it easier for data consumers to use these predictions, for example, to filter marketing campaign audiences. Either save your scores to a new table, or add them into your main user table.

# COMMAND ----------

# DBTITLE 1,Add propensity deciles and labels
df = predictions.toPandas()
df["propensity_decile"] = pd.qcut(df["propensity_score"], 10, labels=False)
df["propensity_label"] = pd.cut(df["propensity_score"], [0., 0.33, 0.66, 1.0], include_lowest=True,
                                labels=['Low', 'Medium', 'High'])

# COMMAND ----------

# DBTITLE 1,Propensity score distribution
fig = px.histogram(df, x="propensity_score", color="propensity_label", nbins=50, log_y=True)
fig.show()

# COMMAND ----------

# DBTITLE 1,Save scores to table
df_spark = spark.createDataFrame(df[["domain_userid", "propensity_score", "propensity_decile", "propensity_label"]])
df_spark.write.mode("overwrite").saveAsTable("snowplow_samples.samples.snowplow_user_propensity_scores")

display(df_spark)
