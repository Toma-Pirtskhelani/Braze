---
url: https://www.braze.com/docs/user_guide/channels/line/line_setup
slug: docs__user_guide__channels__line__line_setup
title: "LINE setup"
description: "This article covers how to set up the Braze LINE channel, including prerequisites and suggested next steps."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# LINE setup

This article covers how to set up the LINE channel in Braze, including how to set up users, reconcile user IDs, and create LINE test users in Braze.

## Prerequisites

You’ll need the following to integrate LINE with Braze:

- LINE business account
 
- Premium or verified account status (necessary for syncing existing followers)

- View LINE’s account guidelines

- LINE developers account
 
- LINE messaging API channel

Sending LINE messages from Braze draws from your account’s Message or Action Credits.

note

Setting native_line_id: You can set native_line_id by sending user updates to Braze (for example, with the /users/track endpoint, CSV import, or Cloud Data Ingestion). If your app’s SDK doesn’t have a dedicated field for native_line_id, send it in server-side user updates using one of these methods.

## Types of LINE accounts

 Account type | 
 Description | 

 Unverified account | 
 An unreviewed account that can be obtained by anyone (individual or corporate). This account is represented with a gray badge and won’t appear in search results within the LINE app. | 

 Verified account | 
 An account that has passed the LINE Yahoo screening. This account is represented with a blue badge and will appear in search results within the LINE app.

This account is only available for accounts based in Japan, Taiwan, Thailand, and Indonesia. | 

 Premium account | 
 An account that has passed the LINE Yahoo screening. This account is represented with a green badge and will appear in search results within the LINE app. This account type is automatically granted during the screening at LINE’s discretion. | 

### Required account type

To sync followers into Braze, your LINE account needs to be verified or premium. When you create an account, its default status will be unverified. You’ll need to request account verification.

### Applying for a verified LINE account

important

Verified accounts are only available for accounts based in Japan, Taiwan, Thailand, and Indonesia.

- On the LINE Official Account page, select Settings.
 
- Under Information Disclosure Verification Status, select Request Account Verification.
 
- Enter the required information.
 
- Wait for a notification with the review results.

## Integrating LINE

To set up consistent user updates, bring over existing users’ LINE IDs, and sync them all to LINE’s subscription states:

- Import or update existing known users
 
- Integrate the LINE channel
 
- Reconcile user IDs
 
- Change user update methods
 
- (Optional) Merge user profiles

note

You can only have one LINE account in a single workspace. If you have multiple LINE accounts, we recommend using each one in a different workspace.

## Step 1: Import or update existing LINE users

This step is necessary if you have an existing and identified LINE user, as Braze will later automatically pull their subscription state and update the correct user profile. If you haven’t previously reconciled users with their LINE ID, skip this step.

You can import or update users using any of the methods that Braze supports, including the /users/track endpoint, CSV import, or Cloud Data Ingestion.

Regardless of the method you use, update the native_line_id to provide the user’s LINE ID. To learn more the native_line_id, see User setup.

note

Don’t specify the subscription group state—it’s ignored. LINE is the source of truth for user subscription status, which syncs to Braze through the subscription sync tool or event updates.

## Step 2: Integrate LINE channel

After the integration process completes, Braze automatically pulls that channel’s LINE followers into Braze. For any LINE IDs that are already associated with a Braze user profile, each profile is updated with the “subscribed” status, and any LINE IDs that remain generate anonymous users. Additionally, new followers of your LINE channel have unidentified user profiles created when they follow the channel.

### Step 2.1: Edit webhook settings

- In LINE, go the Messaging API tab and edit your Webhook settings:

- Set the Webhook URL to https://anna.braze.com/line/events.

- Braze will automatically change this to a different URL when integrating, based on your dashboard cluster.

- Turn on Use webhook and Webhook redelivery. 

- Take note of the following information in the Providers tab:

 Information type | 
 Location | 

 Provider ID | 
 Select your provider and then go to *Settings > Basic information | 

 Channel ID | 
 Select your provider and then go to Channels > your channel > Basic settings | 

 Channel secret | 
 Select your provider and then go to Channels > your channel > Basic settings. | 

 Channel access token | 
 Select your provider and then go to Channels > your channel > Messaging API. If there isn’t a channel access token, select Issue. | 

