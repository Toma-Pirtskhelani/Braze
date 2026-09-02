---
url: https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization
slug: docs__user_guide__messaging__messaging_fundamentals__localization
title: "Localization"
description: "This reference article covers the basics of localization, lists the benefits of different orchestration approaches across campaigns and Canvases, and lists different ways users can..."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Localization

For companies with customers in many countries, handling localization early in your Braze journey can save your companies time and resources.

## How it works

Locale information is stored on a user’s profile based on data you collect using a Braze SDK (automatically), or REST API. The locale contains the language and a region identifier. This information is available in the Braze segmentation tool under Country and Language.

tip

For technical details on how locale is collected by our SDKs, refer to the official iOS, Android, and Web documentation.

## Translation management

Consider the following approaches for managing your translations.

- campaign
 
- canvas

### One template for all

In this approach, localization is applied to a single template in Braze using Liquid. After sending, the dashboard provides aggregated campaign analytics. User-level engagement can be measured using custom segment funnels, for example, by combining Country and Received Campaign filters.

 Advantages | 
 Considerations | 

 - Centralized approach
- Reduced email build time, no need to build out an email multiple times | 
 - Manual report building
- Campaign report shows aggregated metrics rather than metrics per country
- Need to thoroughly test Liquid to ensure it populates as expected
- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country
- Harder to schedule sends for specific times across time zones
- Harder to use if you want to send separate content per country. | 

### One template per country

This approach separates templating into different sending locales. After sending, the dashboard reports sending analytics based on each country separately, and any downstream user-level Currents events will also be tied to a specific campaign.

- Templates benefit from implementing tags for maintenance and tracking purposes.
 
- Campaigns can inherit the configurations from the same Braze template and Content Blocks (such as email templates that contain Liquid).
 
- Pre-existing campaigns and templates can be duplicated to allow a faster time time-to-value.

 Advantages | 
 Considerations | 

 - Scalable to multiple locations
- Reporting on revenue per country within Braze (such as per campaign)
- Flexibility if there is drastically different content per country | 
 - Requires strategic structuring
- More build effort required (such as separate campaigns for each country) | 

### One journey for all

In this approach, localization is handled within Canvas basics and Liquid to define messaging for each user.

After a Canvas is sent, the dashboard provides aggregated Canvas Analytics, whereas the user level engagement can be measured via custom segment funnels, such as combining Country and Received Canvas Step filters.

 Advantages | 
 Considerations | 

 - Centralized approach
- Reduced email build time - no need to build out an email multiple times. | 
 - Manual report building
- Canvas report shows aggregated metrics rather than metrics per country
- Need to thoroughly test Liquid to ensure it populates as expected
- Depending on how you pull in the country value or how many counties you have set up, it could be tricky to test each country
- Harder to schedule sends for specific times across time zones
- Harder to use if you want to send separate content per country. | 

### One journey per country

In this approach, the Canvas journey builder provides the flexibility of creating user journeys via multiple Canvas components. These components can be duplicated at the component and overall journey level.

Localization can be achieved with the following methods:

- Separate Canvases per country, this ensures the complex user journeys are defined at the top of the funnel using audience filters
 
- Bespoke user journeys per country, the implementation of Audience Paths to intuitively segment users on a large scale for each journey by creating separate message threads for each country in a single Canvas

Once sent, the dashboard provides dynamic analytics per country and within user-level Currents events based on the customer’s current location.

 Advantages | 
 Considerations | 

 - Reporting on revenue per country within Braze (such as per Canvas, variant, or step)
- Flexibility if there is drastically different content per country
- Can add other channels as part of the journey in the future | 
 - Requires strategic structuring
- More build effort required (such as separate message steps for each country)
- Canvas can become large and difficult to read if you have custom, complex journeys for each country in a single Canvas. | 

## Sending translated messages

To send personalized messages based on a user’s language, locale, or custom attributes, use one of the following methods.

### Translation Liquid tags (recommended)

Braze supports a {% translation salutation %}Hello!{% endtranslation %} Liquid tag to target users in different languages with a single message.

For a full walkthrough, refer to the guide on using translation tags.

### Alternative approaches

- custom liquid
 
- content blocks
 
- catalogs
 
- braze partners
 
- spreadsheets

You can manually paste your content into the body of your message and use Liquid to conditionally display the correct language to the recipient. To do this:

- Compose your message, then select Language to generate Liquid conditional logic for each of your selected languages.
 
- 
 
