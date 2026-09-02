---
url: https://www.braze.com/docs/partners/message_orchestration/templates/copy_pastd
slug: docs__partners__message_orchestration__templates__copy_pastd
title: "Copy Pastd"
description: "This reference article outlines the partnership between Braze and Copy Pastd, a drag-and-drop email builder that pushes Liquid-powered Content Blocks and templates directly into your..."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Copy Pastd

Copy Pastd offers Building Blocks, a drag-and-drop email builder that pushes Liquid-powered Content Blocks and full templates directly into your Braze workspace. Design once, sync to Braze, and reuse the same components across campaigns, Canvases, and triggered flows without rebuilding HTML each time.

This integration is maintained by Copy Pastd.

## About the integration

The Braze and Copy Pastd integration lets you build emails in Building Blocks—a hosted email builder that produces Braze-native output with clean Liquid, Content Block references, and templates that drop into any campaign or Canvas without translation.

You can assemble an email from reusable blocks, push it to Braze in one click, and trust that the same brand styles, components, and dynamic content render consistently across every send. The result is fewer hand-coded templates, less time spent creating and sending emails, and a centralized library that updates everywhere when it changes.

## Prerequisites

The following are required to use this integration:

 Requirement | 
 Description | 

 Copy Pastd account | 
 Required to use Building Blocks. Sign up at copypastd.com. Each customer gets a workspace, a stylesheet library, five builder seats, and a block library. | 

 Braze REST API key for email templates | 
 An API key with templates.email.create, templates.email.update, and templates.email.list permissions.

Create the key in the Braze dashboard from Settings > API Keys. | 

 Braze REST API key for Content Blocks | 
 An API key with content_blocks.create, content_blocks.update, content_blocks.info, and content_blocks.list permissions.

Create the key in the Braze dashboard from Settings > API Keys. | 

 Braze REST API key for Catalogs (optional) | 
 An API key with read access to catalogs.get, catalogs.get_item, and catalogs.get_selections. Required only if you plan to bind blocks to Braze Catalogs. | 

 Braze REST endpoint | 
 Your REST endpoint URL. Your endpoint depends on the Braze URL for your instance. Building Blocks selects the endpoint automatically based on the cluster you choose. | 

## Use cases

- Brand-consistent authoring at scale. Apply a Building Blocks stylesheet to every template, and colors, fonts, button styles, and padding scale render identically across hundreds of emails. When the brand changes, update the stylesheet once and resync to roll out the update across all your emails at once.
 
- Connected Content and Catalog-bound product templates. Bind email block fields directly to your Connected Content endpoints and Braze Catalogs from inside the builder. Reuse the same template for new product drops, seasonal collections, or content refreshes without touching Liquid.
 
- Self-serve email production for non-technical marketers. Compose a full email from approved blocks, including Liquid personalization and logic, and push it to Braze for review without developer support to write HTML or Liquid or review either.
 
- Central headers and footers, updated in one click. Build a header or footer once in the Building Blocks builder and push it to Braze. Every template that references it stays in sync, so a logo swap, a legal copy change, or a new social link takes only one update inside Building Blocks to land across every email already in Braze.
 
- Centralized content across all emails. Build a hero, footer, or promo card once as a Building Blocks smart block. Update it, sync, and every email already in Braze that references it picks up the change on the next send. Welcome flows, weekly newsletters, and triggered journeys stay fresh without editing each campaign.
 
- Locked templates for contributors to self-serve. Build templates, lock selected fields, then invite other teams to build their own emails from a contributor interface without granting them access to user-facing tools.

## Integration

### Step 1: Connect Building Blocks to Braze

note

Connecting Building Blocks to Braze is a one-time setup. After your credentials validate, Building Blocks saves the credentials for all future syncs and template pushes.

- Log in to Building Blocks at blocks.copypastd.com, or select Login at copypastd.com.
 
- From the dashboard, select Set up your Braze connection. (This pill appears for admins on first login and until completed. You can also access the page from Team Settings > Connect > Braze API Keys.)
 
- Select your Braze cluster from the dropdown. The matching REST endpoint is completed for you.
 
- Paste your Templates API key, your Content Blocks API key, and (optionally) your Catalogs API key into the relevant fields.
 
