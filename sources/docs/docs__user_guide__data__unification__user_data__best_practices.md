---
url: https://www.braze.com/docs/user_guide/data/unification/user_data/best_practices
slug: docs__user_guide__data__unification__user_data__best_practices
title: "Collection best practices"
description: "The following article helps clarify different methods and best practices for collecting new and existing user data."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Collection best practices

Knowing when and how to collect user data for known and unknown users can be challenging when envisioning the user profile lifecycle of your customers. This article helps clarify different methods and best practices for collecting new and existing user data by walking you through a use case.

The following example is an email collection use case, but the logic applies to many different data collection scenarios. In this example, we assume you have already integrated a sign-up form or way to collect user information.

After a user provides information for you to log, we recommend you verify if the data already exists in your database and, when necessary, create a user alias profile or update the existing user profile.

If an unknown user were to view your site and then, at a later date, create an account or identify themselves through email sign-up, profile merging must be handled carefully. Based on the method in which you merge, alias-only user information or anonymous data may be overwritten.

## Capturing user data through a web form

### Step 1: Check if the user exists

When a user enters content through a web form, check if a user with that email already exists within your database. You can do this in one of these ways:

- Check internal database (recommended): If you have an external record or database containing the provided user information that exists outside of Braze, reference this at the time of email submission or account creation to confirm the information hasn’t already been captured.
 
- /users/track endpoint: Use email as an identifier, and a new user profile will be created if the email address doesn’t exist yet.
 
- /subscription/status/get endpoint: If you collect email through a custom form and then set subscription group membership through the REST API, call this endpoint first. If no matching profile exists, create or subscribe the user with the /subscription/status/set endpoint. Otherwise, update the existing profile instead of creating a duplicate.

### Step 2: Log or update user

- If a user exists:

- Don’t create a new profile.
 
- Log a custom attribute (for example, newsletter_subscribed: true) on the user’s profile to indicate that the user has submitted their email through a newsletter subscription. If multiple Braze user profiles exist with the same email address, all profiles will be exported.

- If a user doesn’t exist:

- Create an alias-only profile through the /users/track endpoint. This endpoint will accept a user_alias object and create an alias-only profile when update_existing_only is set to false. Set the user’s email as the user alias to reference that user in the future (as the user won’t have an external_id).

## Capturing user emails through an email capture form

Use an email capture form to prompt users to submit their email address, which will be added to their user profile. For more information on how to set up this form, check out Email capture form.

If you use a custom form and set subscription group membership through the REST API, check whether a profile already exists before creating a user. See Step 1: Check if the user exists.

## Identifying alias-only users

When identifying users upon account creation, alias-only users can be identified and assigned an external ID through the /users/identify endpoint by merging the alias-only user with the known profile.

To check if a user is alias-only, check if the user exists within your database.

- If an external record exists, you can call the /users/identify/ endpoint.
 
- If the /users/export/id endpoint returns an external_id, you can call the /users/identify/ endpoint.
 
- If the endpoint returns nothing, a /users/identify/ call shouldn’t be made.

## Capturing user data when alias-only user information is already present

When a user creates an account or identifies themselves through email sign-up, you can merge the profiles. For a list of fields that can be merged, refer to Merge updates behavior.

### Merging duplicate user profiles

As your user data grows, you can merge duplicate user profiles from the Braze dashboard. These duplicate profiles must be found using the same search query. For more information on how to duplicate user profiles, check out Merge duplicate users.

You can also use the Merge users endpoint to merge one user profile into another.

note

After user profiles are merged, this action cannot be undone.

## Additional resources

- Check out our article on the Braze user profile lifecycle for additional context.

- View our documentation on setting user IDs and calling the changeUser() method for Android, iOS, and Web.

- 

New Stuff!
