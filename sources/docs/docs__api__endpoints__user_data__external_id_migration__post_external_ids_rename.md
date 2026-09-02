---
url: https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename
slug: docs__api__endpoints__user_data__external_id_migration__post_external_ids_rename
title: "Rename external ID"
description: "This article outlines details about the Rename external IDs endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Rename external ID

post

/users/external_ids/rename

Use this endpoint to rename your users’ external IDs.

You can send up to 50 rename objects per request.

This endpoint sets a new (primary) external_id for the user and deprecates their existing external_id. This means that the user can be identified by either external_id until the deprecated one is removed. Having multiple external IDs allows for a migration period so that legacy versions of your apps that use the previous external ID naming schema don’t break. The profile remains fully functional under both identifiers during the migration window—the Braze SDK, REST API, and messaging pipelines can continue to reference the user by either ID until the deprecated one is explicitly removed.

After your old naming schema is no longer in use, we highly recommend removing deprecated external IDs using the /users/external_ids/remove endpoint.

warning

Make sure to remove deprecated external IDs with the /users/external_ids/remove endpoint instead of /users/delete. Sending a request to /users/delete with the deprecated external ID deletes the user profile entirely and cannot be undone.

## How renaming works

When you call this endpoint, it assigns a new primary external_id to a user profile while simultaneously converting the previous primary external_id into a deprecated external ID. After a successful rename, the user profile holds exactly one primary external_id (the new value) and one deprecated external ID (the old value).

Subsequent rename calls on the same profile are permitted: each rename creates an additional deprecated external ID, so a profile may accumulate one primary external_id and multiple deprecated external IDs over time. However, the new_external_id value must not already exist on any Braze profile, either as a primary or a deprecated external ID.

The endpoint does not log data points and does not affect MAU counts. All historical user data—events, purchases, attributes, campaign engagement—remains attached to the same profile.

See me in Postman

## Prerequisites

To use this endpoint, you’ll need an API key with the users.external_ids.rename permission.

## Rate limit

We apply a rate limit of 1,000 requests per minute to this endpoint, as documented in API rate limits.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY

```
 | 

```

1
2
3

```
 | 
```
{
 "external_id_renames" : (required, array of external ID rename objects)
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 external_id_renames | 
 Required | 
 Array of external identifier rename objects | 
 View request example and the following limitations for the structure of the external identifier rename object. | 

Note the following:

- The current_external_id must be the user’s primary ID, and cannot be a deprecated ID. If the value passed as current_external_id is itself a deprecated ID on the profile, the call will fail. Before retrying a failed rename, use the /users/export/ids endpoint to confirm which ID is currently primary.
 
- The new_external_id must not already be in use as either a primary ID or a deprecated ID. Attempting to rename to an ID that is already stored as a deprecated ID returns a “new_external_id is already in use” error.
 
- The current_external_id and new_external_id cannot be the same.

## Request example

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "external_id_renames" :[
 {
 "current_external_id": "existing_external_id",
 "new_external_id" : "new_external_id"
 }
 ]
}'

```
 | 

## Response

The response will confirm all successful renames, as well as unsuccessful renames with any associated errors. Error messages in the rename_errors field will reference the index of the object in the array of the original request.

```

1
2
3
4
5

```
 | 
```
{
 "message" : (string) status message,
 "external_ids" : (array of strings) successful rename operations,
 "rename_errors": (array of arrays) <minor error message>
}

```
 | 

The message field will return success for any valid request. More specific errors are captured in the rename_errors array. The message field returns an error in the case of:

- Invalid API key
 
- Empty external_id_renames array
 
- external_id_renames array with more than 50 objects
 
- Rate limit hit (more than 1,000 requests per minute)

## Bulk migrations

For migrations involving large user populations, batch users into groups of up to 50 and send each batch as a separate API call. The endpoint is subject to a rate limit of 1,000 requests per minute. At maximum batch size (50 objects per request), this allows up to 50,000 user renames per minute.

Each rename object in the batch is processed independently. A failure on one object does not block the others in the same request. The response body distinguishes successful renames (listed in the external_ids array) from failed ones (listed in the rename_errors array with an index reference back to the position of the failing object in the request array).

When running bulk migrations:

- Iterate through the full user population in batches of up to 50 pairs.
 
- On each response, inspect both external_ids (success) and rename_errors (failure) to identify any users that need to be retried.
 
- Collect failed objects and schedule retry batches separately. Common failure causes include the new_external_id already being in use, or the current_external_id being a deprecated ID rather than a primary ID.
 
- Log successes and failures against your own records so the migration state is tracked outside Braze.

## Verifying the current external ID

During a migration, you may need to confirm which external ID is the active primary identifier on a given profile—for example, when determining whether a specific user has already been migrated, or when troubleshooting a failed rename. Use the /users/export/ids endpoint for this purpose.

The export endpoint resolves both primary and deprecated external IDs to the same underlying profile and always returns the current primary external_id in the response. This means you can query any known identifier for a user—old or new—and the response will contain the canonical primary ID. This is a reliable way to determine migration state.

To check only the external ID (rather than pulling the full profile), pass fields_to_export with only the external_id field.

## Recommended migration workflow

For most migration use cases, the recommended sequence is:

- Test in staging — Run the full rename-and-verify flow against a development or staging workspace before touching production.
 
- Rename in batches — Use the /users/external_ids/rename endpoint in batches of up to 50, handling rename_errors on each response and queuing failed pairs for retry.
 
- Verify — After each batch (or at the end of migration), spot-check profiles using /users/export/ids to confirm the expected primary external_id is set.
 
- Maintain the deprecation window — Keep deprecated external IDs active for as long as any system (including legacy app versions in the field) may still reference the old IDs. Don’t rush this step.
 
- Remove deprecated IDs — Once all systems are confirmed to be using the new IDs, use /users/external_ids/remove in batches of up to 50 to clean up.

If you’re also migrating your SDK integration (for example, changing the value passed to changeUser), coordinate the API-side rename with the app release schedule so that the new external ID is in use on both the server and the client before deprecated IDs are removed.

## Frequently asked questions

### Does this impact MAU?

No, because the number of users stays the same, they have a new external_id.

### Does user behavior change historically?

No, because the user is still the same, and all their historical behavior is still connected to them.

### Can it be run on development or staging workspaces?

Yes. In fact, we highly recommend running a test migration on a staging or development workspace, and ensuring everything has gone smoothly before executing on production data.

### Does this log data points?

This feature does not log data points.

### What is the recommended deprecation period?

We have no hard limit on how long you can keep deprecated external IDs around, but we highly recommend removing them after there is no longer a need to reference users by the deprecated ID.

### How many deprecated external IDs can a profile have?

A user profile can hold one primary external_id and any number of deprecated external IDs accumulated through successive rename operations. There is no documented cap on the number of deprecated IDs a single profile can hold, but Braze recommends removing them as soon as they are no longer needed.

- 

New Stuff!
