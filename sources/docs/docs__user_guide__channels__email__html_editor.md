---
url: https://www.braze.com/docs/user_guide/channels/email/html_editor
slug: docs__user_guide__channels__email__html_editor
title: "Create an email with custom HTML"
description: "This reference article covers how to create an email using the Braze platform. Included are best practices on how to compose your messages, preview your..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create an email with custom HTML

Email messages are great for delivering content to your users on their terms. They are also excellent tools to re-engage users who may have even uninstalled your app. Sending customized and tailored email messages will enhance your users’ experience, and help your users get the most value out of your app.

To see examples of email campaigns, check out our Case Studies.

tip

If this is your first time creating an email campaign, we highly recommend checking out these Braze Learning courses:

- Email Opt-Ins and Permissions
 
- Project: Build a basic email marketing program

## Step 1: Choose where to build your message

Use campaigns for single, simple messaging. Use Canvases for multi-step user journeys.

- campaign
 
- canvas

- Go to Messaging > Campaigns and select Create Campaign.
 
- Select Email, or, for campaigns targeting multiple channels, select Multichannel.
 
- Name your campaign something clear and meaningful.
 
- Add teams and tags as needed.

- Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by particular tags.

- Add and name as many variants as you need for your campaign. For more on this topic, refer to Multivariate and A/B testing.

tip

If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose Copy from Variant from the Add Variant dropdown.

- Create your Canvas using the Canvas composer.
 
- After you’ve set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
 
- Choose a step schedule and specify a delay as needed.
 
- Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
 
- Choose your advancement behavior.
 
- Choose any other messaging channels which you would like to pair with your message.

tip

If you plan to build custom HTML and need backgrounds to stay consistent in the Gmail mobile app with device dark mode on, see Gmail mobile app and Dark Mode background colors.

important

To gain access to the HTML editor, contact your IT administrator to verify that your firewall has *.bz-rndr.com allowlisted.

## Step 2: Select your editing experience

Braze offers two editing experiences when creating an email campaign: our drag-and-drop editor and our standard HTML editor. Choose the appropriate tile for the editing experience you’d prefer.

Then, you can either select an existing email template, upload a template from a file (HTML editor only), or use a blank template.

If you use the HTML editor and need background colors to stay consistent in the Gmail mobile app when the device is in dark mode, see Gmail mobile app and Dark Mode background colors.

tip

We recommend selecting one editing experience per email campaign. For example, choose either the HTML Classic or Block editor in a single email campaign rather than switching between editors.

## Step 3: Compose your email

After you’ve selected your template, you’ll see an overview of your email where you can directly jump to the fullscreen editor to draft your email, change your sending information, and view warnings about deliverability or law compliance. You can switch among HTML, classic, plaintext, and AMP tabs while you compose.

Braze automatically updates the plaintext version from the HTML version until it detects an edit to the plaintext. After Braze detects an edit, it stops updating the plaintext because it assumes you made intentional changes. To restore automatic sync, go to Plaintext and select Regenerate from HTML (visible only when plaintext isn’t synchronizing).

tip

To add motion in an email with an accurate preview, use GIFs instead of elements that require JavaScript, as most inboxes don’t support JavaScript.

important

Braze automatically removes HTML event handlers referenced as attributes. This modifies the HTML, so re-check the email after you finish. Learn more about HTML handlers.

tip

Need help creating awesome copy? Try using the AI copywriting assistant. Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

Need help crafting right-to-left messages for languages like Arabic and Hebrew? Refer to Creating right-to-left messages for best practices.

### Gmail mobile app and dark mode

The Gmail mobile app (Android and iOS) can invert background colors when the device is in dark mode. That can break layouts where the email background should match an image edge or a specific brand color.

To avoid this, in the table cell that needs a stable background, use a single-color CSS linear-gradient instead of background-color. Gmail is less likely to invert that treatment than a flat background color.

For example, to keep a white background on a cell, use this:

```

1

```
 | 
```
<td style="background-image: linear-gradient(#ffffff, #ffffff);">

```
 | 

Replace #ffffff with your intended color.

note

