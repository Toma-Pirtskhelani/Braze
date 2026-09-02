---
url: https://www.braze.com/docs/partners/data_and_analytics/reverse_etl/hightouch/hightouch_personalization_api
slug: docs__partners__data_and_analytics__reverse_etl__hightouch__hightouch_personalization_api
title: "Hightouch Personalization API"
description: "This reference article outlines the integration between Braze and Hightouch's Personalization API, a managed service for hosting a low-latency data API based on any dataset..."
section: partners/data_and_analytics
fetched: 2026-09-02
evidence: company-own (technical)
---
# Hightouch Personalization API

Hightouch’s Personalization API is a managed service that lets you host a low-latency data API based on any dataset in your cloud data warehouse.

The Braze and Hightouch integration allows you to use the API with Braze Connected Content to pull up-to-date customer or object data into your campaigns or Canvases at the time-of-send.

Hightouch’s Personalization API provides a REST endpoint to use within your Braze configuration. Specifically, you can use the Braze Connected Content offering to make a GET request to the Personalization API to retrieve all information related to a particular identifier. The data exposed by this API could represent customer, product, or any other object data.

## Prerequisites

 Requirement | 
 Description | 

 Hightouch account with Personalization API enabled | 
 A Hightouch Business Tier account is required to take advantage of this partnership. | 

 Defined use cases | 
 Before setting up the API, you must determine your use case for this integration. Reference the following list for common use cases. | 

 Data stored in a cloud data warehouse or other source | 
 Hightouch integrates with over 25+ data sources | 

 Hightouch API key | 
 This can be created within Hightouch > Settings > API keys > Add API key. | 

- use cases
 
- datasets

### Use Cases

Before getting started, it’s helpful to plan exactly how you want to use the personalization API.

Common use cases include:

- Product recommendations to streamline embedding personalized product recommendations in email templates, campaigns, or in-app experiences
 
- Powering personalized marketing campaigns by enriching marketing touchpoints with dynamic product recommendations
 
- Delivering in-app or web personalization, for example, customized search results, cohort-based pricing, and messaging, article recommendations, or nearest-store locations
 
- Recommendations based on financial or medical data—financial data has stringent requirements that Hightouch meets via its strict data security policies. With Hightouch, you can create customer segments based on financial or medical data without exposing the underlying attributes used in your segmentation criteria.

### Datasets

The Personalization API acts as a cache for selected data in your warehouse, so you should already have the recommendation data stored there. You can use Hightouch to transform it according to a template if necessary. This type of data includes:

- User metadata such as geographic region, age, or other demographic information
 
- User actions or events, including past purchases, page views, clicks, etc.

## Integration

### Step 1: Connect data source to Hightouch

Hightouch sources are where your organization’s business data lives. In this case, it’s wherever your user data is stored.

- In Hightouch, go to Sources Overview > Add Source. Select your data warehouse as the source.

- Enter the relevant credentials; these will differ depending on the source.

For further details, refer to the relevant source documentation.

### Step 2: Model data

Hightouch models define what data to pull from your source. To set up a new model, follow these steps:

- In Hightouch, go to Models overview > Add model, and select the source you just connected. 

- Next, choose a modeling method. Because all your information should be joined in one table, you can use the visual table selector to define it. Alternatively, you can write SQL to include only the columns you want or rely on your existing dbt models, Looker Looks, or Sigma workbooks.

- Before continuing, preview your model to ensure it’s querying the data you’re interested in. By default, Braze limits the preview to the first 100 records. After you’ve validated your data, click Continue.

- Name your model, for example, “User recommendations.”

- Lastly, select a primary key and click Finish. A primary key should be a column with unique identifiers. This is also the field you’ll use to call the personalization API to retrieve a particular user’s recommendations.

### Step 3: Configure personalization API

Preparing the API to receive requests has two steps:

- Enabling the personalization API in the regions closest to your infrastructure
 
- Creating syncs to define which models should be materialized in the Hightouch-managed cache

Follow these instructions to complete both:

- In Hightouch, go to Destinations and select the Hightouch personalization API created for you. If you don’t have this destination enabled, contact Hightouch support.

- Next, select the appropriate region. Selecting the region closest to your infrastructure will reduce your response times. If you don’t see a region close to your infrastructure, contact Hightouch support.

- Go to the Syncs overview page and click the Add sync button. Next, select the relevant model and the destination you previously set up.

- Enter an alphanumeric collection name. Collections are conceptually similar to database tables. Each should represent a particular data type, such as customers or invoices. Collection names must be alphanumeric and will become part of your Personalization API endpoint.

- Next, specify which column from your model should serve as the primary index for record lookups. This field must uniquely identify each record in the collection and is often the same as your model’s primary key. The personalization API supports lookups on multiple indices. For example, you might want to retrieve customer profiles using user_id, anonymous_id, or email_address. To enable multiple indices, contact Hightouch support.

- Use the field mapper to specify which columns from your model should be included in the API response payload. You can rename these fields and use the advanced mapper to apply transformations using the Liquid template language.

- Select the appropriate delete behavior for your use case.

- Lastly, click Continue and then select a sync schedule.

Hightouch will now sync the data in your warehouse to a managed database and expose it via the Personalization API.

### Step 4: Call personalization API through Braze Connected Content

Once you’ve set up your personalization API instance, you can use it as a Braze Connected Content endpoint.

The API is accessible at https://personalization.{region}.hightouch.com, for example, https://personalization.us-west-2.hightouch.com.

The information is available using this endpoint /v1/collections/:collection_name/records/:index_key/:index_value.

For example, you could include this snippet in a campaign or Canvas:

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

```
 | 
```
{% connected_content
 https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
 :method get
 :headers {
 "Authorization": "Bearer {{YOUR-API-KEY}}"
 }
 :content_type application/json
 :save customer
%}

```
 | 

You can use Liquid templating to reference the properties returned in the JSON payload and use them in your messaging.

For the following example payload:

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

```
 | 
```
{
 "user_id": 12345,
 "full_name": "Alex Smith",
 "lifetime_value": 1492.18,
 "churn_risk": 0.04,
 "90_day_summary": {
 "num_songs_listened": 813,
 "top_genres": [
 "house",
 "techno",
 "ambient"
 ],
 "top_artists": [
 "deadmau5",
 "Marsh",
 "Enamour"
 ]
 },
 "recommendations": {
 "concerts": [
 {
 "artist": "Aphex Twin",
 "location": "San Francisco, CA",
 "event_date": "2023-01-31"
 },
 {
 "artist": "Sultan + Shepard",
 "location": "San Francisco, CA",
 "event_date": "2023-02-25"
 }
 ],
 "upcoming_album_release": {
 "title": "Universal Language",
 "artist": "Alex Lee",
 "label": "Anjunadeep",
 "release_date": "2023-04-28"
 }
 }
}

```
 | 

The following Liquid references would return this example data:

 Liquid template | 
 Returned example | 

 {{artists.recommendations.concerts[0].artist}} | 
 Aphex Twin | 

 {{artists.recommendations.concerts[0].location}} | 
 San Francisco, CA | 

 {{artists.recommendations.upcoming_album_release.title}} | 
 Universal Language | 

## Troubleshooting

If you have questions, contact Hightouch support for assistance.

- 

New Stuff!
