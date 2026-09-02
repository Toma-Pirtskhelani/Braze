---
url: https://www.braze.com/docs/partners/ai_model_providers/google_gemini
slug: docs__partners__ai_model_providers__google_gemini
title: "Google Gemini"
description: "This reference article outlines the partnership between Braze and Google Gemini, which lets you connect Gemini models to Braze for use with custom AI agents...."
section: partners/ai_model_providers
fetched: 2026-09-02
evidence: company-own (technical)
---
# Google Gemini

Google Gemini is Google’s family of AI models that combines advanced reasoning across text, code, and images to help brands deliver smarter, more personalized experiences.

important

This partner appears on your Technology Partners page only if you have Braze Agents enabled. For help getting started, contact your customer success manager.

This integration is maintained by Google.

## About the integration

The Braze and Google Gemini integration lets you connect Gemini to Braze using an API key or by signing in with your Google account so you can use Gemini models when building custom AI agents. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using Google’s Gemini models.

## Prerequisites

 Requirements | 
 Description | 

 Google Cloud account | 
 A Google Cloud account with access to the Gemini API. You can authenticate with an API key or by connecting your Google account and selecting a GCP project in the Braze dashboard. For help, contact your admin or Google Cloud support. | 

 Braze instance | 
 You can find your Braze instance on the API overview page or from your Braze onboarding manager. | 

## Integration

To connect Google Gemini to Braze:

- Go to Partner Integrations > Technology Partners in the Braze dashboard and find Google Gemini.
 
- For Authentication Method, choose API Key or Connect Google Account.
 
- Complete setup for your chosen method:

- API Key: Under API Type, select Gemini API or Gemini Enterprise Agent Platform (formerly Vertex AI). Enter your API key. If you selected Gemini Enterprise Agent Platform, also enter your Project ID. Select Save.
 
- Connect Google Account: Select Connect Google Account, then select Connect Google and sign in with your Google account. Select your GCP Project from the dropdown. If both Gemini API and Gemini Enterprise Agent Platform are enabled in that project, choose the API Type Braze should use. Select Save.

note

Connect Google Account appears only for workspaces where this authentication option is enabled.

After saving, you can select Gemini models when creating a custom agent in the Agent Console.

Contact Google Cloud support with any issues or questions regarding your integration.

- 

New Stuff!
