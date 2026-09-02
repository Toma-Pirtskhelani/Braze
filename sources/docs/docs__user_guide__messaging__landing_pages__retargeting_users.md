---
url: https://www.braze.com/docs/user_guide/messaging/landing_pages/retargeting_users
slug: docs__user_guide__messaging__landing_pages__retargeting_users
title: "Retarget users through a landing page"
description: "Learn how to retarget users who've submitted a form through a landing page."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Retarget users through a landing page

Learn how to retarget users who’ve submitted a form through a landing page by creating a dedicated segment or triggering a message when the form is submitted.

## Prerequisites

Before you start, create a landing page.

## Retargeting users

Braze automatically tracks when a user submits a landing page form. You can view the total number of submissions for a form under landing page analytics. For user-specific retargeting, retarget users through your landing page form using one of the following methods:

- using a segment
 
- using a message trigger

Create a new segment to automatically identify users who have or haven’t submitted a landing page form. When you create a segment, under “Retargeting” group, choose Submitted Form on Landing Page.

From here, you can segment users based on whether they have or haven’t submitted a landing page form for your landing page.

Set up a message trigger to automatically message users or enter them into a Canvas after they submit the form. When you choose your delivery option for your campaign or Canvas, select Action Based Delivery, then Submitted a Landing Page form.

All users who submit a form through this landing page form are either messaged through the chosen messaging channel or entered into the chosen Canvas.

note

The action-based delivery option for landing pages isn’t available for in-app messages. To target users who have submitted a form on a landing page with an in-app message, select the Submitted Form on Landing Page filter in the Targeting Options of your campaign.

### Multi-step form

For a multi-step form, both retargeting methods rely on the Submitted a Landing Page form event, which only logs after a user completes every step. A user who submits some but not all steps is saved to their profile but isn’t included in either method until they complete the entire form. For more information, see Track data from partially completed forms.

- 

New Stuff!