This approach does not apply reliably to <table aria-label="Gmail mobile app and dark mode #gmail-dark-mode"> elements alone, so set the gradient on the cell instead of only on the table.
Gmail mobile app and dark mode

For more information about gradient syntax, see CSS gradients on W3Schools.

### Step 3.1: Add your sending information

After you finish designing and building your email message, add your sending information in Sending Settings.

- Under Sending Info, select an email as the From Display Name + Address. You can also customize this by selecting Customize From Display Name + Address.
 
- Select an email as the Reply-To Address. You can also customize this by selecting Customize Reply-To Address.
 
- Next, select an email as the BCC Address to make your email visible to this address.
 
- Add a subject line to your email. Optionally, you can also add a preheader. To add whitespace after the preheader, select the Add whitespace after preheader checkbox.

tip

You can use Liquid in the From Display Name + Address and Reply-To Address fields to dynamically template these based on custom attributes. This allows you to send from different brands, regions, or departments using a single email campaign or Canvas step.

A preview in the right-hand panel will populate with the sending information you’ve added. This information can also be updated by going to Settings > Email Preferences > Sending Configuration.

#### Advanced

Under Sending Settings > Advanced, turn on inline CSS for the widest client support. If messages clip or images stretch to row height, try turning inline CSS off temporarily. Some templates behave better without inlining.

You can also add personalization for email headers and email extras to send additional data back to other email service providers.

##### Email attachments

You can also add email attachments by the following methods:

- Upload a file: Drag and drop or browse to upload a file directly from your computer to the email. Braze validates the file type and size (up to 2 MB by default) before uploading, then these files are uploaded to the media library. Files that are larger than 2 MB limit cannot be uploaded.
 
- Use the media library: Browse and select from assets already stored in the media library. PDFs, Word documents, Excel files, and PowerPoint presentations are all supported.
 
- Add from URL: Enter a URL pointing to the file and provide a display filename. Because Braze cannot probe arbitrary URLs for size during email composition, the file size is enforced at send time.

note

Liquid is not supported in the Add from URL field.

Refer to Email guidelines for specific best practices to consider.

##### Email headers

To add email headers, select Add New Header. Email headers contain information about the email being sent. These key-value pairs typically include sender, recipient, authentication protocol, and routing information. Braze automatically adds the RFC-required header information for emails to reach inbox providers.

Braze allows you the flexibility to add additional email headers as needed for advanced use cases. There are a few reserved fields that the Braze platform will overwrite during sending.

Avoid using the following keys:

 Email headers

 Reserved Fields | 
 | 
 | 

 BCC | 
 dkim-signature | 
 Reply-To | 

 CC | 
 From | 
 Subject | 

 Content-Transfer-Encoding | 
 MIME-Version | 
 To | 

 Content-Type | 
 Received | 
 x-sg-eid | 

 DKIM-Signature | 
 received | 
 x-sg-id | 

##### Adding email extras

Email extras allows you to send additional data back to other email service providers. This is only applicable for advanced use cases, so you should only use email extras if your company already has this set up.

To add email extras, go to the Sending Info and select Add New Extra.

warning

The total key-value pairs added should not exceed 1 KB. Otherwise, the messages will be aborted.

Email extra values are not published to Currents or Snowflake. If you’re looking to send additional metadata or dynamic values to Currents or Snowflake, use message_extras instead.

### Step 3.2: Preview and test your message

After you finish composing your email, test it before sending. From the bottom of the overview screen, select Preview and Test.

Here, you can preview how your email will appear in a customer’s inbox. With Preview as User selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

Then, you can Copy preview link to generate and copy a shareable preview link that shows what the email will look like for a random user. For more information, see Shareable preview.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message will appear in different contexts.

tip

Curious about what your email looks like for dark mode users? Select the Dark Mode Preview toggle located in the Preview and Test section (drag-and-drop editor only). If you use the HTML editor, you can still address Gmail mobile dark mode rendering with Gmail mobile app and Dark Mode.

When you’re ready for a final check, select Test Send and send a test message to yourself or a tester group to confirm the email displays properly across devices and clients.

If you see any issues with your email, or want to make any changes, select Edit Email to return to the editor.

tip

