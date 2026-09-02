---
url: https://www.braze.com/docs/user_guide/channels/banners/create_a_banner
slug: docs__user_guide__channels__banners__create_a_banner
title: "Create a Banner"
description: "This reference article covers how to create, compose, configure and send Banners using Braze campaigns and Canvases."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create a Banner

Learn how to create Banners when you build campaigns and Canvases in Braze. For more general information, see About Banners.

## Prerequisites

Before you can launch your Banner, your development team must set up placements in your app or website. You can still draft your Banner campaign in the meantime, but you won’t be able to launch the campaign until the placements are configured.

## Create a Banner message

### Step 1: Create placements in Braze

If you haven’t already, you’ll need to create Banner placements in Braze that are used to define the locations in your app or site can display Banners. To create a placement, go to Settings > Banners Placements, then select Create Placement.

Give your placement a name and assign a Placement ID. Be sure you consult other teams before assigning an ID, as it’ll be used throughout the card’s lifecycle and shouldn’t be changed later. For more information, see Placement IDs.

### Step 2: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

- campaign
 
- canvas

- Go to Messaging > Campaigns and select Create Campaign.
 
- Select Banner.
 
- Name your campaign something clear and meaningful.
 
- Add teams and tags as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
 
- Select the placement you previously created to associate it with your campaign.
 
- Add variants as needed. You can choose a different message type and layout for each one. For more information on variants, refer to Multivariate and A/B testing.
 
- Choose a start date and time for your Banner campaign. By default, Banners last indefinitely. You can change this by selecting End Time and specifying an end date and time.

tip

If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then select Copy from Variant from the Add Variant dropdown.

- Create your Canvas using the Canvas composer.
 
- After setting up your Canvas, add a Message step in the Canvas builder. Name your step something clear and meaningful.
 
- Select Banner as your messaging channel.
 
- Select a placement for the Banner.
 
- Set the priority. The Banner priority determines the order in which Banners are displayed if they share the same placement.
 
- Set an expiration for the Banner. This can be after a duration of time after the step is available or at a specific date and time. The maximum expiration duration is 31 days after the step becomes available to the user.

### Step 3: Compose a Banner

Next, choose how you want to start building:

- Drag-and-drop editor: Start with a blank Banner and build visually with blocks and rows.
 
- HTML editor: Start with a blank Banner and work directly in HTML.
 
- Templates: Open the template library and select a design from Braze Templates or Your Templates. Templates open in the drag-and-drop editor for customization.

#### Step 3.1: Style the Banner

- drag-and-drop editor
 
- html editor

You can drag and drop blocks and rows into the canvas area to start building your message. For a reference of Banner editor blocks and links to shared property details, see Editor blocks (Banners).

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

To customize your message’s background properties, border settings, and more, select Styles. If you only want to customize the style for a specific block or row, select it to make changes.

##### Hide rows and blocks by device

To tailor your layout for desktop versus tablet and mobile, select a row or block on the canvas, then use the Hide on toggle in the properties panel to hide it on Desktop or Tablet and smaller devices. A hidden row or block won’t appear for that device type, either when previewing your Banner in the drag-and-drop editor or in the live Banner.

The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling. You can write or paste custom HTML directly into the editor. Liquid personalization tags are fully supported, so you can reference user attributes, custom attributes, catalog items, and more.

tip

Need help building your Banner HTML? Select Ask Operator in the HTML editor and describe the Banner you want. BrazeAI Operator™ generates HTML you can review and insert into the editor. For more information, see Generate messages.

For click and dismissal tracking in your custom HTML, you must call JavaScript bridge methods explicitly. For the full reference, see Custom code and JavaScript bridge for Banners.

note

To target users in different languages within a single Banner campaign, see Multi-language messages.

#### Step 3.2: Define on-click behavior (optional)

- drag-and-drop editor
 
- html editor

When a user clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to log a custom attribute or event, which updates your user’s profile with custom data when they click the Banner. For more granular click tracking, assign a custom identifier to each interactive element using the Identifier for Reporting field in its properties panel.

important

On-click behavior can be overridden if a specific element (such as a button, link, or image, of the Banner) has its own on-click behavior. For example, given the following on-click behaviors:

- A Banner has an on-click behavior that redirects to a website's homepage.
- An image in the Banner has an on-click behavior that redirects to a website's product page.If a user clicks the image, they are redirected to the product page. However, clicking the surrounding area in the Banner redirects them to the homepage.

In the HTML editor, click tracking is not automatic. You must call brazeBridge.logClick() from within your HTML for each clickable element you want to track. For example:

```

1

```
 | 
```
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>

```
 | 

For the full JavaScript bridge reference, see Custom code and JavaScript bridge for Banners.

#### Step 3.3: Configure dismissal behavior (optional)

important

Banner dismissals require the following minimum SDK versions. Older SDK versions do not render Banners with dismissal enabled.

   Swift: 14.1.0+     Web: 6.7.1+     Android: 42.1.0+  Flutter: 20.0.0+  React Native: 22.0.0+  

- drag-and-drop editor
 
- html editor

Select the Banner can be dismissed checkbox in the Dismiss behavior section to allow users to dismiss the Banner. This is useful when you want to promote a limited-time offer to a broad audience but still let uninterested users hide the message.

