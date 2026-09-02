---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events
slug: docs__user_guide__data__distribution__braze_currents__event_glossary__user_profiles_events
title: "User profiles"
description: "This glossary lists the user profile updates that Braze can track and send to chosen Data Warehouses using Currents."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# User profiles

Find the events you need to use Currents effectively. These schemas consist of the Braze Events that are directly related to user profile updates.

tip

These events are also available as SQL tables in the Query Builder, SQL Segment Extensions, and Snowflake Data Sharing. For SQL table schemas and column details, refer to the SQL table reference. For Snowflake Data Sharing schemas for user profile attribute views, refer to User profile attributes.

Contact your Braze representative or open a support ticket if you need access to additional event entitlements. If you can’t find what you need on this page, see the Customer Behavior Events Library, Message Engagement Events Library, or Currents sample data examples.

 Explanation of user profile update event structure

### Event structure

This customer behavior and user events breakdown shows what type of information is generally included in a user profile update event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

important

Storage schemas apply to flat file event data sent to data warehouse storage partners, such as Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage. Some event and destination combinations listed here are not yet generally available. For information about supported events by partner, see available partners and the related partner pages.

Currents drops events with payloads larger than 900 KB.

## User Delete Request events

when a user is deleted by customer request

- cloud storage
 
- custom http connector

```

1
2
3
4
5
6
7
8

```
 | 
```
// users.UserDeleteRequest

{
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
 "id" : "(required, string) Globally unique ID for this event",
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13

```
 | 
```
// users.UserDeleteRequest

{
 "event_type" : "(required, string) The name of the event type",
 "id" : "(required, string) Globally unique ID for this event",
 "properties" : {
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to"
 },
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "user" : {
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
 }
}

```
 | 

## User Orphan events

when a user is orphaned, meaning the user is merged with another user’s profile

- cloud storage
 
- custom http connector

```

1
2
3
4
5
6
7
8
9
10
11
12

```
 | 
```
// users.UserOrphan

{
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
 "app_id" : "(optional, string) API ID of the app on which this event occurred",
 "device_id" : "(optional, string) ID of the device on which the event occurred",
 "external_user_id" : "(optional, string) [PII] External ID of the user",
 "id" : "(required, string) Globally unique ID for this event",
 "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile",
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

```
 | 
```
// users.UserOrphan

{
 "event_type" : "(required, string) The name of the event type",
 "id" : "(required, string) Globally unique ID for this event",
 "properties" : {
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
 "app_id" : "(optional, string) API ID of the app on which this event occurred",
 "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile"
 },
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "user" : {
 "device_id" : "(optional, string) ID of the device on which the event occurred",
 "external_user_id" : "(optional, string) [PII] External ID of the user",
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
 }
}

```
 | 

## User Profile Update events

This represents the profile updates for a user.

important

The user profile update event is in beta. Contact your customer success manager or account manager for access.

- cloud storage
 
- custom http connector

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```
 | 
```
// users.profile.Update

{
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
 "app_id" : "(optional, string) API ID of the app on which this event occurred",
 "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
 "country" : "(optional, string) [PII] Country of the user",
 "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
 "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
 "email_address" : "(optional, string) [PII] Email address of the user",
 "external_user_id" : "(optional, string) [PII] External ID of the user",
 "first_name" : "(optional, string) [PII] First name of the user",
 "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
 "home_city" : "(optional, string) [PII] Home city of the user",
 "id" : "(required, string) Globally unique ID for this event",
 "language" : "(optional, string) [PII] Language of the user",
 "last_name" : "(optional, string) [PII] Last name of the user",
 "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "time_ms" : "(required, long) Time in milliseconds when the update happened",
 "timezone" : "(optional, string) Time zone of the user",
 "update_source" : "(required, string) The source of this update",
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}

```
 | 

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

```
 | 
```
// users.profile.Update

{
 "event_type" : "(required, string) The name of the event type",
 "id" : "(required, string) Globally unique ID for this event",
 "properties" : {
 "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
 "app_id" : "(optional, string) API ID of the app on which this event occurred",
 "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
 "country" : "(optional, string) [PII] Country of the user",
 "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
 "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
 "email_address" : "(optional, string) [PII] Email address of the user",
 "first_name" : "(optional, string) [PII] First name of the user",
 "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
 "home_city" : "(optional, string) [PII] Home city of the user",
 "language" : "(optional, string) [PII] Language of the user",
 "last_name" : "(optional, string) [PII] Last name of the user",
 "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
 "time_ms" : "(required, long) Time in milliseconds when the update happened",
 "update_source" : "(required, string) The source of this update"
 },
 "time" : "(required, int) UNIX timestamp at which the event happened",
 "user" : {
 "external_user_id" : "(optional, string) [PII] External ID of the user",
 "timezone" : "(optional, string) Time zone of the user",
 "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
 }
}

```
 | 

- 

New Stuff!
