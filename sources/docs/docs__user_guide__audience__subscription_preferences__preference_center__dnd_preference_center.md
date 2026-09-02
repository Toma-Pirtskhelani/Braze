---
url: https://www.braze.com/docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
slug: docs__user_guide__audience__subscription_preferences__preference_center__dnd_preference_center
title: "Create an email preference center with drag-and-drop"
description: "This reference page covers how to create an email preference center with the drag-and-drop editor."
section: user_guide/audience
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create an email preference center with drag-and-drop

Using the drag-and-drop editor, you can create and customize a preference center to help manage which users receive certain types of communication. You can have up to 100 preference centers per workspace.

tip

You can also manage subscriptions on a Braze landing page. Add a Manage Subscriptions block so consumers can review and update their existing subscriptions or opt in to new ones, all while you capture their engagement data on the same page. For more information, see Manage Subscriptions block.

You can manage existing drag-and-drop preference centers from Audience > Email Preference Centers:

- To change a preference center’s name or content, open the preference center from the dashboard.
 
- Drag-and-drop preference centers can’t be deleted from the dashboard. To remove one, first remove its Liquid tag from any email campaigns or Canvas steps, then contact Braze Support.
 
- If a removed preference center was used in previously sent messages, it stops working in those delivered emails.

important

To gain access to the drag-and-drop editor, contact your IT administrator to verify that your firewall has *.bz-rndr.com allowlisted.

## Step 1: Create an email preference center

Create a preference center by going to Audience > Email Preference Centers. Here, a list of custom preference centers is displayed. Select Create New to create a new preference center, or select the name of an existing one to make changes.

## Step 2: Name the email preference center

Preference center names can only contain alphanumeric characters, dashes, or underscores. The name you provide determines the syntax of the generated Liquid tag.

This Liquid tag can be included in any outbound email campaigns or Canvas steps and directs users to the preference center.

## Step 3: Add subscription groups to the preference center

Select Launch Editor to begin designing your preference center in the drag-and-drop editor.

### Define available subscription groups

To determine which subscription groups should be shown in the preference center, select the + Add subscription groups button to launch a modal where desired subscription groups can be selected. After selecting, select the Add Subscription Groups button to add them to the preference center.

You can further configure the selected subscription groups by selecting the smart block and adjusting the block properties.

- Adjust the order of subscription groups
 
- Add or remove additional subscription groups
 
- Include descriptions
 
- Add or remove a Subscribe to all checkbox which subscribes the user to all subscription groups shown in this block
 
- Add or remove an Unsubscribe from all checkbox which unsubscribes the user from all subscription groups shown in this block

The Unsubscribe from all button at the bottom of the template is non-removable and globally unsubscribes the user from receiving any email messages.

## Step 4: Customize the preference center using the drag-and-drop editor

### Set common styles

You can set certain styles to be applied across all relevant blocks in your preference center from the Common Styles tab. The styles set in this section are used everywhere in your message except where you override them for a specific block. For an easier design experience, we recommend setting up page-level styles before you customize styles at the block level.

tip

To return to the common styles, select the “X” button on individual block properties. Next, select the message container, message “X” button, or editor background.

## Drag-and-drop preference center components

The drag-and-drop editor uses two key components to make preference center composition quick and easy: rows and blocks. All blocks must be placed in a row.

- rows
 
- blocks

Rows are structural units that define the horizontal composition of a section of the message by using cells.

When a row is selected, you can add or remove the number of columns you need from the Column customization section to put different content elements side by side. You can also slide to adjust the size of existing columns.

As a best practice, format your row and column properties before formatting any blocks inside the rows. You can adjust the spacing and alignment in many places, so starting from the foundation makes it easier to edit as you go.

Blocks represent different types of content you can use in your message. Drag one inside an existing row segment, which auto-adjusts to the cell width.

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see Editor blocks (preference center).

If you’re using the Custom Code block in your preference center, inline frames may not generate in the custom code when delivered to your users.

note

Content Blocks with links cannot be used in the drag-and-drop preference center. Links within Content Blocks are not clickable.

## Step 5: Customize your confirmation page

Next, customize the confirmation page by selecting Confirmation Page. This page is displayed to users after they update their preferences using the preference center. The same styling capabilities from Set common styles and Drag-and-drop preference center components apply to this page.

## Step 6: Preview and launch your preference center

You can preview your preference center by selecting the Preview tab within the editor. The preview shows both the preference center and the confirmation page.

However, testing functionality is disabled. Additionally, test sends of campaigns or Canvas steps that include the preference center Liquid tag do not generate a valid link. This preview does not let you save subscription changes—it only shows how the page looks. To test saving preferences, see Testing preference centers. After editing your preference center, you can close the editor by selecting the Done button.

Select Save as Draft to return to this preference center later, or if you are satisfied, select Launch Preference Center.

When launching the preference center, you’re prompted to confirm the name, as it cannot be edited after launching. After you confirm the name, the preference center launches and is ready for use.

## Use the preference center

important

There are certain browsers, such as the Naver Android and iOS apps, that don’t support the Braze preference center. If you anticipate that some of your users use these browsers, consider providing alternative methods for them to manage their email preferences.

To place a link to the preference center in your emails, copy the Liquid tag of the desired preference center by selecting the Copy Liquid icon.

Add the Liquid tag to the desired place in your email, similar to how unsubscribe URLs are inserted.

## Testing preference centers

Preference center links are generated for each user at send time and are tied to a live campaign or Canvas send. Test sends and editor previews do not support saving subscription changes. This is expected behavior.

### What you’ll see

- Test sends: Preference center Liquid tags may not resolve to a valid link. If the page loads, the Save Preferences button is disabled, and subscription changes are not saved.
 
- Drag-and-drop editor Preview tab: You can preview layout and styling, but you cannot test saving preferences from the editor.

### How to test end-to-end

To verify that preference center links and buttons work before a full launch:

- Create a campaign or Canvas email step that includes your preference center Liquid tag.
 
- Target only your test users or a small internal segment.
 
- Launch the message and open the email from a real inbox (not Send Test).
 
- Select the preference center link, update subscription groups, and select Save Preferences.
 
- Confirm the changes on the user’s profile in the Braze dashboard.

For other test-send limitations, see Send test messages.

### Preview, test send, and live send

 Method | 
 Preview layout | 
 Save subscription changes | 

 Drag-and-drop editor Preview tab | 
 Yes | 
 No | 

 Campaign or Canvas Send Test | 
 Partial (email arrives) | 
 No | 

 Live send to a test user or segment | 
 Yes | 
 Yes | 

 Generate preference center URL API | 
 Yes | 
 Yes | 

## Frequently asked questions

### Why doesn’t my preference center work in a test send?

Preference center links require a live send context. Test sends do not generate valid preference center URLs, and the Save Preferences button is disabled if the page loads. This is expected behavior. To test end-to-end, launch a campaign or Canvas step to a test user or small internal segment. For details, see Testing preference centers.

## Handle errors

If an error occurs when a user selects Save on a preference center, they are presented with the following default error message, which cannot be customized or styled in the editor. However, localization of the error messages is still supported on these pages.

- 

New Stuff!
