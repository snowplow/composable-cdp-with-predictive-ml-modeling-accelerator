+++
title = "Create an Audience"
weight = 2
+++

#### **Step 1:** Create a parent model

First you need to create a [parent model table](https://hightouch.com/docs/audiences/schema#the-parent-model-table) for the audiences to be built off of. This can be based on your out-of-the-box Snowplow modelled `snowplow_web_users` table or any custom user tables you have built.

#### **Step 2:** Audience builder

Now you can build an audience using columns from your parent model. In this example we are targetting users in the awareness stage based on the following criteria:
* First time on website
* Did not arrive from a marketing campaign
* **High** propensity score

![hightouch_audience_builder](../images/hightouch_audience_builder.png?width=30pc)

You can see we have utilised a [related model](https://hightouch.com/docs/audiences/schema#other-objects) *User Propensity Scores*. This model is based on the table of propensity scores outputted by your predictive ML model. You can join other source tables like this to your user parent model.

#### **Step 3:** Add Hightouch Events (Optional)
It can be useful to flag key user behavoir like adding a product to basket or filling out a form as a Hightouch [Event](https://hightouch.com/docs/audiences/schema#events). Similary to related models, these can then be joined onto the parent model to filter your audiences by.

For example, you may want to filter an audience by if or when the user had viewed a certain page on your website. You can make this an audience event using the following query on your `snowplow_web_page_views` table:

```sql
select 
  domain_userid,
  page_view_id,
  start_tstamp
from dbt_cloud_derived.snowplow_web_page_views
where page_urlpath like '/get-started/%'
```
Once you have created the event and added the relationship to our parent model, you can use it as an audience filter.
![hightouch_example_event](../images/hightouch_example_event.png?width=30pc)

#### **Step 4:** Audience Splits (Optional)

Use [Audience Splits](https://hightouch.com/blog/audience-splits) to manage A/B and  multivariate testing across your channels. You can also add stratification variables to ensure that the randomized groups of users are distributed as desired. 

![hightouch_splits](../images/hightouch_splits.png?width=40pc)
