+++
title="Modelling"
chapter = true
weight = 3
pre = "2. "
post = ""
+++

# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Predict)-->id4(Activate)-->id5(Track)-->id6(Enrich)-->id7(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id7 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

The [snowplow-web dbt package](https://hub.getdbt.com/snowplow/snowplow_web/latest/) transforms and aggregates the raw web event data collected from the [Snowplow JavaScript tracker](https://github.com/snowplow/snowplow-javascript-tracker) into a set of derived tables: *page views, sessions* and *users*. Modeling the data makes it easier to digest and derive business value from the Snowplow data either through AI or BI.

In this chapter you will learn how to set-up an run the snowplow-web package to model the sample data.