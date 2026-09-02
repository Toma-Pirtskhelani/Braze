---
url: https://www.braze.com/docs/user_guide/administer/global/user_management/manage_company_users
slug: docs__user_guide__administer__global__user_management__manage_company_users
title: "Manage company users"
description: "This page covers managing your company users, such as adding and deleting users, setting user permissions, creating Teams, and managing company settings."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Manage company users

Learn how to manage users in your company account, including adding, suspending, and deleting users.

## Adding company users

You must have administrator permissions to add users to your Braze account.

To add a new user:

- Go to Settings > Company Settings > User Management > Company Users.
 
- Select + Add New User.
 
- Enter their information as prompted, including their email, department, and user role.
 
- For users that aren’t administrators, select the company-level and workspace-level permissions you want this user to have.

### Email address requirements

Every email address used in an instance must be unique. This means that if you try to add an email address that’s already associated with a user who had or still has access to a company workspace in that instance, you’ll see an error message.

If your team uses Gmail and you’re experiencing issues adding an email address, you can create an alias by adding a plus sign (+) like “+1” or “+test” to the email address. For example, [email protected] can have an alias of [email protected]. Emails to [email protected] are still delivered to [email protected], but the alias is recognized as a unique email address.

To use one account across multiple companies without aliases, see Use multi-company developers. If you use SSO, review Considerations for Single Sign-On (SSO) before registering with multiple email addresses.

### Can I change my Braze account’s email address?

For security reasons, users cannot change the email address associated with their Braze account. If a user wants to update their email address, an administrator should create a new account for them with their preferred email address.

## Assigning user access and responsibilities

You can use Teams, permission sets, and user roles to manage company user access and responsibilities within Braze. Each feature encompasses a different collection of permissions and access-controls.

### Key differences

At a high level, each feature has a different scope:

- Permission sets control what company users can do across all workspaces.
 
- Roles control what company users can do in specific workspaces.
 
- Teams control the audiences that company users can reach with their messages.

 Feature | 
 What you can do | 
 Scope of access | 

 Permission sets | 
 Bundle permissions related to specific subject areas or actions (such as for “Developers” and “Marketers”), then apply them to company users who need the same permissions across different workspaces. | 
 Company wide | 

 Roles | 
 Bundle individual custom permissions and workspace-access controls (such as “Marketer - Fashion Brands”, where the user has certain permissions associated with their role as a marketer and is limited to the “Fashion Brands” workspaces). Then assign a role to company users to directly grant them the associated permissions and workspace access. 

Users with this level of access are typically managers in more tightly controlled setups with many brands or regional workspaces in one dashboard. | 
 Specific workspaces | 

 Teams | 
 Limit company user access to resources based on the audience (such as customer base location, language, and custom attributes). 

Users with this level of access typically are responsible for a specific scope within the brand that they’re working on, such as building language-specific content for a multilingual brand. | 
 Specific dashboard | 

## Suspending company users

Suspending a user puts their account into an inactive state, where the user can no longer log in, but the data associated with their account is preserved. Only administrators can suspend or unsuspend company users. Note that suspended users may still receive notifications from Braze.

To suspend a user, go to Settings > Company Settings > User Management > Company Users, find their username, and select Suspend.

Administrators can also suspend a user by selecting their name from the list and selecting Suspend user in the footer.

## Deleting company users

To delete a user, go to Settings > Company Settings > User Management > Company Users, find the user’s name, and select Delete user.

Only administrators can delete company users, and company users cannot delete their own accounts. An administrator cannot delete their own dashboard account; another administrator must delete it for them.

After a user is deleted, Braze does not keep any of the following account data:

- Any attributes that the user had
 
- Email address
 
- Phone number
 
- External user ID
 
- Gender
 
- Country
 
- Language
 
- Other similar data

Braze keeps the following account data:

- Custom attributes or test data associated with their account
 
- Campaigns or Canvases they created (but the user’s name won’t appear in them, such as appearing in the Last edited by column)

### Impact of deleting a dashboard user

Deleting a dashboard user does not significantly affect the assets they created within the dashboard, such as campaigns, segments, and Canvases. However, the Created By field for these assets displays a “null” value instead of the email address of the deleted user.

If a new dashboard user is subsequently created with the same email address as the deleted user, Braze does not re-associate the assets created by the deleted user with the new user. The new dashboard user starts with a clean slate and is not credited as the creator of any existing assets in the dashboard.

## Troubleshooting

### “Unable to perform action” when adding a user

If adding a dashboard user fails with an “Unable to perform action” (or similar) error:

- Remove leading or trailing spaces and hidden characters from the email address.
 
- Confirm the address is a valid email format for your organization. Some special characters are rejected.
 
- The same email cannot be used for two dashboard users in the same cluster. If the address is already registered in another workspace on that cluster, use a distinct address or an alias such as [email protected].

### “Email is already taken” when trying to add a user

If you try to add a new user and receive an error saying the email is already taken, but can’t find them in your user list, that user most likely exists within a different instance of the same Braze dashboard cluster.

To create this new user, you can do either of the following:

- Delete the user from the other instance before you can create them in the new one, or
 
- Create the user with a different email string (such as [email protected]) or another email alias.

If you don’t receive the message activation in your inbox when using [email protected], confirm with your IT team that you can accept messages from that kind of email address. Some administrators filter messages sent to email addresses with a +.

## Next steps

After adding users, manage their access:

- Permissions to configure what each user can do in the dashboard.
 
- Teams to organize users into groups with shared access to specific dashboard objects.

- 

New Stuff!
