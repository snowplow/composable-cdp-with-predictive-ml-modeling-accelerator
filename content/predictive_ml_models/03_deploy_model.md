+++
title = "Deploying your Model"
weight = 3
+++

#### Deploying your ML model

Now that our model is built and saved in MLFlow registry, we can load it to run our predictions at scale using:
* In batch or streaming (ex: refresh every night)
  * Using a standard Databricks's notebook job
  * Or as part of the DLT pipeline we built
* In real-time over a REST API, deploying Databricks serving capabilities

Here is how you might deploy your model in a Databricks notebook:

{{< jupyter accelerator_deploying_model 1000 >}}
