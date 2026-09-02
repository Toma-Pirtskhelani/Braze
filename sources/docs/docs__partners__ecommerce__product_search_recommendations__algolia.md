---
url: https://www.braze.com/docs/partners/ecommerce/product_search_recommendations/algolia
slug: docs__partners__ecommerce__product_search_recommendations__algolia
title: "Algolia"
description: "Learn how to use Algolia with Braze Connected Content to dynamically deliver personalized search results and product recommendations in your Braze messages."
section: partners/ecommerce
fetched: 2026-09-02
evidence: company-own (technical)
---
# Algolia

Algolia is a search and discovery platform that helps developers build fast, relevant, and scalable search experiences. With a powerful API-first approach, Algolia combines advanced ranking algorithms with AI-driven insights for seamless site search, navigation, and personalized content discovery.

The Algolia and Braze integration uses Connected Content to populate Algolia-powered search results and product recommendations in your Braze messages. By querying Algolia’s API at send time, you can deliver personalized content that drives users to high-conversion product detail or landing pages.

## Use cases

- Promote trending products: Automatically pull trending or top-performing products from Algolia into Braze messages to promote high-interest items and increase engagement.
 
- Personalize campaigns with search intelligence: Personalize Braze campaigns using Algolia search and browsing intelligence to deliver products or categories aligned with each user’s interests.

## Prerequisites

 Requirement | 
 Description | 

 Algolia account | 
 An Algolia account is required to take advantage of this partnership. | 

 Algolia API credentials | 
 Your Algolia API key and Application ID. | 

 Algolia product index | 
 An Algolia index populated with your product data. This is required to use the Search or Recommend APIs. | 

## Integration

### Step 1: Set up your Algolia API request

For more information about request formats, response structures, and usage, refer to the Algolia Search API and Algolia Recommend API documentation. If you need assistance with setup, contact the Algolia team.

- search api
 
- recommend api

#### Example Search API request

```

1
2
3
4

```
 | 
```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}

```
 | 

#### Example query payload

```

1
2
3
4
5
6

```
 | 
```
{
 "query": "",
 "hitsPerPage": 4,
 "filters": "category_page_id:'this week's offers'",
 "attributesToRetrieve": ["name", "price", "image", "url"]
}

```
 | 

In this example, the query retrieves the top four results from a page that uses a category filter based on an attribute called category_page_id. The attributesToRetrieve parameter limits the response to keep the payload at a manageable size.

Example use case: To feature search results from https://www.yoursite.com/weekly-offers in a weekly offers Braze campaign, query the corresponding Algolia index and apply filters to retrieve the top results from that page.

tip

Retrieve additional fields using attributesToRetrieve to enhance personalization, such as ratings, reviews, or discounts.

#### Example Recommend API request

```

1
2
3
4

```
 | 
```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}

```
 | 

#### Example query payload

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

```
 | 
```
{
 "requests": [
 {
 "indexName": "prod_ECOM",
 "model": "trending-items",
 "threshold": 40,
 "maxRecommendations": 4
 }
 ]
}

```
 | 

The Recommend API supports multiple models, including Frequently Bought Together, Related Products, Trending Items, Trending Facet Values, and Looking Similar. This example uses the Trending Items model.

important

If your recommendations rely on user-specific attributes or objectIDs, be mindful of the rate limits defined in your Algolia contract. Refer to the Considerations section for best practices.

### Step 2: Implement Braze Connected Content

Use Braze’s Connected Content feature to make API calls to Algolia endpoints and dynamically inject the response into a message. For more information about configuration, request formatting, and best practices, refer to Connected Content.

- search api
 
- recommend api

#### Example Connected Content Search request

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
{% capture request_body %}
{
 "query": "",
 "hitsPerPage": 4,
 "filters": "category_page_id:'this week's offers'",
 "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
 :method post
 :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
 :body {{request_body}}
 :save algolia_search
%}

```
 | 

#### Example Connected Content Recommend request

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

```
 | 
```
{% capture request_body %}
{
 "requests": [
 {
 "indexName": "prod_ECOM",
 "model": "trending-items",
 "threshold": 40,
 "maxRecommendations": 4
 }
 ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
 :method post
 :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
 :body {{request_body}}
 :save algolia_recommendations
%}

```
 | 

### Step 3: Format search results in Braze messages

After fetching results from Algolia, use Liquid to parse the API response and dynamically render the results within your message.

- search api
 
- recommend api

#### Example Liquid email template for Search API

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
{% for item in algolia_search.hits %}
 <div style="margin-bottom: 10px;">
 <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
 <p><strong>{{ item.name }}</strong></p>
 <p>Price: ${{ item.price }}</p>
 <a href="{{ item.url }}">View Product</a>
 </div>
{% endfor %}

```
 | 

This generates a list of products from the Search API results inside the message body. Each product link directs users to a product detail page (PDP) or a campaign-specific landing page.

#### Example Liquid email template for Recommend API

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
{% for item in algolia_recommendations.hits %}
 <div style="margin-bottom: 10px;">
 <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
 <p><strong>{{ item.name }}</strong></p>
 <p>Price: ${{ item.price }}</p>
 <a href="{{ item.url }}">View Product</a>
 </div>
{% endfor %}

```
 | 

This generates a list of recommended products from the Recommend API results inside the message body. Each product link directs users to a product detail page (PDP) or a campaign-specific landing page.

## Considerations

### Avoiding unique queries

Be mindful of the Algolia rate limits defined in your contract. Avoid making user-specific queries, as these can quickly exceed your allotted requests. To personalize results, target a segment instead of an individual user ID, or filter by category or brand instead of a specific objectID. Use Braze attributes to further personalize the recommendations.

### Caching Connected Content results

Cache Connected Content results using cache_max_age to minimize API requests to Algolia and improve performance. For more information, refer to Caching responses.

- 

New Stuff!
