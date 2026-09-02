---
url: https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines
slug: docs__user_guide__administer__global__workspace_settings__brand_guidelines
title: "Brand guidelines"
description: "This reference article describes how to create, manage, and add brand guidelines as context for Operator and agents."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Brand guidelines

Tailor the style of your AI-generated copy to match your brand’s voice, tone, and personality with customized brand guidelines.

Create and manage brand guidelines from Content > Brand Guidelines.

## Creating brand guidelines

### Step 1: Create a brand guideline

On the Brand Guidelines page, select Create new. If you want this brand guideline to be the default for the workspace, select Use as default brand guideline. You can have one default per workspace.

### Step 2: Describe your brand personality

For Brand personality, think about what makes your brand unique. Include traits, values, voice, and any archetypes that define your brand. Keep this field to 10,000 or fewer characters. If you generate this text with an LLM, include that character limit in your prompt so the output fits the field.

Here are some characteristics to consider:

 Characteristic | 
 Definition | 
 Example | 

 Reputation | 
 How you want your brand to be perceived in the market. | 
 We are known for being the most reliable and customer-focused brand in our industry. | 

 Personality traits | 
 Human-like characteristics that describe your brand’s character. | 
 Our brand is friendly, approachable, and always upbeat. | 

 Values | 
 Core values that guide your brand’s actions and decisions. | 
 We value sustainability, transparency, and community. | 

 Differentiation | 
 Unique qualities that set your brand apart from competitors. | 
 We stand out by offering personalized customer service that goes the extra mile. | 

 Brand voice | 
 The tone and style of communication your brand uses. | 
 Our voice is casual yet informative, ensuring clarity without being too formal. | 

 Brand archetype | 
 The archetype that represents your brand’s persona (The Hero, The Creator, and so on). | 
 We embody the “Explorer” archetype, always seeking new challenges and adventures. | 

### Step 3: Define language that should be avoided (optional)

For Exclusions, list any language or style that doesn’t align with your brand. For example, you might want to avoid “sarcasm,” “negative attitudes,” or “condescending” tones. Keep this field to 300 or fewer characters.

### Step 4: Test your guidelines

Test your guidelines to see how they perform. Expand Test your guidelines to generate example copy and adjust as needed.

### Step 5: Save your guidelines

When you’re happy with your guidelines, select Save brand guideline. Your guidelines are saved to your workspace for future use.

important

You can change the output language regardless of what language your copy is in, but neither Braze nor OpenAI guarantees the quality of translation. Always test and verify translations before using them.

## Managing brand guidelines

You can edit brand guidelines by selecting them on the Brand Guidelines page. Archive a brand guideline to make it inactive and unavailable in message composers. To make it active and selectable again, you can filter for archived brand guidelines and then unarchive it.

## Using brand guidelines

In the Operator chat panel, select  Add context for Operator, then choose one or more guidelines under Brand guidelines. Operator applies the guidelines you select to generated copy, templates, and images. By default, nothing is selected.

When you configure an agent, select brand guidelines under Add context so the agent follows that voice and style. Agent Console selects the workspace default for you.

## How is my data used and sent to OpenAI?

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per OpenAI’s API platform commitments, data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

- 

New Stuff!