When dismissal is turned on, you can customize the dismiss button in the Dismiss behavior section:

 Setting | 
 Description | 

 Button size | 
 The size of the dismiss button displayed on the Banner. | 

 Button color | 
 The color of the dismiss button. | 

 ARIA label | 
 The accessible label for the dismiss button, used by screen readers. Defaults to “Close” if left blank. | 

When a user dismisses a Banner, it doesn’t appear again for that user, even if they still qualify for the campaign’s targeting criteria.

In the HTML editor, dismissal is handled in your HTML using brazeBridge.closeMessage(). Pair it with brazeBridge.logClick() to also track the dismiss action as a click event. For example:

```

1

```
 | 
```
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>

```
 | 

When a user dismisses a Banner this way, it doesn’t appear again for that user, even if they still qualify for the campaign’s targeting criteria.

For the full JavaScript bridge reference, see Custom code and JavaScript bridge for Banners.

#### Step 3.4: Add custom properties (optional)

You can add custom properties to a Banner to attach structured metadata, such as strings or JSON objects. These properties don’t affect how the Banner is displayed but can be accessed through the Braze SDK to modify your app’s behavior or appearance. For example, you could:

- Send metadata for your third-party analytics or integrations.
 
- Use metadata such as a timestamp or JSON object to trigger conditional logic.
 
- Control the behavior of a Banner based on included metadata like ratio or format.

Custom properties work the same way in both the drag-and-drop editor and the HTML editor. To add a custom property, select Settings > Properties > Add property.

For each property you’d like to add, fill out the following:

 Field | 
 Description | 
 Example | 

 Property type | 
 The data type for the property. Supported types include string, boolean, number, timestamp, image URL, and JSON object. | 
 String | 

 Property key | 
 The unique identifier for the property. This key is used in the SDK to access the property. | 
 color | 

 Value | 
 The value assigned to the property. Must match the selected property type. | 
 #FF0000 | 

When you’re finished, select Done.

#### Step 3.5: Personalize with Connected Content (optional)

important

Connected Content for Banners is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.

Because Banners render inline during a session refresh, Connected Content in this channel works differently than in other channels:

- Only GET requests are supported.
 
- All placements in a single refresh (up to 10) share a rendering budget of approximately two seconds. If a call is slow, times out, or the budget is exceeded, the Connected Content result for that placement is treated as null. Banners don’t retry.

For best results:

- Keep your endpoints fast and cache responses whenever possible.
 
- Limit the number of unique Connected Content URLs across the placements that render together.
 
- Avoid chaining calls where one Connected Content response determines the URL for the next. Each additional call adds to the shared budget.
 
- Use Liquid guard statements or the default filter to handle null results and avoid blank Banners.

### Step 4: Build the remainder of your campaign or Canvas

- campaign
 
- canvas

#### Set Banner priority (optional)

Banner priority determines the order in which Banners are displayed if they share the same placement. To manually set the priority:

- Select Set exact priority.
 
- Drag and drop the campaigns to order them with the correct priority.
 
- Select Apply Sort.

tip

If you have multiple Banner campaigns using the same placement ID, we recommend using the drag-and-drop priority sorter to define the exact priority.

#### Configure re-eligibility (optional)

By default, users who dismiss a Banner are never re-eligible for that campaign. To let dismissed users see the Banner again, go to the Delivery Controls step and select Allow users to become re-eligible to receive campaign. When enabled, set a cooldown window in minutes, hours, days, or weeks.

The countdown starts from when the user dismisses the Banner. After the window expires, the user is automatically re-eligible—no campaign restart required. Re-eligibility is tracked per user per campaign.

#### Choose your audience

- In Target Audiences, choose segments or filters to narrow your audience. You automatically receive a preview of the approximate segment population. Exact segment membership is calculated before the message is sent.

important

Your message will only be sent to users who already match the conditions you set in the Target Audience step. After that, they still need to meet the trigger you define in the Schedule Delivery step. Think of the target audience as a waiting room—only people already inside can move forward when the next action happens.

- In Assign Conversions, track how often users perform specific actions after receiving a campaign by defining conversion events with up to a 30-day window to count the action as a conversion.

#### Choose conversion events

Braze allows you to track conversion events, how often users perform specific actions, after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion is counted if the user takes the specified action.

If you haven’t done so already, complete the remaining sections of your Canvas component. For details about building the rest of your Canvas, including multivariate testing and Optimize with BrazeAI™, see Build your Canvas.

To control re-eligibility for Canvas Banner steps, use the Canvas re-entry settings. For more information, see Re-eligibility for campaigns and Canvas.

### Step 5: Test your message (optional)

Select Preview to you preview your Banner or send a test message.

Keep in mind, your preview may not be identical to the final render on a user’s device due to differences across hardware.

To send a test message, add either a content test group or one or more individual users as Test Recipients, then select Send Test. You’ll be able to view your test message on the device for up to 5 minutes. You can then select Copy preview link to generate and copy a shareable preview link that shows what the banner will look like for a random user. The link will last for seven days before it needs to be regenerated.

While reviewing your test Banner, verify the following:

- Is your Banner campaign assigned to a placement?
 
- Do the images and media show up and act as expected on your targeted device types and screen sizes?
 
- Do your links and buttons direct the user to where they should go?
 
- Does the Liquid function as expected? Have you accounted for a default attribute value in the event that the Liquid returns no information?
 
- Is your copy clear, concise, and correct?

For more information, see Send test messages.

### Step 6: Review and deploy

After you’ve finished building your campaign or Canvas, review its details, test it, then send it when you’re ready.

- 

New Stuff!
