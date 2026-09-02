---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalized_recommendations/certona
slug: docs__partners__message_personalization__dynamic_content__personalized_recommendations__certona
title: "Certona"
description: "This reference article outlines the partnership between Braze and Certona, a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle. Use Certona with..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Certona

Certona’s platform drives personalization across the customer lifecycle. From highly individualized email campaigns to machine-learning-powered product recommendations, Certona ensures that you’re harnessing the power of personalization.

This integration is maintained by Certona.

## About the integration

The Braze and Certona integration uses Certona’s machine learning product recommendations in Braze campaigns and Canvases through Connected Content.

## Prerequisites

 Requirement | 
 Description | 

 Certona account | 
 A Certona account is required to take advantage of this partnership. | 

 Certona REST API endpoint | 
 This endpoint is used directly in your Braze campaign message to pull recommended content based on user ID. | 

## Integration

Use Certona’s REST API to insert personalized content into your messages. This can be done by adding the following Connected Content template into your Braze message composer along with your Certona REST API endpoint.

```

1

```
 | 
```
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}

```
 | 

Next, define the content you would like to call such as relevant text or images. For example, {{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}.

Once you put this message into the composer body, preview your Connected Content call to make sure you have displayed the correct information.

- 

New Stuff!
