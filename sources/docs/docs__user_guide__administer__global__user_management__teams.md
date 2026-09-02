---
url: https://www.braze.com/docs/user_guide/administer/global/user_management/teams
slug: docs__user_guide__administer__global__user_management__teams
title: "Teams"
description: "This reference article covers how to use Braze Teams in the dashboard. Here, you can learn how to create Teams, assign roles, and assign tags..."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Teams

As a Braze admin, you can group your company users into Teams with varying user roles and permissions. This allows you to have multiple, unrelated groups of company users working together in one workspace by separating the types of content that can be edited.

Teams can be set up across customer base location, language, and custom attributes so that Team members and non-Team members have different access to messaging features and customer data. Team filters and tags can be assigned across various engagement tools. There is no limit on how many teams you can create in your workspace.

Teams are not available on all Braze contracts. To access this feature, contact your Braze account manager or contact us for a consultation.

## How do Teams differ from permission sets and roles?

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

## Create Teams

Go to Settings > Internal Teams and select Add Team.

Enter the Team Name. If desired, use the Define Team (Optional) field to select a custom attribute, location, or language to further define what user data the Team has access to. For example, a possible use case is to perform testing with Teams by creating a development Team that only has access to test users, identified by a custom attribute. Another use case is to restrict communication with users based on the product.

If a Team is defined by a custom attribute, language, or country, you can then use the Team to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. For more, see Assigning Team tags.

## Assign users to Teams

Braze administrators and limited users with the company-level permission “Can Manage Company Settings” can assign Team-level permissions to a company user with limited access. When assigned to a Team, company users are limited to only read or write data available to their particular Teams, such as user language, location, or custom attribute, as defined when the Team was created.

### Limit company user permissions without deleting a user

To stop a company user from signing in while preserving their account, suspend the user instead. Suspending puts the account in an inactive state where the user can’t log in.

If the user should remain able to sign in with limited capabilities, go to Settings > Company Users, select the user, and edit their permissions. Remove workspace-level permissions for campaigns, Canvases, segments, and user data, and leave only minimal access—for example, “View Media Library Assets”. For more information, see Edit a user’s permissions.

Team permissions work on top of workspace permissions. If you assign the user to a Team, grant only the minimum team-level permissions they need, and don’t grant permissions for campaigns, Canvases, segments, or user profiles. They remain in the workspace and can sign in, but they can’t perform most messaging or audience actions.

To assign a user to a Team, navigate to Settings > Company Users and select a user you’d like to add to your Team.

Then perform the following steps:

- In the Workspace-level permissions section, add the user to the appropriate workspace if they aren’t already included.

- Select + Add team-level permissions, then select the Team you’d like to add this user to.
 
- Assign specific permissions from the Team permissions section.

### Available Team-level permissions

The following are all available permissions you can assign at the Team level. Any permissions not listed here are only granted on the workspace level, and these permissions will appear as “–” in the Teams permissions column.

- View Campaigns
 
- Edit Campaigns
 
- Archive Campaigns
 
- Launch Campaigns
 
- Approve Campaigns
 
- View Canvases
 
- Edit Canvases
 
- Archive Canvases
 
- Launch Canvases
 
- Approve Canvases
 
- View Content Blocks
 
- Edit Content Blocks
 
- Archive Content Blocks
 
- Launch Content Blocks
 
- View Segments
 
- Edit Segments
 
- Archive Segments
 
- View IAM Templates
 
- Edit IAM Templates
 
- Archive IAM Templates
 
- View Email Templates
 
- Edit Email Templates
 
- Archive Email Templates
 
- View Webhook Templates
 
- Edit Webhook Templates
 
- Archive Webhook Templates
 
- View Email Link Templates
 
- Edit Email Link Templates
 
- View Media Library Assets
 
- Edit Media Library Assets
 
- Delete Media Library Assets
 
- Export User Data
 
- View User Profiles (PII Redacted)
 
- View PII
 
- Edit Dashboard Users
 
- Edit Canvas Templates
 
