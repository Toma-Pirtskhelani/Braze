---
url: https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys
slug: docs__user_guide__messaging__landing_pages__create_landing_pages__surveys
title: "Landing page surveys"
description: "Learn how to create surveys on Braze landing pages, review responses, and retarget users."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Landing page surveys

Braze surveys collect feedback on landing pages that you can analyze and use in follow-up messaging. Surveys are built in the landing page drag-and-drop editor.

For an overview of Surveys and the capabilities shared across channels, see Surveys.

## Prerequisites

Before creating a survey, you must:

- Have access to landing pages in your Braze workspace
 
- Be familiar with creating landing pages

## Create a survey

Surveys are built inside your existing message composition flow.

- Go to Messaging > Landing Pages.
 
- Create a new landing page.
 
- Select Survey as your message type.

## Use survey form blocks

For shared styling and composition controls, see:

- Landing page form blocks

You can add the following form blocks to surveys:

- Phone capture
 
- Email capture
 
- Radio button group
 
- Short text capture
 
- Long text capture
 
- Dropdown
 
- Single checkbox
 
- Checkbox group
 
- Rating scale
 
- NPS

### Randomize answer choices

Radio button group, checkbox group, and dropdown blocks support randomized answer choices. Turn on Randomize choice order to shuffle the choices each time the survey loads. For more information, see Randomized choice order.

### Long text capture

Long text capture is useful for qualitative feedback, up to 1,000 characters. For more information, see Long-form text capture.

### Rating scale

Rating scale (also called a number scale question) is useful for capturing sentiment, satisfaction, or likelihood to recommend as a single number. For more information, see Number scale questions.

## Configure required fields and attributes

For each form block, enter an Identifier for Reporting in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

Keep in mind:

- You can log most survey responses to user profile custom attributes.
 
- Long text responses can’t be logged as custom attributes.
 
- If you choose not to log a response as a user attribute, you can’t segment users by that response value.

## View reporting and analytics

After launch, review results in:

- The landing page analytics view for landing page surveys

For definitions of the top-level analytics available for every survey (all responses, completed, partially complete, and unique impressions), see Analytics.

note

Landing page surveys track partially complete responses when the survey uses multi-step forms.

You can also review per-question response breakdowns, choose among three chart types, and export data as CSV. For more information, see Chart types.

## Retarget and trigger

You can:

- Segment users by survey responses that are logged as user attributes.
 
- Segment users by survey completion status.

- Trigger campaigns and Canvases when a user completes a survey on a landing page.

### Limitations

You’re restricted by the following:

- You can’t segment users by long-form text responses.
 
- Question-and-answer triggering that does not rely on logged user attributes is not available.

- 

New Stuff!
