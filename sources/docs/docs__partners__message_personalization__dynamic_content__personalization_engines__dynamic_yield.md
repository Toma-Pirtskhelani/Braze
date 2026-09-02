---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalization_engines/dynamic_yield
slug: docs__partners__message_personalization__dynamic_content__personalization_engines__dynamic_yield
title: "Dynamic Yield"
description: "This reference article outlines the partnership between Braze and Dynamic Yield. This partnership allows you to use Dynamic Yield's recommendation and segmentation engine to create..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Dynamic Yield

Dynamic Yield, a Mastercard company, helps businesses across industries deliver digital customer experiences that are personalized, optimized, and synchronized. With Dynamic Yield’s Experience OS, marketers, product managers, developers, and digital teams can algorithmically match content, products, and offers to each customer for the acceleration of revenue and customer loyalty.

This integration is maintained by Dynamic Yield.

## About the integration

The Braze and Dynamic Yield partnership allows you to use Dynamic Yield’s recommendation and segmentation engine to create Experience Blocks that can be embedded into Braze messages. Experience blocks can be made of:

- Recommendations blocks: Set algorithms and filtering to source users’ personalized content that propagates when the email is opened.
 
- Dynamic Content Blocks: Target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened.

## Prerequisites

 Requirement | 
 Description | 

 Dynamic Yield account | 
 A Dynamic Yield account is required to take advantage of this partnership. | 

## Integration

### Step 1: Create an Experience Block

To create an Experience Block in Dynamic Yield, navigate to Email > Experience Emails > Create New.

Next, select Create Experience Block to design a Dynamic Content or Recommendations block to embed inside a Braze email template.

### Step 2: Draft your messaging

The following image shows an email from scratch in the builder.

- Enter a campaign name, note, and labels for the campaign in the heading area.

- Insert an Experience Block. These blocks include:

- Recommendations: A widget offering users fully-personalized recommendations.
 
- Dynamic Content: Target different promotions and messages to different audiences.

- Update settings:

- Use the URL parameters to track clicks within your analytics software (optional). Add parameters to the default displays as needed.
 
- Select an attribute window, either seven days (default) or one day.

- Save and exit. You can return to edit all elements of your email at any time before the code is generated. After the code is generated, you can edit anything that does not affect the code.

### Configure a Recommendations block

The recommendations block enables you to set algorithms and filtering to source users’ personalized content that propagates when the email is opened.

- Drag a Recommendations block from the editing pane into the body of your email.

- Select your desired algorithm (popularity, user affinity, similarity, and more). Depending on the algorithm selected, additional options are displayed:

- If your recommendation is based on popularity, you can shuffle the results to avoid serving the same recommendation from different emails the viewer opens.
 
- Other algorithms, such as similarity, rely on context to serve recommendations requiring that you select items to include. These items can be added in the builder or add a merge tag to the embed code to make it dynamic, for example, to add similar items into shipping confirmation emails. 

- You can exclude products the user has already purchased to avoid recommending these products.

- You can add a custom filer rule to pin specific products to slots, or include and exclude products by product properties. For example, do not show products that code less than $5 or only products from the shorts category.

- Lastly, configure the recommendation block design. To do this, select an item template, set the number of items to display, and in how many rows.

### Configure a Dynamic Content Block

Use Dynamic Content to target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened.

- Drag a Dynamic Content Block from the editing pane into the body of your email.

- Select a template for the first variation. You can now define design and content variables. Save the variation when complete. 

- Set the audience in the Dynamic Content pane.

- Add another variation to target another specific audience or all users. Repeat as needed.

- Set the priorities for your variations using the up and down arrows. 

- Priorities determine which variation is served when a user is eligible for more than one experience.

### Step 3: Integrate your email with Braze

This integration allows you to add personalized recommendation widgets and dynamic content powered by Dynamic Yield into your Braze email campaigns. Embedding these campaigns into Braze campaigns is done with a simple embed code that you paste into the Braze email editor.

- Click the ESP Integration icon on the Experience Email list page.

- Enter the relevant token from Braze that inserts the user’s CUID and Email ID.

When satisfied with your email, the next step is to generate the code to embed in Braze.

- In Experience Emails, click Generate Code.

- Next, click Copy to Clipboard.

- Paste the code into your Braze email campaign, and then continue to design, test, and publish your email campaign.

- 

New Stuff!
