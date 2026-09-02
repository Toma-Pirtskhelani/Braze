---
url: https://www.braze.com/docs/user_guide/brazeai/operator/capabilities
slug: docs__user_guide__brazeai__operator__capabilities
title: "What you can do with Operator"
description: "This reference article covers what BrazeAI Operator™ can do across the dashboard, including building campaigns, Canvases, segments, reports, dashboards, and agents; generating copy, messages, Liquid,..."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# What you can do with Operator

BrazeAI Operator™ is an AI assistant built into the Braze dashboard. It answers questions, composes messages, and acts across supported pages—describe what you want in natural language and Operator handles it in context.

Because Operator understands your workspace—custom attributes, Connected Content, the page you’re working on, and any brand guidelines you add as context—its output is more context-aware than what standalone assistants can produce. When Operator proposes a change to a campaign, Canvas, segment, or other object, it shows the change as a visual diff in an action card that you review and approve before anything is saved.

You can keep the conversation going with follow-ups. Operator remembers earlier messages until you clear your chat history.

## Prerequisites

Operator has the same permissions you do, so certain actions require the relevant permission for that surface. For example, generating an image requires Edit Media Library Assets. If you don’t see an entry point, check your permissions with your admin. For more information, see List of permissions.

## Navigate the dashboard

Operator isn’t limited to acting only on the page you’re currently viewing. When a prompt needs a different part of the dashboard, Operator identifies the destination, proposes the navigation, and takes you there before continuing its work.

This means Operator can chain multi-step work together from a single prompt. For example, if you ask Operator from the home page to help set up your drag-and-drop editor settings to match your brand guidelines, it navigates you to the relevant email settings and continues helping you from there. Describe the outcome you want in plain language, and Operator can take you to the relevant settings or feature to begin work.

By default, Operator asks you to approve a proposed navigation before it moves you to a new page, the same as it does for other proposed actions. To let Operator navigate without waiting for your approval each time, turn on Auto-approve actions.

## What Operator can create

Beyond generating copy and Liquid, Operator can help you build several other objects across the dashboard, including but not limited to:

- Campaigns
 
- Canvases
 
- Content Blocks
 
- Custom agents
 
- Custom attributes and custom events
 
- Dashboards
 
- Images
 
- Messages and message templates (see Generate messages and Create message templates)
 
- Predictions
 
- Reports
 
- Segments
 
- Segment Extensions

note

Operator’s capabilities across the dashboard expand regularly. Ask Operator directly for the most current answer of what it can do.

## Campaigns and audiences

Operator can help you go from an idea to a drafted campaign or audience, and refine either one once it exists. Any changes Operator proposes to a campaign or segment appear as an action card you review before they’re saved.

To get started, look for the Create with Operator option when you create a campaign or segment.

- Create and edit campaigns: When you start a campaign, Operator can help you draft it end-to-end from a single natural-language brief. This includes audience, content, and delivery settings. You can also ask Operator to help you edit an existing campaign, such as adjusting targeting or refreshing the message content.
 
- Go from brief to campaign: Describe a full campaign brief, and Operator helps you build a draft that includes copy, images, personalization, targeting, and send-time recommendations. Review the draft in the campaign composer and refine it with follow-up prompts before you launch it.
 
- Create and edit segments: When you start a segment, describe the audience you want and Operator helps you build the filter logic, including attribute conditions, event history, and catalog lookups. Operator can also help you edit an existing segment’s filters when your targeting strategy needs changes.
 
- Create Segment Extensions: Operator can help you build a SQL-defined Segment Extension by writing the query that defines it. Describe the audience logic you want, and Operator drafts the query for you to review before you save it. You can also ask Operator for help from the Segment Extensions overview. For more on Operator and SQL, see Write SQL queries.
 
- Import and manage users: On supported audience pages, Operator can help you import users, delete users, and merge duplicate profiles. Review each proposed action before it’s saved.

## Canvases

Operator can help you go from a journey idea to a drafted Canvas, and refine an existing Canvas. Any changes Operator proposes appear as an action card you review before they’re saved.

