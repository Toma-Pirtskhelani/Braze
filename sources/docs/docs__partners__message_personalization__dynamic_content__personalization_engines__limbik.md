---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalization_engines/limbik
slug: docs__partners__message_personalization__dynamic_content__personalization_engines__limbik
title: "Limbik"
description: "This reference article outlines the partnership between Braze and Limbik, an AI resonance layer that predicts how audiences interpret and respond to messages using synthetic..."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Limbik

Limbik is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

This integration is maintained by Limbik.

## Prerequisites

The following are required to use Limbik with Braze:

 Requirements | 
 Description | 

 Limbik account_id | 
 Speak to your Limbik account team, or make a GET request to Limbik’s /rest/api/organizations endpoint | 

 Limbik access token (access_token) | 
 Make a POST request to Limbik’s login endpoint and use the returned access_token value as the Bearer token in the Authorization header. | 

 Braze REST API key | 
 A Braze REST API key with “Messages” permissions. Create one in the Braze dashboard under Settings > API Keys. | 

 Braze campaign_id | 
 Go to Messaging > Campaigns and select a campaign. If the campaign you want does not exist yet, create one and save it. At the bottom of the campaign page, find the Campaign API identifier. | 

Before using any of the forecast endpoints, you must first identify which organization (account_id) you have access to. While most customers have only one organization, some accounts may have multiple organizations available.

Retrieve available organizations

Query the organizations endpoint to retrieve your available organizations:

```

1
2
3

```
 | 
```
curl -X 'GET' \
 'https://cortex.prod.limbik.com/rest/api/organizations' \
 -H 'accept: application/json'

```
 | 

Example Response

```

1
2
3
4
5
6
7
8

```
 | 
```
{
 "data": [
 {
 "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
 "name": "Braze API"
 }
 ]
}

```
 | 

Select the uid from your desired organization to use as the account_id header in all subsequent API requests.

## Authentication

To access the API endpoints, you need a bearer token for authentication. Obtain your token by authenticating with your credentials.

Login request

```

1
2
3
4
5
6
7
8

```
 | 
```
curl -X 'POST' \
 'https://cortex.prod.limbik.com/rest/api/auth/login' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "username": "your_username",
 "password": "your_password"
}'

```
 | 

Example response

The response contains an access_token that you can use as the bearer token in all subsequent API requests:

```

1
2
3
4

```
 | 
```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
 "token_type": "Bearer"
}

```
 | 

Include this token in the Authorization header for all API requests:

```

1

```
 | 
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

```
 | 

note

You can use API platforms like Postman to set up automated workflows that call multiple REST API endpoints from different organizations, such as the following workflow.

## Use case - Generating message copy

By using both Braze and Limbik’s REST API endpoints, you can use Limbik’s generative forecasts to create message copy and send it through Braze messaging channels, or adjust existing copy to improve impact for your audience. Both platforms expose functionality you can call programmatically to build sophisticated workflows.

This documentation outlines two examples: generating message copy in Limbik and using this copy in a subsequent message sent through Braze, as well as using Limbik to score the quality of a given message for your chosen audience.

Limbik generative forecast request

Use this endpoint to generate a message and return it in a forecast template. Example request:

```

1
2
3
4
5

```
 | 
```
curl -X 'GET' \
 'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
 -H 'account_id: YOUR_ACCOUNT_ID' \
 -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
 -H 'accept: application/json'

```
 | 

Replace YOUR_PROMPT, YOUR_ACCOUNT_ID, and YOUR_ACCESS_TOKEN with your prompt text, organization ID (from the organizations endpoint), and bearer token from the login endpoint.

Example response

Example Limbik forecast template response:

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

```
 | 
```
[
 {
 "type": "Message",
 "displayText": "Formula one next race",
 "additionalDetail": "The latest dev in Formula...",
 "messages": [
 {
 "body": "The latest dev in Formula ..."
 }
 ],
 "population": {
 "id": 56,
 "name": "us2",
 "org_enabled": true,
 "org_visible": true,
 "categories": [],
 "display_name": "US Adults",
 "composite_key": "us2",
 "enabled": true
 }
 }
]

```
 | 

The key element for this use case is the additionalDetail field, which contains the message copy that Limbik generated.

Use this value to populate a message sent to Braze. For example, with the POST /campaigns/trigger/send endpoint, use additionalDetail to populate a payload field. With the POST /messages/send endpoint, use it to populate the message object of your choice.

### Response fields

The response contains the following key fields:

- type: The message type (for example, "Generate" for AI-generated content, "Message" for validated messages)
 
- displayText: A short title or summary of the message
 
- additionalDetail: The complete AI-generated message copy - This is the primary field containing the full message text that you can send through your messaging platform
 
- population: The target population and segments for this message

### Using with Braze

