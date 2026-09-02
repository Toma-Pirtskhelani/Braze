---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups
slug: docs__user_guide__channels__sms_mms_and_rcs__message_setup__subscription_groups
title: "SMS, MMS, and RCS subscription groups"
description: "This reference article covers subscription groups, subscription states, and the subscription group setup process for SMS, MMS, and RCS channels."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# SMS, MMS, and RCS subscription groups

Subscription groups are the foundation for sending SMS, MMS, and RCS messages through Braze. A subscription group is a collection of sending entities—such as RCS-verified senders, SMS short codes, SMS long codes, or SMS alphanumeric sender IDs—used for a specific messaging purpose (for example, transactional versus promotional). For a cross-channel overview of subscription groups, see Subscription groups.

note

You can add up to 450 subscription groups per workspace.

## Subscription group states

There are two subscription states for SMS and RCS users: subscribed and unsubscribed. A user’s subscription state resides at the subscription group level and is not shared across subscription groups, meaning a user can be subscribed to a transactional subscription group but unsubscribed to a promotional one. For brands, this separation of states ensures that they can continue to send relevant SMS and RCS messages to their users.

 State | 
 Definition | 

 Subscribed | 
 User is subscribed to receive SMS and RCS from a specific subscription group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an SMS or RCS subscription group to receive SMS, RCS, or both. When double opt-in is enabled, users must confirm their opt-in intent before their subscription status updates to Subscribed. | 

 Unsubscribed | 
 User has explicitly opted out of messaging from your SMS and RCS subscription group and the sending phone numbers inside the subscription group. They can unsubscribe by texting an opt-out keyword response or you can unsubscribe users through the Braze subscription API. Users unsubscribed from an SMS and RCS subscription group no longer receive any SMS or RCS from sending phone numbers that belong to the subscription group. | 

### Set a user’s state

When a phone number is updated on a user profile, the new phone number inherits the subscription group status of the user. If the phone number is updated to a number that already exists in Braze, the subscription status of that existing phone number is inherited.

For example, if User A has a phone number that is subscribed to several subscription groups and that phone number then gets added to User B, User B is subscribed to the same subscription groups. To prevent a user from inheriting the existing subscriptions, you can reset the subscription groups of the old number through the Braze REST API whenever a user changes their number. If multiple users share this phone number, they are all unsubscribed.

To set a user’s subscription group state, use one of the following methods:

- REST API: Use the /subscription/status/set endpoint to programmatically set user profiles with the Braze REST API. Each request can include between 1 and 25 subscription groups.
 
- SDK Integration: Users can be added to or removed from an email or SMS and RCS subscription group using addToSubscriptionGroup and removeFromSubscriptionGroup for Android, iOS, or Web. SDK methods don’t replace regulatory opt-in or opt-out flows handled by keywords and the REST API.
 
- Phone Number Capture IAM Form: User phone numbers can be collected through the phone number capture template in the in-app message drag-and-drop editor.
 
- Automatically handled upon user opt-in/opt-out: By users texting a default opt-in or opt-out keyword, Braze automatically sets and updates users’ subscription state.
 
- User import: Users can be added into email or SMS and RCS subscription groups through Import Users. When updating subscription group status, you must have these two columns in your CSV: subscription_group_id and subscription_state. Refer to User import for more information.
 
- Braze dashboard: Select User Search from the sidebar, open a user’s profile, and update SMS or RCS subscription groups under Contact Settings on the Engagement tab.
 
- Cloud Data Ingestion (CDI): Include subscription_group_id and subscription_state in synced rows. See Cloud Data Ingestion table setup.
 
- User Update step: Update subscription status in a Canvas with a User Update step. See Update a user’s state in a Canvas for timing considerations.

#### Update a user’s state in a Canvas

When updating a user’s subscription group status as part of a Canvas flow, use a User Update step instead of a webhook. The User Update step waits for processing to complete before advancing the user to the next step, so subsequent messaging steps use the updated subscription status.

