+++
title="Upload sample data"
chapter = true
weight = 2
pre = "1. "
post = ""
+++

# Upload sample data

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Predict)-->id4(Activate)-->id5(Track)-->id6(Enrich)-->id7(Next steps)
    style id1 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id7 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

A sample events dataset for your Databricks warehouse has been provided. This will allow you to be able to start data modeling and getting familiar with Snowplow event data, without the need to have a working pipeline. This chapter will guide you through this process.