- Select Validate and save. Building Blocks calls Braze to confirm the keys work and the permission scopes are correct. If anything is missing, an inline error shows you which scope is wrong.

### Step 2: Sync your library to Braze

- After the keys validate, select Sync now in the setup modal. (You can also resync any time from Settings > Connect > Braze > Sync library.) 
 Building Blocks pushes your stylesheet and blocks into your Braze workspace as Braze Content Blocks. They appear in Braze under names prefixed with CP_ (for example, CP_Hero_1) or cp_ for stylesheets (for example, cp_default_style).
 
- After the sync finishes, you can push individual templates from the builder using Push to Braze.

## Customize Building Blocks

### Step 1: Set up your stylesheet

- In Building Blocks, navigate to Settings > Build > Stylesheets.
 
- Edit the default stylesheet or create a new one. Set your color palette (24 named colors), fonts (Google Fonts supported), button styles, link styles, radius, and padding scale.
 
- Select Save. Building Blocks regenerates the Liquid for every block that uses this stylesheet.
 
- Select Sync now to push the updated styles into your Braze workspace.

### Step 2: Enable Connected Content endpoints (optional)

- In Building Blocks, navigate to Settings > Connect > Connected Content endpoints.
 
- Add the endpoint URL, name it, and save. Building Blocks supports a Google Sheets response shape in addition to the standard JSON shape.
 
- In the builder, bind any text, image, or link field to a Connected Content variable from the Personalize panel. The correct {% connected_content %} Liquid is generated at export.

### Step 3: Bind to Braze Catalogs (optional)

- In Building Blocks, navigate to Settings > Connect > Catalogs. Building Blocks reads your catalog list using the Catalogs API key.
 
- Open a compatible block (for example, a product grid).
 
- Select a catalog and a selection, then map block fields to catalog item attributes.
 
- Push the template. Building Blocks emits the correct {% catalog_items %} and {% catalog_selection_items %} Liquid for Braze to resolve at send time.

### Step 4: Add your Braze custom attributes (optional)

Building Blocks comes with the default Braze user attributes (first_name, email, country, and so on). To bind blocks to your own custom attributes, import them into Building Blocks once and they remain available in every Personalize dropdown.

- In Building Blocks, navigate to Team Settings > Connect > Custom Attributes.
 
- Import your custom attributes using one of the following methods:

- Bulk import (recommended). In Braze, navigate to Data Settings > Custom Attributes and select Export. Upload the CSV in Building Blocks.
 
- Add attributes one at a time. Type the attribute name (for example, loyalty_tier) and select Add. This method is useful if you’re adding only several attributes or if you want to add a new attribute between Braze exports.

After you save, your custom attributes appear in the builder’s Personalize dropdown alongside the defaults. Inserting one renders the correct {{custom_attribute.${name}}} Liquid at export, so Braze resolves the value per recipient at send time.

## Use the integration

### Step 1: Push a template to Braze

- Open any email in the Building Blocks builder.
 
- Select Push to Braze in the action bar.
 
- Select the workspace and confirm. Building Blocks creates an email template in Braze with the rendered Liquid.

The template appears in Braze under Templates & Media > Email Templates, named after the email and the selected date in the email settings.

### Step 2: Use the template in a campaign or Canvas

- In Braze, create a new email campaign or Canvas step.
 
- Select Templates and choose the template Building Blocks pushed.

The template carries every Building Blocks reference (stylesheet, Content Blocks) as live {{content_blocks.${...}}} Liquid, so updates in Building Blocks propagate without re-importing the template.

### Step 3: Update content centrally

- In Building Blocks, edit the relevant block or stylesheet.
 
- Select Sync to push the updated Content Block back to Braze.

Every email in Braze that references it (evergreen, triggered, welcome flows) picks up the new version on the next send. You do not need to edit each campaign.

### Step 4: Build content pools

Content pools are tables of content rows that emails reference instead of containing static copy. Update the pool in Building Blocks, and every email in Braze that uses it serves the new content on the next send. Use content pools anywhere the same piece of content needs to stay fresh across many emails, such as weekly newsletters, welcome flows, win-back sequences, seasonal campaigns, or post-purchase journeys.