note

You can update or rotate the channel secret and channel access token for an already integrated LINE channel by going to Partner Integrations > Technology Partners > LINE and selecting your integration.

- Go to your Settings page > Response settings and do the following:

- Turn off Greeting message. This can be handled in Braze by triggering on follow.
 
- Turn off Auto-response messages. All triggered messaging should be through Braze. This won’t prevent you from sending directly from the LINE console.
 
- Turn on Webhooks.

### Step 2.2: Generate LINE subscription groups in Braze

Braze creates a subscription group for each LINE channel you integrate. For how LINE subscription groups work, see LINE subscription groups.

note

You can add up to 450 subscription groups per workspace.

- Go to the Braze Technology Partners page for LINE and input the information you noted from your LINE Providers tab:

- Provider ID
 
- Channel ID
 
- Channel secret
 
- Channel access token

If you want to add IP whitelisting in your LINE account, add all of the IP addresses listed for your cluster in IP allowlisting to your allowlist.

important

During integration, be sure to check that your channel secret is correct. If it’s incorrect, there may be inconsistencies in the subscription status.

- After connecting, Braze will automatically generate a Braze subscription group for each LINE integration that’s successfully added to your workspace. 

 Any changes to your followers list (such as new followers or unfollowers) will be automatically pushed into Braze.

## Step 3: Reconcile user IDs

Combine your users’ LINE IDs with their existing Braze user profiles by following the steps in User ID reconciliation.

## Step 4: Change your user update methods

Assuming you already have a method to provide user updates to Braze, you’ll need to update that to include the new field native_line_id so that subsequent user updates sent to Braze will include that field.

Unidentified user profiles with a native_line_id may exist in Braze that were created as part of the subscription status sync process, or when a new follower followed your channel.

When a LINE user is identified in your application through user reconciliation or other means, you can target a potential unidentified user profile in Braze using the /users/identify endpoint. Every unidentified user profile with a native_line_id also has a user alias line_id that can be used to target the user profile to identify.

Here is an example payload to /users/identify that targets an unidentified user profile by the user alias line_id:

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
{
 "aliases_to_identify": [
 {
 "external_id": "known_external_id_from_your_application",
 "user_alias": {
 "alias_name": "U89f4a626548ccd48482f529a482f138b",
 "alias_label": "line_id"
 }
 }
 ]
}

```
 | 

If no existing user profile exists for your provided external_id, it will be added to the unidentified user profile, making it identified. If a user profile does exist for the external_id, all attributes that are exclusively on the unidentified user profile will be copied to the known user profile, including native_line_id and the user’s subscription status.

You can update LINE users that are known in your application through the /users/track endpoint by passing their external identifiers and native_line_id. If an unidentified user profile already exists for a user and the same native_line_id is added to a different user profile through /users/track, it will inherit all the subscription states of the unidentified user profile. However, duplicate user profiles will exist with the same native_line_id. Any subsequent subscription updates from event updates will update all profiles accordingly.

note

LINE subscription states are tracked by native_line_id, not external_id. For example, if User B’s user profile is created with the same native_line_id as User A, but not the same external_id, User B inherits User A’s LINE subscription status.

Here is an example payload to /users/track that updates a user profile by the external user ID to add a native_line_id:

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

```
 | 
```
{
 "attributes": [
 {
 "external_id": "known_external_id_from_your_application",
 "native_line_id": "U89f4a626548ccd48482f529a482f138b",
 "other": "attribute"
 }
 ]
}

```
 | 

## Step 5: Merge profiles (optional)

As described earlier in this section, there’s a possibility for multiple user profiles to exist with the same native_line_id. If your update methods create duplicate user profiles, you can merge unidentified user profiles to identified user profiles with the /user/merge endpoint.

Here’s an example payload to /users/merge that targets an unidentified user profile by user alias line_id:

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

