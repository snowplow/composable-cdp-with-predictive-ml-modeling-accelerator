+++
title = "Visualise Ad Campaign Performance"
weight = 1
+++

At this stage you will have at least one campaign up and running synced from a Hightouch audience.

#### **Step 1:** Marketing attribution in Snowplow
Snowplow allows you to gain full control of your marketing attribution.

Out of the box, the Snowplow JavaScript tracker captures both the page URL and the referrer URL. The [campaign attribution enrichment](https://docs.snowplow.io/docs/enriching-your-data/available-enrichments/campaign-attribution-enrichment/) can then parse out any marketing parameters that are present in the page URL, as well as click IDs from Google or other search engines. By default, it looks for the `utm_` fields, but other marketing parameters can be specified as well. The [referrer parser enrichment](https://docs.snowplow.io/docs/enriching-your-data/available-enrichments/referrer-parser-enrichment/) will also classify the referrer. Together, these two enrichments populate the following fields in atomic.events:

| Marketing fields | Referred fields |
| ---------------- | --------------- |
| mkt_medium       | refr_medium     |
| mkt_source	   | refr_source     |
| mkt_term	       | refr_term       |
| mkt_content	   |                 | 
| mkt_campaign     |                 | 
| mkt_network	   |                 |
| mkt_clickid	   |                 |

By default, Snowplow's dbt models marketing attribution on a first touch basis. So in the sessions table, the marketing and referrer information of the first page view in that session is saved.

To attribute conversions, you’ll also need to track conversion events. You'll then be able to model your data using different marketing attribution models like first touch, last touch and linear. See [Tutorial: Marketing attribution](https://docs.snowplow.io/docs/try-snowplow/recipes/recipe-marketing-attribution/) for more information.

#### **Step 2:** Ingest campaign data
Ingest your ad campaign data from your marketing tools into your data warehouse using ETL tools like [Fivetran](https://www.fivetran.com/). If you use multiple advertising sources, you now have a single source of truth and can easily query across all of them. 

#### **Step 3:** Build a dashboard
Being able to monitor and compare all your campaigns in one place is vital for your marketing teams to uncover true ROI.

![ad_campaign_dashboard](../images/ad_campaign_dashboard.png?width=100pc)

#### **Step 4:** Drill into Hightouch activated campaigns
Drill deeper into the performance of your Hightouch activated campaigns. Are certain audiences performing better than others? Audiences filtering on high propensity to convert users should see a better return on ad spend so check this is the case. If not there maybe there are ways to improve your ML model like adding new user features.

Below is an example of campaigns activated by two Hightouch audiences, *Awareness (ML Based)* and *Awareness (Rule Based)*, that have been running side by side. You can see the campaigns using ML outputs are achieving a much greater ROI. 

![ad_campaign_dashboard](../images/ad_campaign_dashboard_hightouch.png?width=100pc)
