---
url: https://www.braze.com/docs/user_guide/administer/global/admin_settings/contact_information
slug: docs__user_guide__administer__global__admin_settings__contact_information
title: "Contact information"
description: "This reference article covers important information for admins on managing your company's contact information and time zone in Braze."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Contact information

As an admin, you can use the Contact Information page to manage your company’s contact information and time zone in Braze.

To access this page, go to Settings > Admin Settings > Contact Information. Make sure to select Save to apply any changes before you leave the page.

## Consequences of switching your time zone

warning

Switching time zones can cause data discrepancies around the period when the time zone was changed. If you switch your time zone, Braze makes a good-faith effort to convert things over accurately, but does not guarantee a perfect conversion. You may notice a discontinuity in your data, where it may switch between time zones.

If you choose to switch your time zone, you may experience a variety of consequences, including:

- While campaigns scheduled for specific times in specific locations (such as 9 pm Eastern Time) will run properly on schedule until edited, both campaign analytics and future campaign schedules will be affected by the change.
 
- Any card scheduling that is not assigned to local time may be affected, with active cards potentially appearing as finished or the other way around.
 
- Segmentation filters of the form “Has done X before/after Date” will have the time adjusted because the initial date will now be localized in your workspace’s default time zone (for example, Pacific Time).

- 

New Stuff!
