---
url: https://www.braze.com/docs/partners/ai_model_providers/amazon_bedrock
slug: docs__partners__ai_model_providers__amazon_bedrock
title: "Amazon Bedrock"
description: "This reference article outlines the partnership between Braze and Amazon Bedrock, which lets you connect Bedrock models to Braze for use with custom AI agents...."
section: partners/ai_model_providers
fetched: 2026-09-02
evidence: company-own (technical)
---
# Amazon Bedrock

Amazon Bedrock is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

important

The Amazon Bedrock integration is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.

## About the integration

The Braze and Amazon Bedrock integration lets you connect your Amazon Bedrock credentials to Braze so you can use Bedrock-hosted models when building custom AI agents. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using models available through Amazon Bedrock.

When you connect Amazon Bedrock, Braze shows a curated set of Bedrock models for custom agents. The models available in Braze may differ from the full catalog in your AWS account.

Braze uses Amazon Bedrock’s bedrock-mantle endpoint for this integration. Amazon Bedrock also documents a separate bedrock-runtime endpoint with different model and feature support, so when you review AWS documentation for availability or behavior, follow the guidance for bedrock-mantle.

important

This partner appears on your Technology Partners page only if you have Braze Agents enabled. For help getting started, contact your customer success manager.

## Prerequisites

 Requirements | 
 Description | 

 An AWS account with Amazon Bedrock access | 
 An AWS account with access to Amazon Bedrock in the AWS region where your models are hosted. For help, contact your admin or AWS Support. | 

 Amazon Bedrock model access | 
 Access in your AWS account to the Bedrock models you plan to use. Some models, like those from Anthropic, require access to be granted on your AWS account. Not all models are available in every AWS region—check each model’s regional availability in the Amazon Bedrock console or in Regional availability by models before you connect. | 

 Authentication credentials | 
 Either a long-term Amazon Bedrock API key, or—when IAM role authentication is enabled for your workspace—an IAM role that Braze can assume. | 

 Braze instance | 
 You can find your Braze instance on the API overview page or from your Braze onboarding manager. | 

## Integration

To connect Amazon Bedrock to Braze:

- Go to Partner Integrations > Technology Partners in the Braze dashboard, then search for and select Amazon Bedrock.
 
- For Authentication method, choose API key or AWS IAM role (when available).
 
- Complete setup for your chosen method:

- API key: Enter your long-term Amazon Bedrock API key. Select the AWS region where your Bedrock models are hosted. Select Save.
 
- AWS IAM role: Use the values Braze displays to configure your IAM role trust policy, then enter the role details in Braze:

- Copy the Braze AWS account ID and trust that account in your IAM role’s trust policy.
 
- Copy the Braze external ID and require it in your role’s trust policy with an sts:ExternalId condition. Select Generate new external ID if you need a new value.
 
- Enter the AWS role ARN for the IAM role that has Amazon Bedrock permissions. The ARN must match arn:aws:iam::<account-id>:role/<role-name>.
 
- Select the AWS region where your Bedrock models are hosted.
 
- Select Save.

note

AWS IAM role appears only for workspaces where this authentication option is enabled. With IAM role authentication, Braze assumes your role to generate short-lived Amazon Bedrock credentials and does not store a long-term API key.

After you save, Braze displays a connected status with the date and time of the connection. You can select Amazon Bedrock models when creating a custom agent in the Agent Console.

important

Not all Amazon Bedrock models are available in every AWS region. Before you select an AWS region in Braze, open the model details in Amazon Bedrock and confirm the model lists that region. Models that aren’t available in your connected region return errors during agent invocation (for example, that the model does not exist or is no longer available). See Models at a glance for more details.

To confirm the integration is working, go to the Agent Console and create a test agent using one of your Bedrock models. Enter an instruction such as “Tell me a joke,” and run a test invocation to verify the model responds as expected.

To remove the integration, select Disconnect on the Amazon Bedrock integration page.

For issues with your Amazon Bedrock account or credentials, contact AWS Support.

- 

New Stuff!
