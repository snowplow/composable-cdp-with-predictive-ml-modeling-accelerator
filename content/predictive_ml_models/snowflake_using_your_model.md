+++
title = "Snowflake Using your Model"
weight = 5
+++

#### Predicting user's propensity to convert

Now that your model is built and saved in Snowflake, here is how you can create a Snowflake UDF to get new predictions.

Clone this [notebook](https://github.com/snowplow/composable-cdp-with-predictive-ml-modeling-accelerator/blob/main/content/predictive_ml_models/static/snowflake_deploying_model.ipynb) into your own workspace to run this model for yourself.

{{< jupyter snowflake_deploying_model 500 >}}

Now you are ready to use your model output for activation via Hightouch. The next chapter, [Data Activation]({{< ref data_activation >}}), guides you through how to target high propensity visitors to optimize ad spend.