You can use the following Liquid template to help build out your message. For each field with templating, you should enter the variations after the bracketed segment of templating. The variation should correspond to the language code referenced in the brackets before it.

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
 {% if ${language} == 'en' %}
 This is a message in English from Braze!
 {% elsif ${language} == 'es' %}
 Este es un mensaje en español de Braze !
 {% elsif ${language} == 'zh' %}
 这是一条来自Braze的中文消息。
 {% else %}
 This is a message from Braze! This will go to anyone who does not match the other specified languages!
 {% endif %}

```
 | 

- Test your message before sending it by entering a user’s ID or email to check how a message would appear to an individual depending on their language.

tip

We always recommend including a {% else %} statement in your messaging. While most users will see messaging for their specific language, the text will be visible to those that:

- Do not have a language selected
 
- Have a language that Braze does not support
 
- Have a device where the language is undetectable

Braze Content Blocks are reusable blocks of content. When a block is changed, all references to that block changes. For example, updates to an email header or footer will be reflected in all emails or to house translations. These blocks can also be created and updated using the REST API, and users can programmatically upload translations.

When building a campaign in the dashboard, Content Blocks can be referenced using tag {{content_blocks.${name_of_content_block}}}. These blocks could contain all translations housed within conditional logic for each language, as shown in option 1, or a separate block for each language can be used.

Content Blocks can also be utilized as a translation management process where content that requires translation is housed within a Content Block, fetched, translated, and then updated:

- Manually create a Content Block in the dashboard with the tag “Needs Translation”.
 
- Your service performs a nightly fetch of all Content Blocks using the /content_blocks/list endpoint.
 
- Your service fetches details on each Content Block through the /content_blocks/info endpoint to see which blocks are tagged for translation.
 
- Your translation service translates the body of all “Needs Translation” Content Blocks.
 
- Your service hits the /content_block/update endpoint to update translated content and update the tag to “Translation Complete”.

Catalogs allow you to access data from imported JSON objects via API and CSV files to enrich your messages, similar to custom attributes or custom event properties through Liquid. For example:

- api
 
- csv

Create a catalog via the following API call:

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

```
 | 
```
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
 {
 "name": "translations",
 "description": "My localization samples",
 "fields": [
 {
 "name": "id",
 "type": "string"
 },
 {
 "name": "context",
 "type": "string"
 },
 {
 "name": "language",
 "type": "string"
 },
 {
 "name": "body",
 "type": "string"
 }
 ]
 }
 ]
}'

```
 | 

Add items via the following API call:

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

```
 | 
```
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
 {
 "id": "1",
 "context": "1",
 "language": "en",
 "body": "Hey"
 },
 {
 "id": "2",
 "context": "1",
 "language": "es",
 "body": "Hola"
 },
 {
 "id": "3",
 "context": "1",
 "language": "pt",
 "body": "Oi"
 },
 {
 "id": "4",
 "context": "1",
 "language": "de",
 "body": "Hallo"
 }
 ]
}'

```
 | 

Create a CSV in the following format:

 id | 
 context | 
 language | 
 body | 

 1 | 
 1 | 
 en | 
 Hey | 

 2 | 
 1 | 
 es | 
 Hola | 

 3 | 
 1 | 
 pt | 
 Oi | 

 4 | 
 1 | 
 de | 
 Hallo | 

 5 | 
 2 | 
 en | 
 Hey | 

 6 | 
 2 | 
 es | 
 Hola | 

 7 | 
 2 | 
 pt | 
 Oi | 

 8 | 
 2 | 
 de | 
 Hallo | 

 9 | 
 3 | 
 en | 
 Hey | 

 10 | 
 3 | 
 es | 
 Hola | 

 11 | 
 3 | 
 pt | 
 Oi | 

 12 | 
 3 | 
 de | 
 Hallo | 

These catalog items can them be referenced using personalization, shown in the following example, or selections that allow you to create groups of data.

```

1
2
3

```
 | 
```
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”

```
 | 

Many Braze partners offer localization solutions, including Transifex and Crowdin. Typically users use the platform alongside an internal team and translation agency. These translations are then uploaded there and are then accessible via REST API. These services also often leverage Connected Content, allowing users to fetch the translations via API.

For example, the following Connected Content calls call Transifex and Crowdin to fetch a translation, leveraging {{${language}}} to identify the correct translation for a given user. This translation is then saved in the JSON block “strings” and referenced.

- transifex example
 
- crowdin example

```

1
2

```
 | 
```
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}

```
 | 

```

1
2

```
 | 
```
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}

