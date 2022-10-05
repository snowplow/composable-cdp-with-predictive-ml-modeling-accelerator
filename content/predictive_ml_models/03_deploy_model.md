+++
title = "Using your Model"
weight = 3
+++

#### Predicting user's propensity to convert

Now that our model is built and saved in MLflow registry, we can load it to run our predictions at scale using:
* In batch or streaming (ex: refresh every night)
  * Using a standard Databricks's notebook job
  * Or as part of the DLT pipeline we built
* In real-time over a REST API, deploying Databricks serving capabilities

Here is how you might load and use your model in a Databricks notebook:

{{< jupyter accelerator_deploying_model 300 >}}

A great use for these propensity to convert scores is to pass them to your marketing tools to ensure your campaigns are only targeting website visitors that are likely to convert, minimizing cost per acquisition. The next chapter, [Data Activation]({{< ref data_activation >}}), guides you through how this can be done.
