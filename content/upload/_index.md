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
    id1(Upload)-->id2(Predict)-->id3(Activate)-->id4(Next steps)
    style id1 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


If you are using the sample events dataset from the [Advanced Analytics for Web](https://docs.snowplow.io/advanced-analytics-web-accelerator) accelerator, a table of converted users has been provided. This can be joined to your modelled tables on `domain_userid` and will allow you to be able to create a training dataset for your ML models, without the need to have a working pipeline. This chapter will guide you through this process.

**If you are not using the sample events, please skip to the next chapter, Predictive ML Modelling.**
