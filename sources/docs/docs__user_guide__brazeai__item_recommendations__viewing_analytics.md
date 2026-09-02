---
url: https://www.braze.com/docs/user_guide/brazeai/item_recommendations/viewing_analytics
slug: docs__user_guide__brazeai__item_recommendations__viewing_analytics
title: "Item recommendation analytics"
description: "Learn about item recommendation analytics and how to view them in Braze."
section: user_guide/brazeai
fetched: 2026-09-02
evidence: company-own (technical)
---
# Item recommendation analytics

Learn about item recommendation analytics and how to view them in Braze.

## View analytics

You can view analytics for your recommendation to see which items users were recommended and how accurate the recommendation model was.

- Go to Analytics > Item Recommendation.
 
- Select your recommendation from the list.

## Available metrics

### Audience

These metrics describe your recommendation audience. Depending on the recommendation type and available analytics data, the Audience section can include Precision and Coverage.

For AI Personalized recommendations, the Recommendation type card shows the estimated personalization rate, users with the configured event, and total population. For Most Recent recommendations, it shows the share of users receiving Most Recent recommendations versus the Most Popular fallback. Most Popular and Trending recommendations don’t show a user-level recommendation type breakdown.

Refer to the following table for more information:

 Metric | 
 Description | 

 Precision | 
 The percentage of time the model correctly guessed the next item a user purchased. Precision is heavily dependent on your specific catalog size and mix, and should be used as a guide to understand how often the model is correct.

In past testing, models have performed well with precision numbers ranging from 6-20%. This metric updates when the model next retrains. | 

 Coverage | 
 What percentage of available items in the catalog are recommended to at least one user. You can expect to see higher item coverage with personalized item recommendations over most popular ones. | 

 Personalization rate | 
 For AI Personalized recommendations, the estimated percentage of users with personalized recommendations stored on their profile, calculated against the total number of users who have performed the configured event in the past 24 months. Users who performed the event but don’t have enough data to generate a personalized recommendation receive most popular items as a fallback when messaged. | 

 Recommendation type | 
 For Most Recent recommendations, the percentage of users who receive Most Recent recommendations compared to the Most Popular fallback. | 

### Items

This table includes metrics about your personalized, most recent, and most popular items from your catalog.

Refer to the following table for more information:

 Metric | 
 Description | 

 Personalized items

Most recent items | 
 This column lists each item in the catalog in descending order of most often recommended to users. This column also shows how many users were assigned each item by the model.

Either Personalized or Most recent items will be listed depending on the recommendation type. | 

 Most Popular items | 
 This column lists each item in the catalog in descending order of popularity. Popularity here refers to items in the catalog that users interact with most often in the entire workspace. Most popular is used as the fallback when personalized or most recent cannot be calculated for an individual user. | 

### Overview

This is an overview of your chosen recommendation configuration, which includes when the recommendation was last updated.

- 

New Stuff!
