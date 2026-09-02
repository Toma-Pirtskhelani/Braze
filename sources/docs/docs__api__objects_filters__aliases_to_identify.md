---
url: https://www.braze.com/docs/api/objects_filters/aliases_to_identify
slug: docs__api__objects_filters__aliases_to_identify
title: "Aliases to identify object"
description: "This article explains aliases to identify object specification."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Aliases to identify object

An API request with any fields in the attributes object creates or updates an attribute of that name with the given value on the specified user profile.

Use Braze user profile field names (listed as follows or any listed in the section for Braze user profile fields) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

## Object body

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

```
 | 
```
{
 "aliases_to_identify" : (required, array of aliases to identify object)
 [
 {
 "external_id" : (required, string) see External user ID,
 // external_ids for users that do not exist return a non-fatal error.
 // See server responses for details.
 "user_alias" : {
 "alias_name" : (required, string) see User aliases,
 "alias_label" : (required, string) see User aliases
 }
 }
 ]
}

```
 | 

- External user ID
 
- User aliases

- 

New Stuff!