Describe the journey in natural language. Operator assembles a draft that can include entry criteria, steps, delays, and messages. You can also ask Operator to edit an existing Canvas, such as adding a step or updating message content. Review the draft in the Canvas builder and refine it with follow-up prompts before you launch it.

For example, ask Operator to build an abandoned cart journey that waits one hour after cart abandonment, sends an email reminder, then a push after 24 hours if the user still hasn’t purchased.

You can start this from any dashboard page. If you aren’t already on Canvas, Operator navigates there to complete the request.

## Agents

Operator can help you build and refine agents in Agent Console. Any changes Operator proposes to an agent appear as an action card you review before they’re saved.

- Create an agent from scratch: Operator has access to every field in Agent Console, so you can describe the agent you want and Operator helps you configure it. This includes instructions, output settings, and other agent fields.
 
- Start from template: Agent Console offers a Create agent with Operator option that loads a pre-written prompt for a common use case, such as copywriting, sentiment analysis, journey routing, or catalog enrichment. Select a category, and Operator helps you draft an agent you can refine. For the full list of templates, see Agent templates built with Operator.
 
- Refine an existing agent: When you’re editing an agent, select Generate with Operator or Refine with Operator near the agent’s instructions field to get Operator’s help writing or revising the agent’s prompt and output settings. If the agent already has a brand guideline, Operator attaches it as context.

## Content and creative

Operator can generate and review the content in your messages, including copy, message HTML, Liquid, and images, and apply any brand guidelines you add as context. You can also ask Operator for help from the template library and overview pages. For example, you can create or update email templates or Content Blocks from their list pages, schedule work on the Content Calendar, create in-app message color profile templates, or configure Banner placements.

### Apply brand guidelines

Add brand guidelines as context in the Operator chat panel so generated copy, templates, and images match your brand’s voice, tone, and style.

### Generate copy

You can use Operator to brainstorm or generate copy from anywhere, but you get the best experience using it directly in the message composer, where it can work alongside you on the message you’re building. Describe your product or campaign, and Operator returns copy you can review and insert.

Operator improves on the standalone copywriter in a few ways:

- It applies any brand guidelines you add as context.
 
- It uses page-aware context, so you don’t have to re-describe the channel or message you’re working on. Because it’s page-aware, you can also use it to edit or refine an existing message instead of generating one from scratch.
 
- It can look up your custom attributes and events, so you can ask it to personalize copy recommendations with real Liquid.
 
- You can keep the conversation going and iterate. For example, ask for a different tone, a shorter version, or a translation.

#### Tones

The tone of generated copy is driven by your prompt. Describe the style you want and Operator adjusts its output to match. For example, ask for formal, casual, urgent, or eye-catching. You can also refine the tone in follow-up prompts, such as asking for a more relaxed or more polished version. When you add brand guidelines as context, Operator applies them so copy stays consistent with your brand’s voice.

### Generate messages

Operator can generate a full message design for any channel or editor with an HTML mode, including but not limited to:

- Email
 
- SMS/MMS/RCS
 
- In-app message
 
- Content Card
 
- Banner
 
- Push
 
- Webhook

Drag-and-drop editors don’t support direct design generation, though Operator can still help with copy or other content you add manually. Describe the message you want in natural language, review the output, and insert it into your composer. Keep the conversation going to refine the result. For example, you can ask for a different layout, shorter copy, or updated button styling before you insert the HTML into the editor.

You get the best results when you use Operator in the composer you’re building, where it has page-aware context for the channel and message type. When you add brand guidelines as context, Operator applies them to the generated message.

### Create Content Blocks

Operator can help you create Content Blocks, the reusable pieces of content you insert across messages. Describe the block you want, and Operator drafts its content for you to review before you save it. Because Content Blocks are shared, updating one updates every message that references it.

Operator creates Content Blocks one at a time in the dashboard. To create Content Blocks in bulk, use the Create Content Block endpoint with an API key that has the content_blocks.create permission.

### Create message templates

Operator can help you create reusable message templates that you can apply across campaigns. Describe the template you want, and Operator drafts it for you to review before you save it. You can start from anywhere in Braze. Generating a template works much like generating a message, so see Generate messages for the supported channels and editors.

### Generate Liquid

