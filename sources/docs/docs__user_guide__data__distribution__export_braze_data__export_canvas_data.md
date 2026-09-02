---
url: https://www.braze.com/docs/user_guide/data/distribution/export_braze_data/export_canvas_data
slug: docs__user_guide__data__distribution__export_braze_data__export_canvas_data
title: "Export Canvas data"
description: "This reference article covers how to export Canvas analytics."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Export Canvas data

User data can be exported to a CSV. This page covers how to export data for your entire Canvas or a specific Canvas component.

## Exporting data for a Canvas

To export data for a Canvas, do the following:

- Go to Messaging > Canvas and select your Canvas.
 
- Select the User Data dropdown in the Canvas Details section.
 
- Select one of the following export options:

- CSV Export User Data or
 
- CSV Export Email Address.

You can also export user data for all the entrants of a Canvas as a CSV file.

## Export users who entered or re-entered a Canvas

When re-eligibility is enabled, users can enter the same Canvas more than once. The CSV Export User Data option on the Canvas details page exports users who entered the Canvas, but it doesn’t include how many times each user entered or each entry timestamp.

To analyze when users entered or re-entered a Canvas, use one of the following options:

- Most recent entry per user: Export a segment with the canvases_received field using the /users/export/segment endpoint. For each Canvas, the export includes last_entered and last_exited timestamps for that user. The canvases_received field contains data from the last 90 days.
 
- Every entry, including re-entries: Use Canvas Entry events in Braze Currents or Snowflake Data Sharing. Each users.canvas.Entry event represents one Canvas entry and includes a time timestamp. Count events per user to determine how many times they entered.
 
- Build a user list in the dashboard: Create a segment with an Entered Canvas Variation filter, then export the segment to CSV. See Canvas troubleshooting.

note

If you don’t have Currents integrated and need every historical entry timestamp, contact your Braze customer success manager.

For a specific Canvas step in the original workflow, use CSV Export User Data on the step’s details page.

## Exporting data for a component (original workflow only)

Canvas results can be exported on an individual component basis for the original Canvas workflow. To do this, select the specific component, then select the User Data dropdown in the Canvas Step Details page.

tip

For help with CSV and API exports, visit our export troubleshooting article.

- 

New Stuff!
