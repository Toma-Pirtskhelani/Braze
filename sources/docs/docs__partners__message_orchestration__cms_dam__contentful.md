---
url: https://www.braze.com/docs/partners/message_orchestration/cms_dam/contentful
slug: docs__partners__message_orchestration__cms_dam__contentful
title: "Contentful"
description: "This reference article outlines the partnership between Braze and Contentful, a content management system that allows you to dynamically use Connected Content to pull content..."
section: partners/message_orchestration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Contentful

Contentful is a headless content management system that lets you create, manage, and distribute content to any platform. Unlike a content management system (CMS), Contentful allows you to create your content model so you can decide which content you want to manage.

This page provides a step-by-step guide to configure Braze Connected Content to fetch data from Contentful’s Content Delivery API.

After you’re integrated, you can use Contentful’s RESTful APIs to deliver your content across multiple channels, such as websites, mobile apps (iOS, Android, and Windows), or many other platforms. You can also dynamically pull content from Contentful for use in your Braze campaigns.

## Prerequisites

Before you start, you’ll need the following:

 Requirements | 
 Description | 

 A Contentful account | 
 You need a Contentful account with access to the Content Delivery API. | 

 A Braze account | 
 You need a Braze account with access to the Connected Content feature. | 

## Integration

### Step 1: Get your Contentful API credentials

- Log into Contentful with your credentials.
 
- Create or retrieve API access tokens in the Contentful dashboard by going to Settings > API keys. If you don’t already have an API key, create a new one:
2.1 Select Add API key.
2.2 Enter the required details and select the appropriate environment.
2.3 Select Save and note the Space ID and Content Delivery API - access token.
 
- Identify the content model you want to access through the Contentful API.

### Step 2: Configure Braze Connected Content

- Log into Braze with your credentials.
 
- In the Braze dashboard, go to Content > Content Block > Create Content Block > HTML code editor.
 
- Create a Connected Content request to Contentful’s Contentful Content Delivery API URL. An example Contentful Content Delivery API URL is https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries.

 Retrieving different assets requires including specific variables. The example Connected Content URL request targets Contentful’s Entry endpoint. This endpoint needs variables like {space_id} and {environment_id}, or {entry_id} and {access_token}. These can be taken from your Contentful instance. In this example Content Block, the variables must be replaced with your Contentful Space ID and Environment ID.

The example Content Delivery API URL uses only one of Contentful’s available endpoints. Different use cases may be achieved by leveraging different URLs. For example, the Image API can be used to capture images stored in Contentful. For more information, review Content Delivery API.

note

Different endpoints may require new variables, for instance the Images API requires an {asset_id}, {unique_id}, and {name}. For further guidance, contact Contentful.

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
11
12
13
14
15

```
 | 
```
 {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
 {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
 {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
 {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
 {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
 {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
 {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
 {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
 {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
 :method get
 :headers {
 "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
 }
 :content_type application/json
 :save response %}

```
 | 

- Use “Test Endpoint” to test that Braze can successfully connect to the Contentful API and retrieve the desired data.
 
- Select Done to save your Content Block.
 
- Give your Content Block a descriptive name, such as “Contentful API”, then select Launch Content Block.

### Step 3: Use Connected Content in campaigns and Canvasses

- In Braze, create a new campaign or edit an existing one.
 
- Use the Connected Content block to insert data fetched from Contentful. Use the data paths you defined during the configuration to dynamically populate campaign content.

- Response path: After including the Content Block in a Braze Campaign or Canvas, the response becomes available when you insert the variable {response} into your message.

JSON dot notation allows you to specify what part of the response body from Contentful you want to include in your message. This will vary based on your use case. For example, you can use the title value (liquid{{response.items[0].fields.title}}) from Contentful’s Entry endpoint and receive a response like this:

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43

```
 | 
```
 {
 "fields": {
 "title": {
 "en-US": "Hello!"
 },
 "body": {
 "en-US": "This is a sample message!"
 }
 },
 "metadata": {
 "tags": [
 {
 "sys": {
 "type": "Link",
 "linkType": "Tag",
 "id": "nyCampaign"
 }
 }
 ]
 },
 "sys": {
 "id": "5KsDBWseXY6QegucYAoacS",
 "type": "Entry",
 "version": 1,
 "space": {
 "sys": {
 "type": "Link",
 "linkType": "Space",
 "id": "yadj1kx9rmg0"
 }
 },
 "contentType": {
 "sys": {
 "type": "Link",
 "linkType": "ContentType",
 "id": "hfM9RCJIk0wIm06WkEOQY"
 }
 },
 "createdAt": "2016-12-20T10:43:35.772Z",
 "updatedAt": "2016-12-20T10:43:35.772Z",
 "revision": 1
 }
}

```
 | 

- Preview and test your campaign to confirm that the Connected Content data displays correctly.
 
- After you’re satisfied with the setup, launch your campaign.

## Troubleshooting

### API response

Make sure that your Contentful API credentials and endpoint URL are correct. Check for any error messages in Braze that might indicate issues with the API call.

### Data mapping

Verify that the response path mappings are correctly configured and that the API response structure matches your expectations.

## Additional resources

- Contentful Content Delivery API documentation
 
- Braze Connected Content
 
- Braze Content Blocks

- 

New Stuff!
