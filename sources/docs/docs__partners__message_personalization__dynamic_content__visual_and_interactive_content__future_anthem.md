---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/future_anthem
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__future_anthem
title: "Future Anthem"
description: "This reference article outlines the partnership between Braze and Future Anthem, a real-time AI platform for sports betting and iGaming personalization."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Future Anthem

The Future Anthem real-time AI platform powers personalization across sports, casino, bingo, and lottery. Braze customers can enrich player profiles with industry-specific attributes, including favorite game, favorite team, engagement score, next bet recommendation, expected next bet, and more.

Delivered through Real-time Experiences, Dynamic Audiences, and Content Recommendations, every attribute is built on live player behavior, so Braze customers can act in the moment.

This integration is maintained by Future Anthem.

important

This feature is currently in early access. Contact the Future Anthem Customer Success team to get started.

## Prerequisites

 Requirement | 
 Description | 

 Future Anthem account | 
 A Future Anthem account. | 

 Braze REST API key | 
 A Braze REST API key with permission for the users.track endpoint. You can create this in the Braze dashboard from Settings > API Keys. | 

 Braze REST endpoint | 
 The Braze REST endpoint that matches your instance, such as rest.iad-01.com. | 

## Use cases

With this integration, you can:

- Identify players with high engagement scores and target them with personalized offers, such as exclusive promotions or VIP rewards.
 
- Suggest similar games based on the games a player already likes.

## Integration

The Future Anthem Customer Success team helps you set up your integration. Contact your Future Anthem Customer Success contact, and they help you identify the most relevant attributes to send to Braze.

 Example attributes in Future Anthem | 
 Example attributes in Braze | 

 | 
 | 

## Braze custom attributes

These are the available Braze custom attributes. For more information, see Future Anthem: Getting Started.

- bet recommendations
 
- bonus recommendations
 
- game recommendations
 
- player cluster
 
- player sustain (player potential risk)

 Subcategory | 
 Example (JSON) | 
 Data type | 

 User preferences | 
 {"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"} | 
 Object | 

 Single bet recommendations | 
 {"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"} | 
 Object | 

 Accumulator bet recommendations (event labels) | 
 {"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"} | 
 Object | 

 Accumulator bet recommendations (numeric odds) | 
 {"Bet_1": 1.5, "Bet_2": 2} | 
 Object | 

 Bet Builder bet recommendations | 
 {"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"} | 
 Object | 

 Subcategory | 
 Example | 
 Data type | 

 NGR (net gaming revenue, lifetime) | 
 2232 | 
 Number | 

 NGR14 (net gaming revenue, last 14 days of activity) | 
 42 | 
 Number | 

 Player profitability score | 
 130 | 
 Number | 

 Engagement score | 
 0.78 | 
 Number | 

 Churn risk score | 
 0.02 | 
 Number | 

 Estimated next bet date | 
 2024-08-29 | 
 Time | 

 Bet and Get bonus value recommendation | 
 20 | 
 Number | 

 Other bonus value recommendations | 
 0 | 
 Number | 

 Future CLTV | 
 3126 | 
 Number | 

 Subcategory | 
 Example | 
 Data type | 

 Recommended For You | 
 Fluffy Favourites, Fishin’ Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | 
 Array | 

 Favorite games | 
 Fishin’ Frenzy | 
 Array | 

 Recommended new games | 
 Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | 
 Array | 

 Players like you are playing (collaborative filtering) | 
 Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O’ the Irish | 
 Array | 

 Because you played (game similarity) | 
 Fluffy Favourites 2, Luck O’ the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | 
 Array | 

 Up Next (game sequencing) | 
 Fishin’ Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin’ Bigger Pots of Gold | 
 Array | 

 Popular games | 
 Temple of Iris, Fishin’ Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | 
 Array | 

 Trending games | 
 Pig Banker, Hyper Gold, Pyramid King, Gold Cash | 
 Array | 

 Subcategory | 
 Example | 
 Data type | 

 Showcase what cluster the player is in | 
 High Value Game Diverse | 
 String | 

 Subcategory | 
 Example | 
 Data type | 

 Risk score | 
 0.5 | 
 Number | 

 Risky player | 
 True | 
 Boolean | 

- 

New Stuff!
