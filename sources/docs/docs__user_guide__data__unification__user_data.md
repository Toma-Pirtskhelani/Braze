---
url: https://www.braze.com/docs/user_guide/data/unification/user_data
slug: docs__user_guide__data__unification__user_data
title: "User data in Braze"
description: "This landing page is home to articles on user data collection. Here, you can find resources on archival definitions, importing users, the user profile lifecycle,..."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# User data in Braze 

Before completing your Braze implementation, ensure that you have a conversation between your marketing team and your development team about your marketing goals. It’s useful to consider those goals and work backwards from them when deciding what data to track, and how to track that data with Braze.

## Section articles 

- 

 SDK data collection

- 

 User profile lifecycle

- 

 Collection use case

- 

 Collection best practices

- 

 Import users

- 

 Delete users

- 

 Anonymous users

- 

 Language codes

important

Braze blocks user profiles (“dummy users”) with more than 5,000,000 sessions, more than 20,000 distinct custom event names, or more than 20,000 distinct product names in purchases, because they’re usually the result of misintegration. After a profile is blocked, Braze stops ingesting all inbound data for that profile, from both the SDKs and the REST API. If you find that this has happened for a legitimate user, contact your Braze account manager.

- 

New Stuff!
