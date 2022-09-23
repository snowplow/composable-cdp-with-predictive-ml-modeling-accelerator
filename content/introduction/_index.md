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

Here you will learn to:

* Build a predictive model
    - using our sample data for Databricks (no need to have a working pipeline)
* Activate your data using Hightouch
* Apply what you have learned to your own pipeline

***

#### Who is this guide for

- Data scientists who would like to learn how Snowplow behavourial data can be used to build predictive ML models
- Data practitioners who want to learn how to activate Snowplow behavourial data in third party tools

***

#### What you will learn

In approximately 2 working days (~13 working hours) you can achieve the following:
- **Upload data -** Upload a sample Snowplow events dataset to your Databricks lakehouse
- **Build a Predictive model -** Using Using MLflow to build a machine learning model that can accurately predict conversion events using features collected from Snowplow's out-of-the-box modelled data.
- **Data activation -** With Hightouch connected to our rich user data in Databricks, we can enable our marketing teams to effortlessly build new audiences and sync to their needed destinations.
- **Next steps -** Gain value from your own pipeline data.

***

#### Prerequisites

**Modeling**
- dbt CLI installed / dbt Cloud account available
  - New dbt project created and configured
- Python 3 Installed
- Databricks account and a user with access to create schemas and tables
- Use of a Databricks ML Cluster on runtime 11.2
- Hightouch account and a user with admin role

**Tracking and Enrichment**
- Snowplow pipeline
- Web app to implement tracking
