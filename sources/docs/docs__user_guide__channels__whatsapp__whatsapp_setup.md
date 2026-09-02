---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup
slug: docs__user_guide__channels__whatsapp__whatsapp_setup
title: "WhatsApp setup"
description: "This article covers how to set up the Braze WhatsApp channel, including prerequisites and suggested next steps."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# WhatsApp setup

WhatsApp Business messaging is a popular peer-to-peer messaging platform used across the world offering conversation-based messaging for businesses.

## Prerequisites

Acknowledge the following before proceeding with integration:

- Opt-in policy: WhatsApp requires businesses to have customers opt-in to messaging.
 
- WhatsApp content rules: WhatsApp has several content rules that need to be followed.
 
- Compliance: Comply with all applicable Braze and Meta documentation and any applicable Meta policies.
 
- 24-hour conversation limits: After a business sends an initial templated message or a user sends a message, a 24-hour window will occur where the two parties can message back and forth.
 
- Initiating conversation: Users can initiate a conversation at any point. A business can only initiate a conversation through an approved message template.

 Requirement | 
 Description | 

 Meta Business Manager account | 
 A Meta Business account is required to leverage this messaging channel. | 

 WhatsApp Business account | 
 A WhatsApp Business account is required to leverage this messaging channel. | 

 WhatsApp phone number | 
 You must acquire a phone number that meets WhatsApp’s requirements for Cloud API or On-Premises API for use of the messaging channel. | 

## Integration

### Step 1: Connect WhatsApp Messenger to Braze

In Braze, go to Partner Integrations > Technology Partners and search for WhatsApp.

On the WhatsApp partner page, select Begin Integration.

In the open window, select Next until the Begin Integration button appears. Select the button to begin the integration process.

### Step 2: WhatsApp setup

Next, you will be prompted by the Braze setup workflow. For a step-by-step walkthrough, refer to WhatsApp embedded signup.

Within this flow, you will:

- Create or select your Meta and WhatsApp Business accounts. Make sure to review the WhatsApp display name guidelines. 

It is likely that you already have at least one existing Meta Business account at your company. If that is the case, select the one you would like your WhatsApp Business account to live within. User permissions and business verification for WhatsApp will be controlled centrally in your Meta Business account.

- Create your WhatsApp Business profile.
 
- Verify your WhatsApp Business number.

After the setup is complete, a dedicated WhatsApp subscription group is created for your users.

### Step 3: Create WhatsApp templates

Only approved WhatsApp message templates can be used to initiate conversations with customers. WhatsApp templates can be built in the Meta Business Manager. For a list of the WhatsApp messaging features supported by Braze, check out Supported WhatsApp features.

- Navigate to the template manager

In the Meta Business Manager, under Account Tools, select Message Templates.
Next, select Create Templates.

- Message settings

In the new message template composer, select the category of your message, name your template, and choose the languages you want to support. You can delete or add more languages later.

 The available message template categories include the following:

- Marketing: Send promotional offers, product announcements, and more to increase awareness and engagement
 
- Utility: Send account updates, order updates, alerts, and more to share important information
 
- Authentication: Send codes that allow your customers to access their accounts

- Edit template

Next, create your message template. 

You can provide a text or media header, the text body, a message footer, and buttons. Note that video and document headers are not currently available, and headers must be of either text or image type. Any media you add serves as an example for the review process and is not included in the template message. Media needs to be added in Braze. A preview of your message will display in a panel. 

While Meta does not support Liquid, you can template in variables that can be later replaced in Braze for Liquid variables. Select the + Add variable button to do so.

Once you have completed your template, press Submit.

#### Template approval time

You can check the approval status of your message template in either the Message Template page in the Meta Business Manager, or when creating a campaign or Canvas in Braze. Additionally, you can be notified by email by the WhatsApp team depending on your notification permissions.

note

Approved templates can be used in as many campaigns and Canvases as you like. They can also be sent to as many opt-in users as you like. This is true unless the quality of the template decreases.

### Step 4: Create a WhatsApp campaign

Once WhatsApp templates have been approved, you can move over to the dashboard to build out a WhatsApp Canvas or campaign.

note

After your WhatsApp Business Account is created, Meta will determine your starting messaging limit. To learn more, check out throughput.

## Next steps

After completing the integration, we recommend completing the two following Meta processes:

- Business Verification

- You may already have business verification if you’ve used an existing Meta Business Manager.

- Official Business Account

We also recommend reading about user phone numbers and adding any users who will need access to create message templates at your organization.

### WhatsApp Cloud API Local Storage

Braze supports WhatsApp’s Cloud API Local Storage. To have this enabled, contact your Braze customer support manager.

- 

New Stuff!
