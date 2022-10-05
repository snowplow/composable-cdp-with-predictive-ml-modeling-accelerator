+++
title = "Feature Exploration"
weight = 1
+++

#### Explore user features

Primary features returned from the Snowplow dbt web model can be grouped into categories based on their origin:

* **Temporal** – created from first event timestamp: an hour of the day, day of the week.
* **Landing Page** – page title of the first URL, comes out of the box
* **Device** –  User Agent enrichment
* **Referral** – Referral enrichment
* **Marketing** –  Marketing campaign enrichment
* **Geographic** – IP lookup enrichment
* **Engagement** – Accumulated page ping events by dbt page view model

#### Collect user features from Snowplow derived tables
First we need to create a view or table of users features based on their first website visit. **If you are using your own conversion flag ensure you include this so we are ready to train and test our models.** Conversion can be derived from a Snowplow tracked event or using other sources like Salesforce data. 
In this example we are joining onto a `converted_users` table, which contains a list of all users that have converted. If you are using the sample dataset this will be the table you uploaded in the [Upload Sample Data]({{< ref upload >}}) chapter.

```sql
create or replace view first_touch_user_features as (
    with pv as (
        select
            domain_userid,
            absolute_time_in_s,
            vertical_percentage_scrolled,
            geo_country,
            geo_region,
            br_lang,
            device_family,
            os_family,
            row_number() over (
                partition by domain_userid order by start_tstamp
            ) as rn
        from snowplow_web_page_views
        where page_view_in_session_index = 1
        qualify rn = 1
    )

    select
        u.domain_userid,
        u.first_page_title,
        u.refr_urlhost,
        u.refr_medium,
        u.mkt_medium,
        u.mkt_source,
        u.mkt_term,
        u.mkt_campaign,
        u.engaged_time_in_s,
        pv.absolute_time_in_s,
        pv.vertical_percentage_scrolled,
        pv.geo_country,
        pv.geo_region,
        pv.br_lang,
        pv.device_family,
        pv.os_family,
        coalesce(c.converted, false) as converted_user -- Your conversion flag here
    from snowplow_web_users u
    inner join
        pv on u.domain_userid = pv.domain_userid
    left join
        converted_users c on
            u.domain_userid = c.domain_userid
)

```

Here we have just selected a few of the features Snowplow behavioral data has to offer. You can include more columns before going through feature engineering as you start using ML to predict more and more types of user behavior, building out a richer view of each of your customers / users. 

Consider adding this step as a custom model in dbt so the table is kept up to date when your ML model is in production. Read more about adding custom dbt models [here](https://snowplow.github.io/dbt-snowplow-web/#!/overview/snowplow_web).
