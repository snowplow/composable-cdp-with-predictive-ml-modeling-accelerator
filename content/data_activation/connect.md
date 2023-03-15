+++
title = "Connect Data Warehouse to Hightouch"
weight = 1
+++

You can easily connect to Hightouch from your data warehouse using either [Databricks Partner Connect](https://docs.databricks.com/integrations/partner-connect/reverse-etl.html) or [Snowflake Partner Connect](https://hightouch.com/blog/hightouch-snowflake-partner-connect).

1. Make sure your data warehouse account, workspace, and the signed-in user all meet the necessary requirements for Partner Connect.
2. In the sidebar, click **Partner Connect**.
3. Find the Hightouch tile. If the tile has a check mark icon, stop here, as your workspace is already connected.

![hightouch_partner_connect](../images/hightouch_partner_connect.png?width=30pc)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Otherwise, follow the on-screen directions to finish creating the connection.

![hightouch_partner_connect_instructions](../images/hightouch_partner_connect_instructions.png?width=50pc)

Once set-up you should see your new connection under the Sources tab in Hightouch:

![hightouch_sources](../images/hightouch_sources.png?width=40pc)

Alternatively you can connect to Hightouch manually with [Databricks](https://docs.databricks.com/integrations/reverse-etl/hightouch.html#connect-to-hightouch-manually) or [Snowflake](https://hightouch.com/docs/sources/snowflake).