```
 | 

Host translations in a spreadsheet, then use one of the following methods to send your message in the relevant language.

- connected content
 
- json api via sheetdb
 
- json api via sheetlabs

You can with a translation agency to store translations in a Google spreadsheet, then query this content using Braze Connected Content. When you send a message, the relevant translation for each user will be pulled into your campaign body based on their selected language.

note

The Google Sheets API has a limit of 500 requests per 100 seconds per project. Connected Content calls can be cached, but this solution is not scalable for a high-traffic campaign.

This option provides an alternative method of transforming Google Sheets into JSON objects queried via Connected Content. By turning a spreadsheet into a JSON API via SheetDB, you can choose from multiple subscription tiers depending on the cadence of the API calls.

The spreadsheet structure follows the steps in option 4, but SheetDB also provides additional filters to query the objects.

Some users may prefer to implement SheetDB with fewer Liquid and Connected Block dependencies by implementing SheetDB’s search method in GET request calls to filter the JSON objects based on {{${language}}} Liquid tag to automatically return the results for a single language rather than building large conditional blocks.

#### Step 1: Format the Google sheet

First, build out the Google sheet so that the languages are different objects:

 language | 
 title1 | 
 body1 | 
 title2 | 
 body2 | 

 en | 
 Hey | 
 1 | 
 Hey2 | 
 5 | 

 es | 
 Hola | 
 2 | 
 Hola2 | 
 6 | 

 pt | 
 Oi | 
 3 | 
 Oi2 | 
 7 | 

 de | 
 Hallo | 
 4 | 
 Hallo2 | 
 8 | 

#### Step 2: Use the language Liquid tag in a Connected Content call

Next, implement the {{${language}}} Liquid tag within a Connected Content call. Note that SheetDB will auto-generate the sheet_id upon creating the spreadsheet.

```

1

```
 | 
```
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}

```
 | 

#### Step 3: Template your messages

Lastly, use Liquid for templating your messages:

```

1
2

```
 | 
```
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”

```
 | 

##### Considerations

- The {{${language}}} field has to be defined for all users; otherwise, a Liquid conditional block has to be featured as a fallback handler for users without a language.
 
- Data modeling within Google Sheets has to follow a different language-driven vertical as opposed to having message objects.
 
- SheetDB offers a limited free account and multiple paying options that should be considered based on your campaign strategy.
 
- Connected Content calls can be cached. We recommend measuring the projected cadence of the API calls and investigating an alternative approach of calling the main SheetDB endpoint instead of using the search method.

This option turns a Google Sheet into a JSON API you can query with Connected Content. Sheetlabs supports large query volumes and offers free and paid tiers.

#### Step 1: Prepare your translations sheet in Google Sheets

Build the Google Sheet so each row is a language. For example:

 language | 
 greeting | 
 title1 | 
 legal1 | 

 en | 
 Welcome! | 
 Your exclusive offer is here | 
 … | 

 fr | 
 Bienvenue! | 
 Votre offre exclusive est arrivée | 
 … | 

#### Step 2: Use Sheetlabs to import the sheet and create an API

- Sign up at Sheetlabs.
 
- Follow the Sheetlabs instructions to import data from Google Sheets.
 
- Select the spreadsheet you created in step 1.
 
- Select Create a matching API.

#### Step 3: Add your Sheetlabs authentication token to Braze (optional)

If your Sheetlabs API is public, skip this step. If it requires authentication:

- Go to the My Account page in Sheetlabs and copy your API token.
 
- Follow the steps in Braze authentication with Basic Auth to create a basic authentication credential in Braze. Use your Sheetlabs username (email address) and the API token you copied.
 
- Save the credential with a name such as sheetlabs_creds.

#### Step 4: Call the Sheetlabs API from Connected Content

Add a Connected Content call to Sheetlabs. Replace /XXX/yourapi with the path to the API you created in step 2.

```

1
2

```
 | 
```
{% connected_content https://sheetlabs.com/XXX/yourapi?language={{${language}}} :save translations :basic_auth sheetlabs_creds %}

```
 | 

#### Step 5: Template your messages

Use Liquid to reference the returned fields. For example:

```

1
2

```
 | 
```
{{translations[0].greeting}} {{${first_name}}},
{{translations[0].body1}}

```
 | 

#### Considerations

- Define the {{${language}}} field for every user you want to match. If a user has no language set, include a Liquid fallback.
 
- Connected Content calls can be cached. Measure your projected API cadence when choosing a Sheetlabs plan.

For more information, see Using Sheetlabs with Braze.

- 

New Stuff!