```
 | 
```
{
 "merge_updates": [
 {
 "identifier_to_merge": {
 "user_alias": {
 "alias_name": "U89f4a626548ccd48482f529a482f138b",
 "alias_label": "line_id"
 }
 },
 "identifier_to_keep": {
 "external_id": "known_external_id_from_your_application"
 }
 }
 ]
}

```
 | 

tip

To learn more about managing duplicate users in Braze, see Duplicate Users.

## User setup

LINE is the source of truth for user subscription states. Even if you have the LINE ID for a user (native_line_id), if that user hasn’t followed the LINE channel you’re sending from, LINE won’t deliver messages to the user.

To help manage this, Braze offers tooling and logic that supports a well-integrated user base, including subscription syncing and event updates for LINE follows and unfollows.

### Subscription syncing and event logic

For how the subscription sync tool and follow and unfollow event updates keep LINE subscription status aligned with Braze, see Subscription status.

## Re-integrate a LINE channel in another workspace

To use a LINE channel in a different Braze workspace:

- In the original workspace, archive the subscription group for that channel.
 
- In the target workspace, integrate the channel using Step 2: Integrate LINE channel.

Confirm you have the Manage Subscription Groups permission in both workspaces. Without permissions in both workspaces, the integration fails with an error indicating the channel is already connected.

For how archiving affects subscription groups, refer to LINE subscription groups.

## Use cases

These are use cases of how users can be updated after you follow the setup steps.

### Existing Braze user profile already follows LINE channel

- The Braze user profile is updated with a native_line_id attribute. Its default subscription status is unsubscribed.
 
- The subscription sync tool is run, finds that the user is following the LINE channel, and then updates the user profile with the subscription status subscribed.
 
- If any subscription status changes occur (such as the user blocks, unfriends, or refollows the channel), Braze receives the update from LINE and updates the user profile with the native_line_id accordingly.

### Existing user profile has blocked, unfriended, or unfollowed LINE channel

- The Braze user profile is updated with a native_line_id attribute. Its default subscription status is unsubscribed.
 
- The subscription sync tool doesn’t find that the user is following the LINE channel and the user’s subscription status remains as unsubscribed.
 
- If the user later follows the channel, Braze receives the update from LINE and updates the user profile with the subscription status subscribed.

### User profile creation occurs after LINE follow

- The channel gets a new LINE follower.
 
- Braze creates an anonymous user profile with the native_line_id attribute set to be the follower’s LINE ID, and a user alias of line_id set to be the follower’s LINE ID. The profile has a subscription status of subscribed.
 
- The user is identified as having the LINE ID through user reconciliation.

- The anonymous user profile can become identified using the /users/identify endpoint. Subsequent updates (through the /users/track endpoint, CSV import, or Cloud Data Ingestion) to this user profile can target the user by this known external_id.

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
{
 "aliases_to_identify": [
 {
 "external_id": "known_external_id_from_your_application",
 "user_alias": {
 "alias_name": "U89f4a626548ccd48482f529a482f138b",
 "alias_label": "line_id"
 }
 }
 ]
}

```
 | 

- A new user profile can be created (through the /users/track endpoint, CSV import, or Cloud Data Ingestion) by setting the native_line_id. This new profile will inherit the subscription status state of the existing anonymous user profile. Note that this will result in multiple profiles sharing the same native_line_id. These can be merged at any time using the /users/merge endpoint in the process outlined in Step 5.

### User profile creation occurs before LINE follow

- You acquire a new user and send the information to Braze. A new user profile is created (profile 1).
 
- The user follows your LINE account.
 
- Braze receives a follow event and creates an anonymous user profile (profile 2).
 
- The user is identified as having the LINE ID through user reconciliation.
 
- You update profile 1 to set the native_line_id attribute. This profile inherits the subscription status state of profile 2.

- Now there are two user profiles with the same native_line_id. These can be merged at any time using the /users/merge endpoint in the process outlined in Step 5.

## User ID reconciliation

LINE IDs are automatically received by Braze when a user follows your channel, or when you use the one-time “sync followers” workflow. LINE IDs are also specific to the channel that users follow, so it’s unlikely that users can provide their LINE IDs.