Operator is highly capable with Liquid syntax. It can generate complex Liquid logic grounded in the data in your workspace, including looking up attribute, event, and catalog data to find example values. It can also review and explain the existing Liquid in your campaigns.

As with copywriting, you can ask Operator to generate Liquid from anywhere, and it works across all channels and message composers. You get the best results from within a message composer, where Operator has the full context of the message you’re building.

Liquid prompting best practices

#### Give context

Providing context helps Operator understand the bigger picture surrounding your project. It’s helpful to include context such as:

- Your company name and industry
 
- A campaign you’re working on, such as Black Friday or holiday sales
 
- Your goal, such as increasing your click-through rate
 
- Specific custom attributes you want to include in your message

Including context in your prompt helps Operator tailor its responses to better suit your needs. You can also include details from your campaign, message brief, or brainstorming document to bring Operator up to speed.

#### Be specific

Operator can ask follow-up questions, but providing details upfront can lead to more precise results sooner. Consider including details such as:

- Any known preferences or requirements for the message
 
- Instructions on how to handle situations, such as a lack of responses from the message recipient or fallback message options
 
- Exact or similar values for the custom attributes you want to use, which help Operator generate and test more accurate logic
 
- When asking for Liquid that uses Connected Content, documentation for the API endpoint, a sample API response, or both

#### Get creative

Try different prompts to see how Operator can enhance your messaging. Experiment with different prompts and ideas, as creativity can lead to more engaging results.

### Generate images

Operator generates images using GPT Image 2.0, an AI system from OpenAI and a Braze third-party provider. This lets you create realistic images and art from a description in natural language.

In the media library, select Generate with Operator from the Upload Assets panel. Describe the image you want, and Operator generates it and saves it directly to your media library.

#### Prompt tips

- Describe the subject, style, mood, and colors specifically. The more detail you include, the better the result. Uploading a reference image is not supported.
 
- When you apply brand guidelines as context in your Operator prompt, Operator applies them directly to the generated image, so the result reflects your brand’s visual style.
 
- Image generations count toward the company-wide daily Operator usage limit, along with other Operator actions. For more information, see Limitations.

### Review content quality

On the Test tab for SMS, Android push, iOS push, and traditional in-app messages, select Review with Operator to review your content before sending. By default, Operator reviews your campaign for spelling and grammar errors, off-brand or inappropriate tone, offensive language, and any stray code, test content, or unrendered Liquid, and it recommends how to fix what it finds. You can also ask Operator to tailor how it reviews your content directly in your prompt.

Beyond its default review, you can direct Operator to focus on specific checks. Consider prompting it to look at any of the following:

- Spelling and grammar: Proofread for spelling and grammar mistakes and suggest corrections that improve the accuracy of your content.
 
- Tone: Evaluate whether the tone matches your intended communication style and flag anything that could be misunderstood.
 
- Offensive language: Scan for potentially offensive or inappropriate language so you can revise it and keep your messaging respectful.
 
- Accidental content: Catch stray code, markup, or test messages that were added unintentionally, including Liquid that didn’t render for a test user.
 
- Other languages: Review content written in another language. Support for non-English content can vary, so review the results carefully.

#### Best practices

Consider the following to make the most of content review:

- Proofread your message: Although content review can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
 
- Understand the tone analysis: The tone analysis results are subjective and based on the AI model’s understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
 
- Double-check flagged offensive language: Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

## Data automation and lookup

Operator can act as a reference for your workspace data and Braze documentation, write SQL when you need to query that data directly, and generate the code that transforms incoming data, such as a webhook payload, into a format Braze can use.

### What Operator can look up

Operator can reference the following to answer questions or ground the content it generates, including but not limited to:

- Braze documentation
 
- Segments
 
- Custom attributes and custom events
 
- Catalog data
 
- Existing campaign and Canvas configuration, such as targeting and delivery settings
 
- Content Blocks
 
- Promotion codes
 
- Connected Content responses
 
- Agents

Ask Operator directly if you’re not sure whether it can look up a specific piece of information.

### Analyze performance data