If you use a webhook to update subscription groups, the user advances as soon as the webhook is sent—not when the subscription change finishes processing. This can create a race condition where a follow-up SMS step executes before the user is subscribed, causing the message to fail for a portion of users. If you must use a webhook, add a Delay step of at least 1 minute before the next messaging step.

## How Braze handles orphaned subscription states

An orphaned subscription state is a subscription state stored for a phone number or email address that isn’t associated with any user profile. For SMS, email, WhatsApp, and LINE, Braze handles orphaned subscription states as follows:

- If a user is deleted and is the only user associated with a given phone number or email address, the subscription state for that phone number or email address is deleted immediately.
 
- If you call /subscription/status/set or /v2/subscription/status/set with a phone number or email address that is not currently associated with any user profile, Braze stores that subscription state for up to 30 days, after which it is automatically deleted.

- If use_double_opt_in_logic is set to true and no user profile is associated with the provided phone number, the subscription state is not updated; a user must exist to enter the double opt-in workflow.

- If a new user profile is created with a phone number or email address that has an orphaned subscription state stored for it, that user inherits the stored subscription state but only within the 30-day window. This 30-day grace period is intentional and exists to handle race conditions when creating a user and setting its channel identifier’s subscription state happen in separate API calls. An example of this race condition is when a /subscription/status/set request is processed for a phone number before the /users/track request creating the corresponding user profile is processed.

### Check a user’s group

To check a user’s subscription group, use one of the following methods:

- User Profile: Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. When inside a user profile, under the Engagement tab, you can view a user’s SMS and RCS subscription groups.
 
- Rest API: Individual user profiles subscription group can be viewed by the List user’s subscription groups endpoint or List user’s subscription group status endpoint by using the Braze REST API.

## Send messages with a subscription group

To launch an SMS or RCS campaign through Braze, select a subscription group from the SMS/MMS/RCS Variants dropdown. After it’s selected, an audience filter is added to your campaign or Canvas automatically, ensuring that only users subscribed to the selected subscription group are in the target audience.

Before users can receive messages from a campaign or Canvas, they must be subscribed to the selected subscription group. If sends fail for otherwise valid users, confirm they are subscribed using one of the methods in Set a user’s state. For double opt-in requirements, see Subscription group states.

important

In adherence with international telecommunication compliance and guidelines, Braze never sends SMS or RCS to users that have not subscribed to the selected subscription group.

## SMS subscription group best practices

Design separate SMS subscription groups for each messaging purpose (for example, transactional versus marketing) and for each workspace. When you operate in multiple countries, consider separate groups by region to support local compliance rules—for example, Brazil’s restrictions on promotional send windows.

## Enable subscription groups

To enable subscription groups for SMS, MMS, or RCS, refer to the following:

- sms
 
- mms
 
- rcs

During your SMS onboarding process, a Braze onboarding manager sets up subscription groups for your dashboard account. They work with you to determine how many subscription groups you need and add the appropriate sending phone numbers to your subscription groups. Timelines for setting up a subscription group depend on the type of phone numbers you’re adding. For example, short code applications can take anywhere between 8-12 weeks, while long codes can be set up within a day. If you have questions about your Braze dashboard setup, contact your Braze representative for support.

In order to send an MMS message, at least one number within your subscription group has to be enabled to send MMS. This is indicated by a tag located next to the subscription group.

An RCS-verified sender must be present within your subscription group before you can send an RCS message.

There are two ways to add an RCS-verified sender:

- Add it to an existing subscription group
 
- Create a new RCS subscription group
The choice largely depends on the RCS use cases you are interested in.

Depending on your integration, Braze can add RCS-verified senders to your existing SMS subscription groups or set up new subscription groups for you. In either case, your customer success manager guides you through a seamless and efficient SMS traffic upgrade.

## Handle natural language opt-outs in the Agent Console

For comprehensive subscription management, you can capture opt-out intent that falls outside of standard or custom keywords (such as “Please don’t text me”). By creating an AI agent, you can use sentiment analysis to help identify and act on these requests automatically.

### Setup

- In the Agent Console, create an “SMS Sentiment Analysis Agent”.

tip

Use Operator to assist with the initial agent configuration.

