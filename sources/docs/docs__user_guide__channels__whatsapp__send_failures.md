---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/send_failures
slug: docs__user_guide__channels__whatsapp__send_failures
title: "Investigate WhatsApp send failures"
description: "Use campaign analytics, the Message Activity Log, and Currents to investigate WhatsApp send failures and common Meta error codes."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Investigate WhatsApp send failures

Use this page when WhatsApp deliveries or reads are lower than expected, or when Failures in campaign analytics look elevated.

## Investigation workflow

Work through the following steps in order.

- Confirm failures in campaign or Canvas analytics. Open the message step and review the Failures count and failure rate. If failures look elevated compared to sends or deliveries, continue to the next step.
 
- Find the error code in the Message Activity Log. Open the Message Activity Log for the same send, filter to failed messages, and note the provider error code (for example, 131049 for per-user marketing limits). Use Common failure codes to interpret the code and decide next steps.
 
- Export failures with Currents for analysis or retargeting. After you know the error code, export WhatsApp send failure events through Currents. Use that data to analyze failure trends in your warehouse or to build segments and retarget users on another channel.

## Common failure codes

 Error code | 
 Typical cause | 
 Next step | 

 131049 | 
 Meta per-user marketing frequency limit or US marketing pause | 
 See Meta resources and Retargeting users on other Braze channels | 

 130472 | 
 Meta marketing experiment holdout | 
 See Meta resources FAQ | 

 131026 | 
 Various non-delivery reasons (Meta doesn’t disclose specifics) | 
 Avoid immediate retries; review Meta Cloud API troubleshooting | 

- 

New Stuff!
