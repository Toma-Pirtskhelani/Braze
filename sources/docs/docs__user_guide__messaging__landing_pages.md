---
url: https://www.braze.com/docs/user_guide/messaging/landing_pages
slug: docs__user_guide__messaging__landing_pages
title: "About landing pages"
description: "This article contains resources on building and customizing Braze landing pages."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# About landing pages

Braze landing pages are standalone web pages that can drive your user acquisition and engagement strategy.

Use landing pages to grow your audience, capture user data, promote special offers, and support multichannel campaigns. For a reference of landing page drag-and-drop blocks, see Editor blocks (landing pages).

note

Landing page and custom domain availability depends on your Braze package. Contact your account manager or customer success manager to get started.

## Prerequisites

Before you can access, create, and publish landing pages, you either need administrator permissions or all the following permissions:

- View Landing Pages
 
- Edit Landing Page Drafts
 
- Publish Landing Pages

important

To gain access to the drag-and-drop editor, contact your IT administrator to verify that your firewall has *.bz-rndr.com allowlisted.

## Plan tiers

The number of published landing pages, custom domains, and features you can use depends on your plan type: free or pro (incremental).

 Feature | 
 Free tier | 
 Pro tier (incremental) | 

 Published landing pages | 
 Five per company | 
 20 additional | 

 Custom domains | 
 One per company | 
 Five additional | 

 Liquid personalization | 
 Not available | 
 Available | 

 Prefilled form fields | 
 Not available | 
 Available | 

## Rate limits

Braze applies a rate limit of 500 requests per three seconds (approximately 167 requests per second) per workspace for uncached landing pages. This limit helps maintain system performance and reliability during high-traffic periods.

Cached landing page views don’t count toward this limit. For how caching affects traffic, see Can landing pages handle high-traffic scenarios?.

## Adding Google Tag Manager to a landing page

To add Google Tag Manager to your landing pages, add a Custom Code block to your landing page in the drag-and-drop editor, then insert the Tag Manager code into the block. Make sure to add a data layer before the Tag Manager code, such as in this example:

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

```
 | 
```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->

```
 | 

For details on implementing Google Tag Manager, see Google’s documentation.

## Frequently asked questions

### What’s the maximum size for landing pages?

The landing page body size can be up to 500 KB.

### Can landing pages handle high-traffic scenarios?

Yes. Non-personalized landing pages handle high-traffic scenarios effectively. When a landing page is first requested, Braze caches it through Cloudflare. Subsequent requests for the same link are served from cache, which helps during high-traffic periods. This cache lasts 24 hours, and cached page views don’t count toward rate limits.

Personalized landing pages use a shorter Cloudflare cache and generate more uncached requests to Braze. Those uncached requests are subject to the per-workspace rate limit described in Rate limits.

For size limits and other performance guidance for personalized pages, see Personalization considerations.

### Are there any technical requirements to publish a landing page?

No, there aren’t any technical requirements.

### Is there an HTML editor for landing pages?

Yes. Use the Custom Code block in the drag-and-drop editor to add or edit HTML. To interface with the Braze SDK from your custom code, see JavaScript bridge for landing pages. To connect a fully custom UI to a landing page form, see Create custom form blocks.

### Can I use iframes on landing pages?

Yes. Add a Custom Code block in the drag-and-drop editor and include an iframe element with the URL of the content you want to embed.

If the embedded website restricts framing through frame-ancestors in its Content Security Policy (CSP) or X-Frame-Options, the page may not load in the iframe. Braze can’t override those settings—the embedded site must be configured to allow your landing page domain.

### Can I create a webhook inside a landing page?

No, but the Submitted a Landing Page form event can act as a trigger for Canvases or webhook campaigns:

- Canvas: Use the Submitted a Landing Page form event as a Canvas entry trigger and add a webhook step.
 
- Campaign: Use the Submitted a Landing Page form event to trigger based on form submission.

When the page isn’t sent through a Braze channel (such as through a website or ad), a new user profile may be created on submission—even if that person already exists in Braze. To handle this, set up a Canvas triggered by Submitted a Landing Page form and add a Braze-to-Braze webhook step that calls the /users/merge endpoint to merge the new profile into the existing one.

When you use the landing_page_url Liquid tag to share the page, form submissions are automatically tied to the existing user profile. You can then reference the user attributes submitted on the landing page through Liquid for subsequent templating.

- 

New Stuff!
