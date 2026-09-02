---
url: https://www.braze.com/docs/user_guide/get_started/workspaces
slug: docs__user_guide__get_started__workspaces
title: "Get started: Workspaces"
description: "Everything you do in the Braze platform happens within a workspace. This article describes how they work and what important considerations to keep."
section: user_guide/get_started
fetched: 2026-09-02
evidence: company-own (technical)
---
# Get started: Workspaces

Everything you do in the Braze platform happens within a workspace. Workspaces act as separate silos of data and let you keep different brands or activities separate. Multiple versions of your website or mobile app can send data to the same workspace. We refer to the different sites and apps that are collected within a workspace as “app instances.”

## Understanding workspaces

Workspaces serve two key purposes:

- Unifying user data: When multiple app instances are in one workspace, you can gather and target user data seamlessly across different versions of your app, such as iOS, Android, and web. This makes sure that you always have up-to-date information about each user, regardless of the platform they’re using.
 
- Separating distinct activities: Workspaces also provide a means to keep distinct brands or activities separate. For instance, if you have multiple sub-brands with different user bases, it’s beneficial to create separate workspaces for each.

tip

This approach is particularly useful for companies like mobile gaming firms that can manage individual workspaces for each of their games or eCommerce sites that want separate workspaces for each region they operate in.

## Planning workspaces

You must create separate app instances for each version of your app on each platform. When deciding which app instances to include in a workspace, think of the users you want to target and group them accordingly.

The draw to have multiple app instances under one workspace can be enticing, as it lets you rate limit messaging across your entire app portfolio. However, as a best practice, we suggest only putting different versions of the same (or very similar) apps together under one workspace.

### Shared workspaces

Common examples of when you would want to have multiple app instances in the same workspace:

- When you have multiple, nearly identical apps across different platforms
 
- When you have different major revisions of the app, but want to keep engaging the same users when they upgrade
 
- When you have different versions of the app that the same user could move in or out of (such as free to premium)

#### Impact on segmentation filters

Whichever apps you choose to have in one workspace will have their data aggregated. This will have a notable impact on the following segmentation filters in Braze (this is not an exhaustive list):

- Last Used App
 
- First Used App
 
- Session Count
 
- Money Spent In-App
 
- Push Subscription (This becomes an all-or-none situation—if your users unsubscribe from one app, they are unsubscribed from all apps in the workspace.)
 
- Email Subscription (This becomes an all-or-none situation and can leave you open to compliance issues.)

note

The aggregation of data across app instances in these filters is why we do not recommend housing substantially different apps within the same workspace. It can make targeting tricky!

### Separate workspaces

Other times, you may wish to have multiple, separate workspaces. Common examples of this include:

- Separate workspaces for development and production environments of the same app
 
- Different sub-brands, for example, a mobile game company that offers several games
 
- Different localizations of the same app or website that operate in different countries or targets different languages

### Important considerations

Remember, workspaces act as separate silos of data. All data, whether it is user data or marketing assets, is stored within a workspace. This data cannot be easily shared outside of that workspace.

The following are all key elements that are configured within a workspace:

- App instances
 
- Teams
 
- Company user permissions (but not company users)
 
- Currents connectors
 
- User profiles and the associated user data
 
- Segments, campaigns, and Canvases

#### App instances

You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android, create four app instances within your workspace (free iOS app, free Android app, pro iOS app, and pro Android app). This will give you four API keys to use, one for each app instance.

#### Teams

Teams can be set up across customer base location, language, and custom attributes so that team members and non-team members have different access to messaging features and customer data.

#### Company user permissions

Workspaces have independent access and user permission definitions. User permissions allow you to create granular controls regarding what an individual dashboard user or team has access to within a single workspace.

#### Currents connectors

The Currents tool is a real-time data stream of your engagement events that is the most robust yet granular export out of the Braze platform. Currents connectors are included with certain Braze packages, and you might have initially received one, assuming a single workspace.

When you’re deciding between creating separate or combined workspaces, it’s important to think about the number of Currents connectors you have, as Currents connectors are not shared across workspaces.

For example, if you have separate workspaces for the development and production environments of the same app, activate your Currents connector in the production workspace. To enable Currents in both workspaces, you’ll need to purchase an additional Currents connector.

#### User profiles

All persistent data associated with a user is stored in their user profile. However, user profiles are also a great resource for troubleshooting and testing because you can easily access information about a user’s engagement history, segment membership, device, and operating system.

#### Segments, campaigns, and Canvases

