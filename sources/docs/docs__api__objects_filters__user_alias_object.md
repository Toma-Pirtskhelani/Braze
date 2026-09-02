---
url: https://www.braze.com/docs/api/objects_filters/user_alias_object
slug: docs__api__objects_filters__user_alias_object
title: "User alias object"
description: "This reference article explains the different components of the user alias object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# User alias object

An alias serves as an alternative unique user identifier. By using a user alias object, you can set a consistent identifier for analytics that will follow a given user both before and after they have logged in to a mobile app or website. You can also use this object to add the identifiers used by a third-party vendor to your company users to more easily reconcile your data externally.

The user alias object consists of two parts: an alias_name for the identifier itself, and an alias_label indicating the type of alias. Users can have multiple aliases with different labels, but only one alias_name per alias_label.

This object is used frequently in all of our endpoints, and oftentimes within other objects.

## Object body

```

1
2
3
4
5
6

```
 | 
```
{
 "user_alias" : {
 "alias_name" : (required, string),
 "alias_label" : (required, string)
 }
}

```
 | 

 Field | 
 Data type | 
 Example | 
 Description | 

 alias_name | 
 String | 
 john_doe_123 | 
 A unique identifier for the user, such as an ID from a third-party system. This value must be non-empty and 236 bytes or fewer. | 

 alias_label | 
 String | 
 crm_id | 
 A non-empty custom string that defines the alias type. This value isn’t limited to specific options. You can use any meaningful label, such as email_id, amplitude_id, salesforce_lead_id, or another value that matches your use case. This value must be 236 bytes or fewer. | 

### Example

```

1
2
3
4
5
6
7

```
 | 
```
{
 "user_alias": {
 "alias_name": "john_doe_123",
 "alias_label": "crm_id"
 },
 "external_id": "user_456"
}

```
 | 

In this example, crm_id is a custom label indicating that the alias represents a CRM system identifier.

### Additional example

```

1
2
3
4
5
6

```
 | 
```
{
 "user_alias": {
 "alias_name": "a9f3c102",
 "alias_label": "amplitude_id"
 }
}

```
 | 

In this example, amplitude_id is one possible label value. You can also use labels like email_id or salesforce_lead_id, or another custom label that fits your identifier scheme.

- 

New Stuff!