Email clients that support preview text always pull in enough characters to fill all available preview text space. However, this can leave you in situations where the preview text is incomplete or unoptimized.

To avoid this, you can create white space after your desired preview text so that email clients don’t pull other distracting text or characters into the envelope content. In the Sending Settings section, you can select the Add whitespace after preheader checkbox to automatically add whitespace. 

Alternatively, if you need more control, you can manually add a chain of zero-width non-joiners (‌&zwnj;) and non-breaking spaces (&nbsp;) after the preview text that you want displayed. 

When added to the end of your preview text in the preheader section, the following piece of code for the HTML editor will add the white space you’re looking for:

```

1

```
 | 
```
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>

```
 | 

For the drag-and-drop editor, add only the zero-width non-joiners (‌&zwnj;) without the <div> formatting directly in the preheader in the Sending Settings section.

note

In the Apple Mail app, image links in HTML email must use https:// URLs to be clickable. Use secure links for any image wrapped in an anchor tag when you expect clicks from Apple Mail recipients.

### Step 3.3: Check for email errors

Before send, the editor flags common issues:

- From display name and header not set together
 
- Invalid From or reply-to addresses
 
- Duplicate header keys
 
- Liquid syntax errors
 
- Content Blocks that include a full <!DOCTYPE html>
 
- Email body is over 400 KB

- Aim for less than 102 KB to avoid clipping.

- Blank body or subject
 
- Missing unsubscribe link
 
- From domain not allowlisted (sends heavily throttled)

## Step 4: Build the remainder of your campaign or Canvas

- campaign
 
- canvas

Next, build the remainder of your campaign. See the following sections for details on how to use Braze tools to build your email campaign.

### Choose delivery schedule or trigger

Deliver emails based on a scheduled time, an action, or an API trigger. For more, refer to Scheduling your campaign.

note

For API-triggered campaigns, when the trigger action is set to Interact With Campaign, selecting a Receive option as the interaction will cause your new campaign to trigger as soon as Braze marks the selected campaign as sent, even if that message bounces or fails to be delivered.

You can also set the campaign’s duration, specify Quiet hours, and set frequency capping rules.

### Choose users to target

Next, target users by choosing segments or filters. Braze shows a live preview of the segment population, including how many users are reachable through email. Exact segment membership is calculated just before send.

important

Your message will only be sent to users who already match the conditions you set in the Target Audience step. After that, they still need to meet the trigger you define in the Schedule Delivery step. Think of the target audience as a waiting room—only people already inside can move forward when the next action happens.

You can also choose to only send your campaign to users who have a specific subscription status, such as those who are subscribed and opted in to email.

Optionally, you can also limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

note

When creating a new email campaign, the Control Group defaults to 20% and can be adjusted or removed as needed for your campaign.

#### Multichannel campaigns with email and push

For multichannel campaigns targeting both email and push channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in statuses:

- User A is subscribed to email and is push enabled. This user doesn’t receive the email but will receive the push.
 
- User B is opted-in to email but is not push enabled. This user will receive the email but doesn’t receive the push.
 
- User C is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under Audience Summary, select to send this campaign to “opted-in users only”. This option will check that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

important

With this configuration, don’t include any filters in the Target Audiences step that limit the audience to a single channel (for example, Foreground Push Enabled = True or Email Subscription = Opted-In).

### Choose conversion events

Braze allows you to track how often users perform specific actions, conversion events, after receiving a campaign. You can specify any of the following actions as a conversion event:

- Opens app
 
- Makes purchase (This can be a generic purchase or a specific item)
 
- Performs specific custom event
 
- Opens email

You can allow up to a 30-day window during which Braze counts a conversion if the user takes the specified action. While Braze tracks opens and clicks automatically, you may set the conversion event to an open or click to use Optimize with BrazeAI™.

If you haven’t done so already, complete the remaining sections of your Canvas components. For details about building the rest of your Canvas, including multivariate testing and Optimize with BrazeAI™, see Build your Canvas.

## Step 5: Review and deploy

The final section summarizes the campaign you designed. Confirm all relevant details and select Launch Campaign.

To learn how you can access the results of your email campaigns, check out Email reporting.

- 

New Stuff!
