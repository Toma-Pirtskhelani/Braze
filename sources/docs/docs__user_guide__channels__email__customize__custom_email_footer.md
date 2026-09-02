---
url: https://www.braze.com/docs/user_guide/channels/email/customize/custom_email_footer
slug: docs__user_guide__channels__email__customize__custom_email_footer
title: "Custom email footer"
description: "This article describes how to set up a workspace-wide custom email footer."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Custom email footer

You can set a workspace-wide custom email footer, which you can template into every email using the {{${email_footer}}} Liquid attribute.

By using custom email footers, you no longer have to create a new footer for every email template or email campaign you use. All new and existing email campaigns reflect changes you make to your custom footer. Remember that compliance with the CAN-SPAM Act of 2003 requires you to include a physical address for your company and an unsubscribe link in your emails.

warning

It is your responsibility to make sure that your custom footer meets the aforementioned requirements.

## Create your custom footer

To create or edit your custom footer, do the following:

- Go to Settings > Email Preferences > Subscription Pages and Footers.
 
- Go to the Custom footer section and turn on custom footers.
 
- Select Edit then edit your footer in the Compose section.
 
- Select Preview to preview how your email footer will appear in a customer’s inbox. You can optionally select Copy preview link to generate and copy a shareable preview link that shows what the email will look like for a random user. For more information, see Shareable preview.
 
- Send a test message.

The default footer uses the {{${set_user_to_unsubscribed_url}}} attribute and our physical mailing address. If you’re using this default, be sure to select <other> for the Protocol.

important

To comply with CAN-SPAM regulations, your custom footer must include an unsubscribe link. You can use this Liquid attribute {{${set_user_to_unsubscribed_url}}} or your own custom unsubscribe URL. You won’t be able to save a custom footer without an unsubscribe link.

## Footers without unsubscribe links

Be very careful when using a template with the custom footer {{${email_footer}}} but without the {{${set_user_to_unsubscribed_url}}} unsubscribe link tag. A warning appears, but it’s your choice to send an email with or without an unsubscribe link.

Here’s a warning in the email composer:

Here’s a warning in the campaign composer:

### Adding a custom unsubscribe link

To add a custom unsubscribe link, you can change the unsubscribe link in the custom footer from {{${set_user_to_unsubscribed_url}}} to a link to your own website with a query parameter that includes the user ID. An example is:

https://www.braze.com/unsubscribe?user_id={{${user_id}}}

Next, call the /email/status endpoint to update the user’s subscription status. For more details, see our documentation on changing email subscription status.

Then, save this new link. The default Braze unsubscribe tag (${set_user_to_unsubscribed_url}) must be in the footer. This means you need to include the default link by “hiding” it by either placing the tag in a comment or in a hidden <div> tag.

## Best practices

We suggest the following best practices when creating and using custom footers.

### Personalizing with attributes

When creating a custom footer, Braze suggests using attributes for personalization. The full set of default and custom attributes are available, but here are a few you may find useful:

 Attribute | 
 Tag | 

 User’s Email Address | 
 {{${email_address}}} | 

 User’s Custom Unsubscribe URL | 
 {{${set_user_to_unsubscribed_url}}} 

This tag replaces the previous {{${unsubscribe_url}}} tag. We recommend that you use the newer {{${set_user_to_unsubscribed_url}}} tag instead. | 

 User’s Custom Opt-In URL | 
 {{${set_user_to_opted_in_url}}} | 

 User’s Custom Subscribe URL | 
 {{${set_user_to_subscribed_url}}} | 

 User’s Custom Braze Preference Center URL | 
 {{${preference_center_url}}} | 

### Including an unsubscribe link and opt-in link

As a best practice, Braze recommends including both an unsubscribe link (such as {{${set_user_to_unsubscribed_url}}}) and an opt-in link (such as {{${set_user_to_opted_in_url}}}) in your custom footer. This way, users can unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.

### Setting custom footers for plaintext emails

You can also choose to set a custom footer for plaintext emails from the Subscription Pages and Footers tab on the Email Preferences page, which follows the same rules as the custom footer for HTML emails.

If you don’t include a plaintext footer, Braze automatically builds one from the HTML footer. When your custom footers are to your liking, select Save.

## Considerations

### BrazeAI Decisioning Studio™

If you’re using BrazeAI Decisioning Studio™, note that {{${email_footer}}} is not a standard Liquid tag. It’s pre-processed before Liquid runs, so using {{${email_footer}}} as a context variable value and calling the :rerender flag silently fails. Instead, use a Content Block for an email footer.

### Link templates and UTM parameters

Link templates are not automatically appended to links in custom email footers when using {{${email_footer}}}. If you need link templates like UTM parameters in your footer links, use a Content Block instead, or manually append the UTM parameters to the specific links in your custom footer.

- 

New Stuff!