- In Building Blocks, select Content in the primary nav.
 
- Select New Pool. Provide a name that describes what it holds (for example, Weekly Offers, Product Catalog, News Articles).
 
- Choose the block type the pool feeds (for example, Hero, Grid, Card). This sets which fields are available on each row.
 
- Add rows. Each row is one piece of content. Complete the fields (headline, image, CTA text, CTA link, and so on).
 
- Set the priority order by dragging rows up or down. Toggle each row active or inactive, and set optional start and end dates. At send time, the highest-priority active row whose dates are valid wins.
 
- Click Save. Smart blocks can now reference this pool.

### Step 5: Use smart blocks to render pool content in your emails

A smart block is a block on the builder canvas that references one or more content pools instead of holding static content. At send time, Braze renders the pool row that is highest priority, active, and date-valid. The exported Liquid does the work. No extra Braze setup is needed.

- In Building Blocks, drag a smart block onto the canvas (any block type that has a matching pool).
 
- In the properties panel, open the cascade editor.
 
- Add one or more content pools in priority order. This is the waterfall: the first pool with an active, date-valid row renders. If it has nothing live, the smart block falls through to the next pool, then the next. A common pattern is Flash Sale > Weekly Offers > Evergreen Favorites, so there’s always something on hand.
 
- Push the template to Braze. The exported Liquid carries the full cascade, so Braze evaluates pool priority and dates at every send.

From now on, you update the pool, not the email. Triggered flows, evergreen newsletters, and seasonal campaigns all stay current as long as the pool is current.

Find your uploaded Building Blocks templates in Braze under Templates & Media > Email Templates. Synced stylesheets and blocks appear under Templates & Media > Content Blocks.

## Considerations

- One Braze instance per Building Blocks team space. Each Building Blocks team connects to a single Braze instance. Customers running multiple workspaces (separate brands, regions, or environments) can add them to the same team, which allows sharing blocks.
 
- API key permissions are scoped separately. Templates keys and Content Blocks keys are kept apart. Validation fails fast if a key is missing a required scope, so you know exactly which permission to add in Braze.
 
- Content Block names are namespaced. Building Blocks pushes Content Blocks with CP_ (blocks) and cp_ (stylesheets) prefixes to avoid collisions with Content Blocks created directly in Braze.
 
- Stylesheet edits update every email. Stylesheets render as a single Braze Content Block referenced by every template. A change in Building Blocks updates every email in Braze that uses it, including those already scheduled. Test stylesheet changes in a draft template before syncing.
 
- Catalog binding is read-only. Building Blocks reads catalogs to populate the binding UI. It does not write to Braze Catalogs. All catalog management still happens in the Braze dashboard.
 
- Rate limits and retries. All outbound requests respect Braze’s rate limits, with exponential backoff, jitter, and Retry-After handling. A User-Agent: partner-CopyPastd header is sent on every call for partner attribution.
 
- No user data is transmitted. Building Blocks is a content authoring tool. It does not push user attributes, events, purchases, or segment data to Braze, and it does not consume Braze data points.

## Troubleshooting

- API key validation fails. Check that each key carries the exact permissions listed in Prerequisites. Templates and Content Blocks scopes are checked separately. If you regenerate a key in Braze, paste the new value into Building Blocks and revalidate.
 
- REST endpoint mismatch. Templates and Content Blocks keys must come from the same Braze workspace, and the REST endpoint must match the cluster. The Building Blocks dropdown sets this for you, so check the cluster selection if validation fails.
 
- Push to Braze returns an error. Open Settings > Build > Activity log to see the last sync attempt and the response Braze returned. Most failures are permission-related (missing scope) or quota-related (rate limit, retried automatically).
 
- Content Block not updating in Braze. Trigger a manual resync from Settings > Connect > Braze > Sync library. Building Blocks performs a compare-and-swap, so unchanged blocks are skipped.
 
- Template references a Content Block that does not exist in Braze yet. Push the dependencies first (stylesheet, smart blocks) using Sync library, then push the template.
 
- For everything else. Contact Copy Pastd at [email protected]. Include your team name and the time of the failed action so Copy Pastd can pull the matching activity log.

- 

New Stuff!
