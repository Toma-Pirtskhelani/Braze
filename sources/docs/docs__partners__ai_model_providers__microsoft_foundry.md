---
url: https://www.braze.com/docs/partners/ai_model_providers/microsoft_foundry
slug: docs__partners__ai_model_providers__microsoft_foundry
title: "Microsoft Foundry"
description: "This reference article outlines the partnership between Braze and Microsoft Foundry, which lets you connect Foundry-managed AI models to Braze for use with custom AI..."
section: partners/ai_model_providers
fetched: 2026-09-02
evidence: company-own (technical)
---
# Microsoft Foundry

Microsoft Foundry is a unified Azure platform-as-a-service offering for enterprise AI operations, model builders, and application development.

## About the integration

The Braze and Microsoft Foundry integration lets you use generative AI models managed in Microsoft Foundry when building custom AI agents. The integration currently supports two models: gpt-5.4-mini and gpt-5.4-nano. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using Foundry-managed models.

important

This partner appears on your Technology Partners page only if you have Braze Agents enabled. For help getting started, contact your customer success manager.

## Prerequisites

 Requirements | 
 Description | 

 An Azure account with an active subscription | 
 For help, contact your admin or see Azure account options. | 

 Microsoft Foundry instance | 
 A Microsoft Foundry instance to create a project. | 

 Microsoft Foundry project | 
 A project within your Foundry instance to house the deployed models. | 

 Deployed models | 
 At least one of the supported models deployed within the Foundry project. | 

 Braze instance | 
 You can find your Braze instance on the API overview page or from your Braze onboarding manager. | 

## Deploy supported models in Foundry

The Braze integration with Microsoft Foundry supports two models: gpt-5.4-mini and gpt-5.4-nano. Both must be deployed in a Foundry project within the Foundry instance you’re integrating.

To create the Foundry project and deploy the models, follow the Microsoft Foundry documentation:

- Sign in to Microsoft Foundry through your Azure portal.
 
- In Microsoft Foundry, create a project to house the models you want to integrate with Braze.
 
- Decide whether to use gpt-5.4-mini, gpt-5.4-nano, or both.
 
- For each model you want to use, deploy it using the Microsoft Foundry documentation. Do not change the default deployment name, or the integration for that model may break.

## Integration

To connect your Foundry instance to Braze:

- Go to Partner Integrations > Technology Partners in the Braze dashboard and find Microsoft Foundry.
 
- Enter your Microsoft Foundry API Key.
 
- Enter your Microsoft Foundry instance name. This is the subdomain before .services.ai.azure.com.
 
- Select Save.

After you save, Braze displays a connected status with the date and time of the connection. You can select Foundry models when creating a custom agent in the Agent Console.

important

To use gpt-5.4-mini or gpt-5.4-nano, you must deploy each model in your Foundry project without changing the default deployment name.

To confirm the integration is working, go to the Agent Console and create a test agent using one of your deployed models. Enter a simple instruction, such as “Tell me a joke,” and run a test invocation to verify the model responds as expected.

To remove the integration, select Disconnect on the Microsoft Foundry Integration page.

Contact Azure support with any issues or questions regarding your integration.

- 

New Stuff!
