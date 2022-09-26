+++
title="Tracking"
chapter = true
weight = 6
pre = "5. "
post = ""
+++

# Tracking

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Predict)-->id4(Activate)-->id5(Track)-->id6(Enrich)-->id7(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id7 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

Getting started with sending events using the JavaScript tracker is very similar to other web analytics vendors like Google Analytics and Adobe Analytics.

Once set-up, you will have the ability to send behavioral data to your Snowplow pipeline.