The additionalDetail field from Limbik’s response contains the message copy you send to Braze. One common integration pattern is to pass that value in the trigger_properties.payload when calling the Braze trigger send endpoint. In the following example, replace with the actual string from Limbik's `additionalDetail` field, and replace with your campaign ID.

### Braze trigger message request example

```

1
2
3
4
5
6
7

```
 | 
```
{
 "campaign_id": "",
 "trigger_properties": {
 "payload": ""
 },
 "broadcast": true
}

```
 | 

## Use case - Synthetic audience details

To build on the first use case, use Limbik’s endpoint /rest/api/populations/{account_id}/{population_id}.

This endpoint returns key data points that describe the makeup of Limbik’s synthetic audiences, such as gender, location, and so on. You can use these values to populate Connected Audience objects when calling Braze’s messaging endpoints.

note

Connected Audience objects cannot target users based on Braze’s “default” attributes, so you must store any attributes you want to target in Braze as custom attributes.

To obtain forecast scores for specific segments, identify the available countries and their corresponding segments.

### Step 1: List available countries

Retrieve the list of countries available for your account:

```

1
2
3

```
 | 
```
curl -X 'GET' \
 'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
 -H 'accept: application/json'

```
 | 

From the response, identify the country you want to use. For example, the United States has an id of 56.

### Step 2: Retrieve available segments

After you retrieve the country ID, retrieve the full list of segments for that country.

Example call

```

1
2
3

```
 | 
```
curl -X 'GET' \
 'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
 -H 'accept: application/json'

```
 | 

note

The response can be large. Cache this data (for example, in Redis) by name or key for better performance.

Example response

For example, to target females in the US adult population:

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

```
 | 
```
[
 {
 "id": 56,
 "name": "us2",
 "composite_key": "us2",
 "categories": [
 {
 "id": 9331,
 "name": "gender",
 "composite_key": "us2::gender",
 "segments": [
 {
 "id": 63793,
 "name": "female",
 "composite_key": "us2::gender::female"
 }
 ]
 }
 ]
 }
]

```
 | 

note

- Segments are specified using a simplified composite key format (for example, gender::female).
 
- The full composite key from the API response (us2::gender::female) is shortened to just the category and segment name.
 
- For a complete reference of available populations and segments, see Limbik audiences.

Using the composite key value for your chosen forecast message, you can map these synthetic audience descriptors to values on real user profiles in Braze.

For example, you can use the composite key (fr1::education_level::master_s_degree) in a Braze Connected Audience object as follows:

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

```
 | 
```
{
 "AND": [
 {
 "custom_attribute": {
 "custom_attribute_name": "education_level",
 "comparison": "equals",
 "value": "masters"
 }
 }
 ]
}

```
 | 

## Use case - Evaluating forecast score

You can use Limbik to create an estimated score for a message against a synthetic audience. Do this programmatically with Limbik’s forecasts/synchronous endpoint.

### Option 1 - Synchronous forecast

You can use the response payload from the template generation directly with the synchronous forecast endpoint:

Example generic request

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

```
 | 
```
curl -X 'POST' \
 'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
 -H 'accept: application/json' \
 -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
 -H 'Content-Type: application/json' \
 -d '{
 "type": "Generate",
 "displayText": "Formula one season testing 2026",
 "additionalDetail": "Day 1 of the 2026 Formula 1 Bahrain testing session has concluded. Lando Norris recorded the fastest time in the McLaren, with Ferrari in second place. Cadillac drivers Sergio Perez and Valtteri Bottas completed 107 laps, nearly two race distances, and Audi introduced significant upgrades. Which team do you expect to perform best in Australia? #F12026 #BahrainTesting #LandoNorris",
 "population": {
 "population": "us2",
 "segments": []
 }
}'

```
 | 

Example response (abbreviated)

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

```
 | 
```
{
 "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
 "datetime": "2026-02-11T20:04:06.545+00:00",
 "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
 "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
 "name": "Formula one season t...",
 "user_message_context": "",
 "population": [
 {
 "name": "us2",
 "display_name": "US Adults",
 "categories": []
 }
 ],
 "privacy_compliant": false,
 "model_outputs": {
 "belmetrics": {
 "metrics": {
 "moe": 0.02144,
 "pfi": "0.3611",
 "min_val": 0.2941,
 "mean_val": 0.41831
 }
 },
 "virmetrics": {
 "metrics": {
 "moe": 0.02381,
 "pfi": "0.3611",
 "min_val": 0.2,
 "mean_val": 0.30395
 }
 },
 "model_variant": "v4_0_0"
 }
}

```
 | 

### Option 2: Prepare forecast payload with segments

Create your forecast payload using the selected segments. Segments use a simplified composite key format.

Example segment-specific request

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

```
 | 
```
{
 "type": "Generate",
 "displayText": "Formula one season testing 2026",
 "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
 "population": {
 "population": "us2",
 "segments": [
 "gender::female"
 ]
 }
}

```
 | 

- 

New Stuff!