There are two ways to combine a LINE ID with an existing Braze user profile:

- LINE login
 
- User account linking

### LINE Login

This method uses social media logins for reconciliation. When a user logs into your app, they’re given the option to use LINE Login to create a user account or log in.

note

To acquire the correct LINE ID for each user, set up LINE Login under the same provider as your Braze-integrated LINE official account or channel.

- 
 
Go to the LINE Developer Console and request permission to obtain the email addresses of users who log into your app through LINE Login.

- 
 
Follow the appropriate steps provided by LINE to implement LINE Login:

- Web app directions
 
- Native app directions

Make sure to include email in the scope set up for verification requests.

- 
 
Use the Verify ID token call to acquire the user’s email.

- 
 
Save the user’s LINE ID (native_line_id) to the user’s profile with a matching email in your database, or create a new user profile with the user’s email and LINE ID.

- 
 
Send the new or updated user information to Braze using the /user/track endpoint, CSV import, or Cloud Data Ingestion.

#### Workflows

##### Existing follower uses LINE Login

Scenario: An anonymous user was created during initial subscriber sync or after integration through a “follow” event.

- The user logs into your app using LINE Login.
 
- LINE provides you the user’s email.
 
- You send Braze the updated user (the existing user profile with that email to add the LINE ID) or you update the anonymous user with the email.

##### New follower uses LINE Login

Scenario: No user profile exists in Braze with the user’s LINE ID.

- The user logs into your app using LINE Login.
 
- LINE provides you with the user’s email.
 
- You either:

- Update an existing user profile with that email to also have the user’s LINE ID.
 
- Create a new user profile with the email and LINE ID.

- When the user follows your LINE Official Account, Braze receives a follow event and updates the user’s subscription status to subscribed.

### User account linking

This method allows users to link their LINE account to your app’s user account. You can then use Liquid in Braze, such as {{line_id}}, to create a personalized URL for the user that passes the user’s LINE ID back to your website or app, which can then be associated with a known user.

- Create an action-based Canvas that is based on a subscription state change and triggers when a user subscribes to your LINE channel.

- Create a message incentivizing users to log into your website or app, passing the user’s LINE ID as a query parameter (through Liquid), such as:

```

1

```
 | 
```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id=

```
 | 

- Create a follow-up message that delivers the coupon code.
 
- (Optional) Create an action-based campaign or Canvas that triggers when the LINE user is identified to send the user their coupon code. 

#### How it works

After the user logs in, a change is made on your website or app so that the user ID is sent back to Braze to associate it with the LINE ID that was passed as part of the URL, with example code such as:

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

```
 | 
```
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
 post(
 "https://rest.iad-03.braze.com /users/identify",
 {
 "aliases_to_identify": [
 {
 "external_id": user.getUserId(),
 "user_alias": {
 "alias_name": lineUserId,
 "alias_label": "line_id"
 }
 }
 ]
 }
 )
 braze.logCustomEvent("identified_line_user_for_promotion");
}

```
 | 

#### Workflows

##### Existing user follows your LINE channel

Scenario: An existing user in Braze follows your channel on LINE.

- LINE sends Braze a follow event.
 
- Braze creates an anonymous user profile with the LINE ID, line_id user alias, and LINE subscription group status of subscribed.
 
- The user receives a LINE message with a link to your website and app and logs in. Their user profile is now known.
 
- The anonymous user profile that was created is identified and is merged through the /users/identify endpoint onto the user’s known user profile. The known user profile now contains the LINE ID and has a subscription status of subscribed.
 
- (Optional) The user receives a LINE message with the coupon code and Braze logs the send to the Braze user profile.

## Creating LINE test users in Braze

You can test your LINE channel before setting up user reconciliation by creating a “Who am I” Canvas or campaign.

- 
 
Set up a Canvas that returns a user’s Braze user ID on a specific trigger word. 

Example trigger 

Example message

- 
 
In Braze, you can use the Braze ID to search for specific users and modify them as needed.

important

Make sure the Canvas doesn’t have global control or control groups preventing sends.

- 

New Stuff!
