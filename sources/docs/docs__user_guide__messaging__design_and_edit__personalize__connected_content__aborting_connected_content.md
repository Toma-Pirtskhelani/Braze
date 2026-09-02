---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content
slug: docs__user_guide__messaging__design_and_edit__personalize__connected_content__aborting_connected_content
title: "Abort Connected Content"
description: "This reference article covers some message aborting best practices for Connected Content."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Abort Connected Content

When you use Liquid templating, you have the option to abort messages with conditional logic. This page covers best practices when doing so.

In the following example, the conditionals connected.recommendations.size < 5 and connected.foo.bar == nil specify situations that would cause the message to be aborted.

```

1
2
3
4

```
 | 
```
{% connected_content https://example.com/webservice.json :save connected %}
 {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
 {% abort_message() %}
 {% endif %}

```
 | 

## Specify an abort reason

You can also specify an abort reason, which will be saved to the Message Activity Log. This abort reason must be a string and cannot contain Liquid.

{% abort_message('Could not get enough recommendations') %}

important

Braze doesn’t count aborted messages toward the send count in your Braze account or in Currents.

## Connected Content calls with abort and retry logic

If a Connected Content call uses abort logic for the same condition as the retry logic, the abort logic takes precedence. This prevents any retries from being attempted. Retry logic already resends the call before aborting it if the status code is unsuccessful. Because both target the same status code behavior, you can remove the abort logic and the call still aborts if all retries fail.

- 

New Stuff!