A segment, campaign, or Canvas can’t reference or access data housed within another workspace. Conversely, when multiple apps are in the same workspace, all apps will have their data aggregated. This will have an impact on filters in Braze.

### Overview of each approach

The following table describes the benefits and drawbacks of these two approaches to workspace planning:

- Separate workspaces and user profiles: One workspace has one app instance and one person has one user profile for that app instance.
 
- Shared workspaces and user profiles: One workspace has multiple app instances and one person has one user profile for all of those app instances.

 Overview of each approach

 | 
 Separate workspaces | 
 Shared workspaces | 

 | 
 Benefits | 
 Drawbacks | 
 Benefits | 
 Drawbacks | 

 Targeting | 
 Safest way to keep communications separate. Campaigns are guaranteed to target only specific user profiles. | 
 Unable to send cross-promotional messaging even if you know a user has another user profile in a different workspace. | 
 Can send cross-promotional messaging if you know a user has multiple apps in your workspace.

Can reference user data from across apps. For example, John has X attribute relevant to App 1, and Y attribute relevant to App 2, which can both be referenced in one campaign. | 
 More room for human error—you could accidentally target users across multiple app instances.

To send in-app messages, you must have app-specific custom events so that one campaign doesn't display on another app by accident. For example, app_1_action versus app_2_action. | 

 Custom events and attributes | 
 Custom attributes and events are guaranteed to be specific to an app instance. | 
 Cannot track user behavior across workspaces.

Tip: You can leverage multiple Currents connectors to accomplish this. | 
 Can track user behavior across all app instances in the workspace. | 
 Custom attributes and events would apply to all app instances, which could make it hard to tell what data in a user profile is relevant to what app instance. For example, is "date_of_parking" relevant for App 1 or App 2? To combat this, make sure to use well-structured naming conventions. | 

 Frequency capping | 
 Frequency capping can be defined separately for each app instance (based on workspace). | 
 N/A | 
 N/A | 
 Frequency capping applies to all campaigns, not on a per-app basis, which makes it harder to prevent over-messaging customers. | 

 Subscription status for user profiles | 
 Each user profile's subscription status is unique to each app instance. | 
 N/A | 
 N/A | 
 A user profile's subscription statuses are combined across app instances.

Tip: You could use custom attributes to manage your users' subscriptions instead. | 

 Company user permissions | 
 N/A | 
 Updating user permissions for a dashboard user must be done separately for each workspace the user needs access to. | 
 User permissions can be set once for a dashboard user, and they will have the same permissions for all app instances in the workspace. | 
 N/A | 

 Duplicating content | 
 N/A | 
 Some content, such as segments and Content Card campaigns, can't be copied across workspaces. | 
 Can copy campaigns, Canvases, and landing pages across workspaces. Supported content includes campaigns and Canvases for eligible channels, as well as landing pages, email templates, feature flags, and Content Blocks.

Can duplicate segments, campaigns, Canvases, and landing pages to reuse content from one app instance to another. | 
 N/A | 

 Analytics | 
 Global statistics will be accurate on the Home page. | 
 N/A | 
 N/A | 
 Global statistics will be aggregated for all app instances in the workspace on the Home page. | 

note

For how MAU differs when viewing all apps versus a single app, see Monthly active users.

## Best practices

### Set up a testing workspace

As a best practice, whenever you plan to set up a production workspace (a workspace that will send messages to real users), you should also set up a testing workspace. A testing workspace is a duplicate of your production workspace without any real user data.

This is considered a best practice for several reasons:

- Isolation of changes: It allows you to test new features, configurations, or updates in an isolated environment without affecting your live production environment. This way, if something goes wrong during testing, your production environment remains unaffected.
 
- Accurate testing: It allows for more accurate testing since the data in the testing environment can be controlled and manipulated without worrying about real-world data.
 
- Debugging: It’s easier to debug issues in a testing environment as you can freely manipulate the environment without worrying about impacting the production environment.
 
- Training: New team members can familiarize themselves with the workspace in a safe environment where mistakes won’t have real-world consequences.

tip

The order in which you set up a testing workspace and a production workspace can depend on your specific needs and circumstances. However, it’s generally a good idea to set up a testing workspace first. This allows you to test features, configurations, and updates before they’re implemented in the production workspace. After you’re satisfied with the testing and results, you can then establish your production workspace.

### Add administrators

You should have more than one Braze user with admin permissions for a single workspace. This ensures there are enough people in your organization to manage other users’ permissions.

## Next steps

After you’ve determined your workspace plan, it’s time to create your workspace and add app instances. For steps, check out Create and manage workspaces.

- 

New Stuff!
