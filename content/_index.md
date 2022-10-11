+++ title = "Composable Customer Data Platform" 
menuTitle="Introduction" 
chapter = false 
weight = 1 
pre = "<i class='fas fa-rocket'></i> "

aliases = [ 
    "/en", 
    "/en/introduction" 
]
+++

#### Introduction

Welcome to the **Composable CDP** accelerator.
This accelerator guides you through building a Composable CDP using a selection of excellent tools for each step of the process. 
* [**Snowplow**](https://snowplow.io/) for creating user behavioral data from your product.
* [**Databricks DeltaLake**](https://www.databricks.com/product/delta-lake-on-databricks) to store the data.
* [**Databricks** and **MLFlow**](https://www.databricks.com/product/managed-mlflow) for training and executing sophisticated ML predictions to determine a likelihood of conversion.
* [**Hightouch**](https://hightouch.com/) activation platform to synchronize the audience segment with marketing tools (like Braze, Salesforce and Facebook Ads) and accelerate their conversion into qualified leads. 

Once finished, you will be able to use predictive models to achieve a competitive advantage from customer behavior data on your website, driving higher return on ad spend.

![composable_cdp](images/composable_cdp.png)

(Data loaders like [Fivetran](https://www.fivetran.com/) can play an important role in a composable CDP. 
In this accelerator we don't go into detail on setting these up, see [Fivetran's Documentation](https://fivetran.com/docs/destinations/databricks) if you want to learn more.)

***

#### Who is this guide for?

- Data scientists who would like to learn how Snowplow behavioral data can be used to build predictive ML models
- Data practitioners who want to learn how to activate Snowplow behavioral data in third party tools

***

#### What you will learn

In approximately 1 working day (~6 working hours) you can achieve the following:
- **Build a predictive model -** Using Databricks and MLflow to build a machine learning model that can accurately predict conversion events using features collected from Snowplow's out-of-the-box modelled data
- **Data activation -** With Hightouch connected to your rich user data in Databricks, you can enable your marketing teams to effortlessly build new audiences and sync to their needed destinations
- **Next steps -** Productionalize your ML model and visualize ad campaign performance synced from your Hightouch audiences

{{<mermaid>}}
gantt
        dateFormat  HH-mm
        axisFormat %M
        section 1. Predict
        2h          :step1, 00-00, 2m
        section 2. Activate
        1h          :step2, after step1, 1m
        section 3. Next Steps
        3h          :step3, after step2, 3m

{{</mermaid>}}

***

#### Prerequisites

{{% notice tip %}}
Complete our [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web/) accelerator if you don't have any Snowplow modelled web data in your warehouse yet. You don't need a working Snowplow pipeline, a sample events dataset is provided.
{{% /notice %}}

**Predictive ML Modelling**
- Snowplow modelled web data (*page views*, *sessions* and *users*) stored in your Databricks warehouse
- Conversion events, these can be derived from a Snowplow tracked event or using other sources like Salesforce data.
- Databricks account and a user with access to create schemas and tables
- Use of a Databricks ML Cluster on runtime 11.2

**Data Activation**
- Snowplow modelled web data (*page views*, *sessions* and *users*) stored in your Databricks warehouse
- Hightouch account and a user with admin role

#### What you will build

A propensity to convert ML model that empowers you to intelligently market campaigns to website visitors that are most likely to convert.

![ad_campaign_dashboard](next_steps/images/ad_campaign_dashboard_hightouch.png?width=100pc)
