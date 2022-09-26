+++ title = "Composable Customer Data Platform" 
menuTitle="Introduction" 
chapter = false 
weight = 1 
post = ""

aliases = [ 
    "/en", 
    "/en/introduction" 
]
+++

#### Introduction

Welcome to the **Composable CDP** accelerator.
This accelerator demonstrates the concept of a Composable CDP by using the best-in-class tools for each step of the process. 
* **Snowplow** for getting user behavioural data from your product.
* **Databricks DeltaLake** to store the data.
* **Databricks** and **MLFlow** for training and executing sophisticated ML predictions to determine a likelihood of conversion.
* **Hightouch** activation platform to synchronize the audience segment with marketing tools (like Braze, Salesforce and Facebook Ads) and accelerate their conversion into the qualified leads. 

![composable_cdp](images/composable_cdp.png)

Once finished, you will be able to use predictive models to achieve a competitive advantage from customer behavoir data on your website, for example driving higher return on ad spend.

***

#### Who is this guide for

- Data scientists who would like to learn how Snowplow behavourial data can be used to build predictive ML models
- Data practitioners who want to learn how to activate Snowplow behavourial data in third party tools

***

#### What you will learn

In approximately 2 working days (~13 working hours) you can achieve the following:
- **Build a predictive model -** Using Databricks and MLflow to build a machine learning model that can accurately predict conversion events using features collected from Snowplow's out-of-the-box modelled data.
- **Data activation -** With Hightouch connected to your rich user data in Databricks, you can enable our marketing teams to effortlessly build new audiences and sync to their needed destinations.
- **Next steps -** Gain value from your own pipeline data.

***

#### Prerequisites

- Snowplow modelled web data (*page views*, *sessions* and *users*) stored in your Databricks warehouse

{{% notice tip %}}
Complete our [Advanced Analytics for Web](https://docs.snowplow.io/advanced-analytics-web-accelerator/en/introduction/) accelerator if you don't have any Snowplow modelled web data in your warehouse yet. You don't need a working Snowplow pipeline, a sample events dataset is provided.
{{% /notice %}}

**Predictive ML Modelling**
- Databricks account and a user with access to create schemas and tables
- Use of a Databricks ML Cluster on runtime 11.2

**Data Activation**
- Hightouch account and a user with admin role