Ask Operator plain-language questions about your campaign and Canvas performance, and it returns charts, comparisons, and short insights pulled from your workspace data. Unlike Operator’s page-aware features, which need context from the page you’re on, Analyze answers from anywhere in the dashboard. For more information, see Operator Analyze.

### Build reports and dashboards

Operator can help you build Report Builder reports and Dashboard Builder dashboards from a natural-language brief. Describe the metrics, channels, and date range you want, and Operator drafts the report or dashboard for you to review before you save it.

For example, ask: “Build me a report that shows my workspace SMS engagement over the last 30 days.”

### Create predictions

Operator can help you view and create Predictive Churn predictions and AI Item Recommendations. Describe the outcome you want, and Operator proposes the prediction or recommendation for you to review.

### Write SQL queries

Operator can help you write SQL for Segment Extensions and for Query Builder query templates. Describe the query you want in natural language, and Operator generates SQL for you to review before you run it.

### Generate data transformation code

In the Data Transformation editor, select Insert Code to generate transformation code that turns an incoming webhook payload into valid Braze API requests. For step-by-step instructions on creating a transformation, see Create a transformation.

## Workspace settings

Operator can review and update settings across several workspace configuration pages. Describe the change you want, and Operator proposes it as an action card you review before it’s saved. Supported settings pages include but aren’t limited to:

- Quiet hours
 
- Push settings
 
- Messaging rate limits
 
- Approval workflows, including messaging rules and always-on approval
 
- APIs and identifiers, including other identifiers, API limits, and API usage alerts
 
- Admin settings contact information
 
- Security settings and SCIM provisioning
 
- Roles and permission sets
 
- Exports log
 
- Message prioritization categories

note

Operator’s coverage of settings pages expands regularly. Ask Operator directly for the most current answer of what it can configure.

## Limitations

note

Operator’s coverage changes frequently. If you’re not sure whether a specific screen or workflow is supported, ask Operator directly.

Operator’s dashboard support is broad, but it has boundaries.

- Canvases: Operator can create and edit Canvases in the current Canvas editor. It doesn’t support the original Canvas editor, starting a Canvas from the template selection page, or using Preview as User while building Canvases. Operator can still reference an existing Canvas’s configuration, such as targeting and delivery settings, to answer questions and ground its output.
 
- Campaign duplication: Operator can’t duplicate an existing campaign from the campaigns list view. To create a similar campaign, ask Operator to build a new one from scratch, or duplicate the campaign manually from the list view’s More Actions menu.
 
- Drag-and-drop editors: Operator can’t generate or insert a message design directly in a drag-and-drop editor, such as the ones for email, Banners, and in-app messages. Switch to the corresponding HTML editor to use Operator, or ask Operator to generate content, such as copy, that you can paste in manually. See Generate messages for supported channels and editors.
 
- Screen visibility: Operator uses page-aware context to understand what you’re looking at, including content inside supported previews and editors. When part of a page falls outside what Operator can read, it tells you instead of guessing, so you know to describe that content yourself.
 
- Usage limits: Operator has a company-wide daily usage limit that resets every 24 hours. All Operator actions count toward this limit, and usage scales with how much Operator has to read and produce. Asking questions, looking up information, and filing a support ticket are lighter usage. Creating or editing objects such as campaigns and segments is heavier usage. Image generations also count toward this limit. If the limit is reached, a “Daily limit reached” message appears and Operator doesn’t process further requests until the limit resets. For troubleshooting steps, see Troubleshooting.

## Legacy assistants

Before Operator, several AI features stood alone as separate assistants: the AI Copywriter, AI Liquid Assistant, AI Image Generator, AI SQL Generator, the Data Transformations AI Copilot, and content review. All of their entry points remain in place and route to Operator, so your existing workflows are unaffected. For what these do today, see Content and creative and Data automation and lookup.

## How is my data used and sent to OpenAI?

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per OpenAI’s API platform commitments, data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

## Data privacy and security

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see How data is used with OpenAI.

## Next steps

- Get started with Operator: Access and use Operator
 
- Prompt library: Browse ready-to-use example prompts
 
- Review actions: Review and approve Operator’s proposed changes
 
- Troubleshooting: Reference common issues and solutions

- 

New Stuff!
