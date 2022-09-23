+++
title = "Connect Databricks to Hightouch"
weight = 1
+++

You can easily connect to Hightouch from Databricks using [Partner Connect](https://docs.databricks.com/integrations/partner-connect/reverse-etl.html).

1. Make sure your Databricks account, workspace, and the signed-in user all meet the [requirements](https://docs.databricks.com/integrations/partner-connect/index.html#requirements) for Partner Connect.
2. In the sidebar, click **Partner Connect**.
3. Find the Hightouch tile. If the tile has a check mark icon, stop here, as your workspace is already connected. Otherwise, follow the on-screen directions to finish creating the connection.

![hightouch_partner_connect](../images/hightouch_partner_connect.png?width=50pc)
Once setup you should see your Databricks cluster under the Sources tab in Hightouch:

![hightouch_sources](../images/hightouch_sources.png?width=40pc)

Alternativley you can [connect to Hightouch manually](https://docs.databricks.com/integrations/reverse-etl/hightouch.html#connect-to-hightouch-manually).
