---
url: https://www.braze.com/docs/partners/ecommerce/shopify/discount_codes
slug: docs__partners__ecommerce__shopify__discount_codes
title: "Send unique discount codes through Shopify"
description: "This reference article covers a community-submitted use case of using Braze promotion codes with the Shopify Bulk Discount Code Bot to send unique discount codes..."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Send unique discount codes through Shopify

This community-submitted use case shows how to use Braze promotion codes with the Shopify Bulk Discount Code Bot to generate unique discount codes for your campaigns and Canvases. Unique discount codes help avoid the exploitation of generic promotion codes.

important

This is a community-submitted integration and isn’t directly supported by Braze. The Bulk Discount Code Bot is directly supported by Shopify. Only Braze promotion codes are supported by Braze.

## Requirements

 Requirement | 
 Description | 

 Set up a Shopify store | 
 Confirm you’ve already set up a Shopify store with Braze. | 

 Install the Bulk Discount Code Bot app | 
 Download the Bulk Discount Code Bot app in the Shopify app store. | 

## Generating unique discount codes

### Step 1: Configure your discount codes

Use the Bulk Discount Code Bot to configure your discount codes based on the number of codes to generate, code length, discount value, and more.

### Step 2: Export your codes

Find your discount set in the Bulk Discount Code Bot’s search bar, then select Export Codes > Download Codes to download a CSV file to your Downloads folder.

In the CSV file, delete row 1 to remove the column header “Promo”. This prevents “Promo” from becoming a discount code in Braze.

### Step 3: Add your discount codes to Braze

In Braze, go to Data Settings > Promotion Codes > Create Promotion Code List and configure your discount codes list. Make sure you match the expiration date that was configured by the Bulk Discounts Code Bot.

Then, upload your CSV file and select Save List.

### Step 4: Add your discount codes to a Braze campaign or Canvas step

If you want to use your unique discount codes in a single-send campaign, or you don’t mind users receiving multiple unique codes across different campaigns or Canvas steps, copy the code’s Liquid snippet from the promotion codes list you saved.

Paste the Liquid snippet into a campaign or Canvas step.

If you want users to receive a single unique discount code no matter how many times the discount code is referenced in campaigns or Canvases, create a User Update step directly before the first Message step that assigns the discount code to a custom attribute, like “Promo Code”.

tip

You can also create a custom attribute by going to Data Settings > Custom Attributes.

In the User Update step, do the following for each field:

- Attribute Name: Select Promo Code.
 
- Action: Select Update.
 
- Key Value: Paste the Liquid code snippet.

Now, you can add the custom attribute {{custom_attribute.${Promo Code}}} to any message, and the discount code will be templated in.

## Discount code behavior

Multichannel campaign or Canvas step

When a discount code snippet is used in a multichannel campaign or Canvas step, users always receive a unique code. If a user is eligible to receive a code through more than one channel, they’ll receive the same code through each channel. In other words, an eligible user would only receive one code across all the messages sent by that campaign or Canvas step.

Different Canvas steps or separate campaigns

When a discount code is referenced by multiple steps in the same Canvas or by separate campaigns, an eligible user will receive multiple unique promotion codes (one code for each Canvas step or campaign).

- 

New Stuff!
