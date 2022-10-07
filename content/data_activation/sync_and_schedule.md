+++
title = "Sync and Schedule"
weight = 3
+++

#### **Step 1:** Sync your audiences to your destinations

After setting up your required [destinations](https://hightouch.com/integrations) in Hightouch you can sync up your new audiences. 

![hightouch_syncs](../images/hightouch_syncs.png?width=40pc)


#### **Step 2:** Schedule your audience syncs

It is important that your audiences connected to these third party tools are always up to date and in sync with our Snowplow web data in Databricks. 

One way you can ensure this is by using the [dbt Cloud extension](https://hightouch.com/docs/syncs/dbt-cloud) to trigger syncs after the dbt Snowplow web model job finishes and the derived tables are updated.

![hightouch_dbt_schedule](../images/hightouch_dbt_schedule.png?width=40pc)