- View Canvas Templates
 
- Archive Canvas Templates
 
- View Dashboard Reports
 
- Edit Dashboard Reports
 
- Delete Dashboard Reports

To see descriptions of what each user permission includes and how to use them, check out our User Permissions section.

## Assign Team tags

You can assign a Team to Canvases, campaigns, Content Cards, segments, email templates, webhook templates, Content Blocks, and media library assets with the Add Team filter.

### Automatic Team assignment

For users with Team-level permissions only (and no workspace-level edit permission), Braze can assign Teams automatically during object creation:

 User’s Team membership | 
 Behavior | 

 Exactly one Team | 
 Braze auto-assigns that Team when the user creates a new campaign, Canvas, Content Block, or email template. | 

 More than one Team | 
 The user must choose a Team before saving. | 

When a Team is assigned to a campaign or Canvas, that Team’s required segmentation filters appear in the audience builder as a read-only Team filter group.

For Canvases, Braze only checks whether users match the team filter criteria when they enter the Canvas. After a user enters a Canvas, they continue to receive messages from all Canvas steps even if their attributes change and they no longer match the team filter criteria. Team filters don’t behave like delivery validations, which re-evaluate users at each Message step send.

- Based on the definitions applied when the Team was created, when a Team filter is assigned, that engagement tool’s audience is restricted to user profiles that match the definition.
 
- Based on assigned permissions, Team members are only allowed to access dashboard engagement tools that have their Team filter set. If they have limited or no workspace permissions, they must add a Team filter to certain objects before they can save or launch them. Team members can also filter Canvases, campaigns, Content Cards, and segments by Team to identify content relevant to them.
 
- Users with Team-level permissions only don’t see Created by or Last edited by filters on the segments, campaigns, or Canvas pages. Braze hides these filters so Team-only users can’t browse all Braze users from those dropdowns.

### Use cases

Consider the following two scenarios for a marketer in Braze named Michelle. Michelle is a member of a Team called “Development”. She has access to all of the Team-level permissions for the Development Team.

- scenario 1 - only team permissions
 
- scenario 2 - team permissions and workspace permissions

In this scenario, Michelle is a limited user who has no workspace-level permissions. Her permissions look something like this:

Based on Michelle’s assigned permissions, whenever she creates a campaign, she can only assign the “Development” Team to that campaign. She can’t launch the campaign unless the Team is assigned, and she can’t view or access any other Team tags.

In this scenario, Michelle is still a member of the Development Team, but she also has an additional workspace-level permission.

Because Michelle has the workspace-level permission of “Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers”, she can view and assign other Team filters to the campaign she creates.

Similar to the first scenario, Michelle must add the Development Team tag to the campaign before she can launch it.

## Test with Teams

One possible use case for Teams is to create a Teams-based approval system for testing and launching content in a production environment.

To do so, create a “Development” Team that only has access to test users. You can limit a Team to only access test users if your test users are identifiable by a custom attribute. Then, add the custom attribute as a definition when creating or editing the Team (see the preceding section Creating Teams). Your approvers should have access to all users.

The general process would be as follows:

- The Development Team creates a campaign and adds the “Development” Team tag.
 
- The Development Team launches the campaign to test users.
 
- The Approver Team validates the local campaign design, promotes, and launches. To launch, the Approver Team changes the Team tag from “Development” to “[All Teams]” and relaunches the campaign.

For changes to active campaigns:

- The Development Team clones the running campaign, adds the “Development” Team tag, and saves.
 
- The Development Team makes edits and shares with the Approver Team.
 
- The Approver Team removes the “Development” Team tag, pauses the previous campaign, and launches the new campaign.

## Archive an existing Team

You can archive Teams from the Internal Teams page.

Select one or many Teams to archive. If the Team is not associated with any object within Braze, the Team is archived immediately. If the Team is associated with an object, you are presented with an option to remove the Team after the archive process or replace the Team.

Braze admins can unarchive a Team by selecting the archived Team and selecting Unarchive.

- 

New Stuff!
