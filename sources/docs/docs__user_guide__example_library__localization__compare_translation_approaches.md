---
url: https://www.braze.com/docs/user_guide/example_library/localization/compare_translation_approaches
slug: docs__user_guide__example_library__localization__compare_translation_approaches
title: "Compare approaches for managing multi-language translations"
description: "Compare manual Liquid, Content Blocks, catalogs, multi-language messages, translation partners, and Connected Content to choose how Kitchenerie manages localized copy."
section: user_guide/example_library
fetched: 2026-09-02
evidence: company-own (technical)
---
# Compare approaches for managing multi-language translations

Evaluate how localized copy is stored, updated, previewed, and sent so you can choose a localization approach that fits your QA workflow, channel mix, and update frequency.

## About this example

Kitchenerie, a fictional kitchenware retailer, sends email, push, and in-app messages in English, French, and German. Marketing and engineering need a repeatable, scalable way to manage translations across campaigns.

Braze supports several localization patterns:

- Manual conditional Liquid: Copy entered per language in the message body
 
- Content Blocks: Reusable blocks (with or without multi-language translation tags)
 
- Catalogs: Structured translation rows keyed by locale
 
- Multi-language messages: Translation tags, CSV uploads, and the translation API (early access)
 
- Translation partners: Smartling, Phrase, Lokalise, and others
 
- Connected Content: Localized strings fetched from your CMS or API at send time

This example compares tradeoffs so you can match an approach to your QA workflow, channel mix, update frequency, and team resources. It doesn’t replace step-by-step setup for any single method. For feature walkthroughs, start with Localization and Multi-language messages.

## Considerations

- Decide whether you need dashboard preview and QA, professional translation workflows, high-frequency content updates, or real-time CMS-driven copy before you pick a pattern.
 
- Multi-language messages support email, push, banners, in-app messages, and Content Blocks. Note that SMS and WhatsApp use other localization patterns. Manual Liquid, Content Blocks, catalogs, partners, and Connected Content can apply across channels where those features are supported.
 
- Braze does not generate translations. You supply copy through the dashboard, CSV, API, catalog import, partner workflow, or external CMS.
 
- Manual Liquid and Content Blocks with embedded conditionals need naming conventions and review processes as languages grow, and multi-language and partner workflows centralize updates but may require CSV or API maintenance.
 
- Connected Content and some partner flows depend on external systems. If an API or CMS is unavailable at send time, localized content may fail to load.
 
- Overlap is common. For example, you may use multi-language tags for email bodies, Content Blocks for shared footers, and catalogs for product copy in the same program.

## Setup

### Step 1: Capture your localization requirements

 Requirement | 
 Questions to answer | 

 Preview and QA | 
 Do marketers need to preview each locale in the Braze composer before send? | 

 Scale | 
 How many languages and how often does copy change? | 

 Workflow | 
 Do you need translator review, revisions, and approvals? | 

 Data shape | 
 Is copy free-form marketing text, or structured product fields (names, prices, URLs)? | 

 Automation | 
 Should translations update automatically when your CMS changes? | 

 Team skills | 
 Can your team maintain Liquid, CSV uploads, APIs, or partner integrations? | 

### Step 2: Compare approaches at a glance

 Dimension | 
 Manual Liquid | 
 Content Blocks | 
 Catalogs | 
 Multi-language messages | 
 Translation partners | 
 Connected Content | 

 Dashboard preview / QA | 
 Yes | 
 Yes | 
 Yes | 
 Yes | 
 Varies by partner | 
 Limited—harder to preview fetched content | 

 Default (no integration) | 
 Yes | 
 Yes | 
 Partial—catalog setup required | 
 Yes | 
 No—vendor setup | 
 No—API or CMS required | 

 Channel coverage | 
 All supported channels | 
 All supported channels | 
 All supported channels | 
 Email, push, banners, in-app messages, Content Blocks | 
 Varies by partner | 
 All supported channels | 

 Implementation effort | 
 Low | 
 Low–medium | 
 Medium | 
 Low | 
 High (partner-dependent) | 
 Medium | 

 Ongoing (BAU) effort | 
 High—per-message edits | 
 Medium—block maintenance | 
 Medium—CSV or API updates | 
 Medium—CSV uploads | 
 Medium—managed in platform | 
 Low—fetched at send time | 

 High-frequency updates | 
 No | 
 Partial | 
 No | 
 Partial | 
 Yes | 
 Yes | 

 Professional translation workflow | 
 No | 
 No | 
 No | 
 No | 
 Yes | 
 No | 

 Structured / product data | 
 Limited | 
 Limited | 
 Yes—ideal for keyed copy | 
 Limited | 
 Varies | 
 Yes—through external source | 

 External dependency risk | 
 None | 
 None | 
 None | 
 None | 
 Medium | 
 Medium—send fails if source is down | 

 Best suited for | 
 Few languages, infrequent updates | 
 Shared components across messages | 
 Many locales of structured strings | 
 Many languages with lower copy-paste effort | 
 Enterprise translation with approvals | 
 Dynamic CMS-driven localization | 

### Step 3: Match Kitchenerie-style scenarios to an approach

 Kitchenerie scenario | 
 Recommended starting point | 

 Three languages, few campaigns per month, small marketing team | 
 Manual conditional Liquid or Content Blocks with Liquid | 

 Shared header, footer, and legal blocks across email and IAM | 
 Content Blocks—with multi-language translations saved on the block when locales scale | 

 Product names, promo lines, and image URLs keyed by locale | 
 Catalogs | 

 Email and push in eight or more locales with composer preview | 
 Multi-language messages | 

 Central TMS with translator workflow and approvals | 
 Localization partners (for example Smartling or Phrase) | 

 Copy owned in a CMS that updates daily | 
 Connected Content | 

### Step 4: Implement the approach you selected

- Manual conditional Liquid: Use profile language or locale attributes with if / elsif / else Liquid. See Alternative approaches and Conditional logic.
 
- Content Blocks: Create reusable blocks; optionally hide conditional Liquid inside blocks. See Content Blocks and the Content Blocks tab under Sending translated messages.
 
- Catalogs: Import translation rows (for example id, context, language, body) and reference them with Liquid catalog_items. See the Catalogs tab under Sending translated messages.
 
- Multi-language messages: Add locales, wrap copy in translation tags, then upload a CSV. If you have early access to the translation endpoints, you can update translations by API instead. Preview with Multi-language user in the composer.
 
- Translation partners: Configure workspace locales, then follow your partner integration (for example Smartling or Phrase).
 
- Connected Content: Call your CMS or translation API at send time. Test thoroughly; preview may not reflect live API responses. See Connected Content.

For Canvas and campaign orchestration across regions (one journey versus one journey per country), see Translation management on the Localization page.

## Related articles

- Localization
 
- Multi-language messages
 
- Localization settings
 
- Content Blocks
 
- Catalogs
 
- Connected Content
 
- Localization partners
 
- Accessibility language for localized messages

- 

New Stuff!