- Create an action-based Canvas triggered by Send an SMS inbound message, within the Other keyword category.
 
- Add the Agent step to the Canvas to identify opt-out intent.
 
- Add a subsequent SMS Message step to confirm the request: “It looks like you’re trying to unsubscribe from SMS, so we are going to unsubscribe you. If this is a mistake, text START to opt back in.”
 
- Add a User Update step to change the user’s status in the specific SMS subscription group to “Unsubscribed.”

note

Using the Agent Console consumes Message or Action Credits.

## Migrate SMS traffic to RCS

If you have separate SMS and RCS subscription groups, you can migrate users from SMS to RCS using a one-step Canvas.

Braze recommends that you test sending RCS to smaller volumes of users initially and migrate more users to the RCS subscription group over time. For example, if you have 1,000,000 users subscribed to an SMS subscription group, this could look like first migrating all users to the new subscription group and then segmenting on a smaller audience of 50,000 to 100,000 (5-10%) to test the RCS messages.

### Step 1: Create a Canvas and fill out the Entry Schedule

Create a Canvas and name it something easily identifiable (such as “SMS-RCS Subscription Group User Transfer”). Then, schedule the campaign whenever is convenient for you.

### Step 2: Define your audience

Define your audience using one of the following methods. Next, go to the Send Settings step and select Users who are subscribed or opted-in.

 Method | 
 Description | 

 Create a segment | 
 Build a segment that includes all users in a subscription group or a subset using segmentation filters (such as a random 5-10%). Segments update before each send to reflect your current user base. | 

 Apply campaign or Canvas filters | 
 Refine the audience in the Target Audience step of your campaign or Canvas. Adjust targeting options without leaving the page for added flexibility. | 

### Step 3: Configure a User Update step

Add a User Update Step to your Canvas. In the step, open the Advanced JSON Editor and input the following (for the unique user identifier field, we recommend using the braze_id field):

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
 "attributes": [
 {
 "braze_id": "{{${braze_id}}}",
 "subscription_groups": [
 {
 "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
 "subscription_state": "subscribed",
 "use_double_opt_in_logic": true
 }
 ]
 }
 ]
}

```
 | 

important

When using use_double_opt_in_logic, a user profile must already exist for the subscription state to be updated. If no user profile is associated with the provided identifier, the subscription state isn’t updated.

### Step 4: Test the Canvas

We highly recommend testing your Canvas to confirm it works as expected before sending it to your broader audience.

### Step 5: Launch your Canvas

After you have successfully tested your Canvas, go ahead and launch it for your subset of users!

To confirm that your users were successfully migrated, we recommend checking a few individual user profiles that were updated. In the Engagement tab, look for Contact Settings and scroll to view the subscription groups the user is subscribed to. The RCS subscription group toggle should now be on.

For RCS sender and subscription group setup, also refer to Set up RCS.

## Best practices

### Designate separate subscription groups

- Messaging type: Create distinct subscription groups for each type of messaging, such as Transactional and Marketing.
 
- Workspace: Create distinct subscription groups for each workspace to maintain clarity and organization.

Consider the following example with four subscription groups across two workspaces:

- Production workspace

- Marketing - PROD for SMS
 
- Transactional - PROD for SMS

- Development Workspace (for testing)

- Marketing - DEV for SMS
 
- Transactional - DEV for SMS

### Use clear naming conventions

Choose descriptive and clear subscription group names so that the correct group is selected when creating SMS campaigns.

### Separate groups by country

SMS regulations vary by country. We suggest separating SMS subscription groups by country. This helps you meet compliance standards in all regions where you send messages.

For each subscription group, you can also configure a country allowlist under Geographic Permissions so SMS, MMS, and RCS are only sent to approved regions. For more information, see Geographic permissions.

For example, in Brazil, sending marketing messages outside the hours of 9 am and 9 pm local time is prohibited, and the country spans three time zones. To comply with these regulations, you might set up separate groups for sending messages to Brazil and the United States. This prevents users in Brazil from receiving marketing messages during prohibited hours.

- 

New Stuff!
