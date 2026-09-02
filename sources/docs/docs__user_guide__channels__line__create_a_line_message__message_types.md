---
url: https://www.braze.com/docs/user_guide/channels/line/create_a_line_message/message_types
slug: docs__user_guide__channels__line__create_a_line_message__message_types
title: "LINE message types"
description: "This article covers the different types of LINE messages."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# LINE message types

This article covers the LINE message types you can compose, including aspects and limitations.

When you compose a LINE message, you can drag-and-drop message types into the composer and then customize them.

## Text

A LINE text message can contain up to 5,000 characters and include emojis and Liquid personalization.

Use cases include:

- Announce a limited-time promotion for clearance stock
 
- Send personalized birthday greetings with unique promotion cards
 
- Share quick updates about upcoming events

## Image

A LINE image message can be added through the media library, a URL, or Liquid. These images are standalone and don’t contain clickable links.

Use cases include:

- Showcase a vacation destination to inspire users to look into purchasing plane tickets
 
- Highlight end-of-season promotions to encourage users to stock up on next year’s winter clothes with great deals
 
- Start a visual countdown to a storewide annual sale

### URL image

Use URL images for use cases that incorporate:

- Liquid dynamic images by including the Liquid in your image source attribute. For example, you can insert https://example.com/images/?imageBanner={{first_name}} as the image URL to include a user’s first name in the image
 
- Connected Content by pulling images directly from your web server or publicly accessible APIs
 
- Braze catalogs by accessing images from imported CSV files and API endpoints

 Specifications | 
 Recommended properties | 

 Image file URL length | 
 2,000 characters maximum | 

 Image format | 
 PNG, JPEG | 

 File size | 
 10 MB maximum | 

## Rich messages (image map)

A LINE rich message is an image that contains one or more links that are opened by selecting specific areas on the image. Select a rich message templates to choose how the links are mapped onto the image.

Use cases include:

- Display a grid of newly arrived handbags with links to each bag’s respective product page
 
- Present an interactive menu that starts an combo order by selecting an item
 
- Lay out multiple promotions for users to choose by selecting a grid square

### Image map

 Specifications | 
 Recommended properties | 

 Image file URL length | 
 2,000 characters maximum | 

 Image format | 
 PNG (can be transparent), JPEG | 

 Aspect ratio | 
 1:1 (width:height) | 

 File size | 
 10 MB maximum | 

### URI link

 Specifications | 
 Recommended properties | 

 Character count | 
 1,000 maximum | 

 Schemes | 
 HTTP, HTTPS, LINE, tel | 

### Text

A text rich message can contain up to 400 characters.

## Card-based (carousel)

A LINE card-based message allows users to scroll through multiple messages, like a carousel, and take action on the messages most relevant to them by selecting a card or a card’s buttons.

Use cases include:

- Display promotions for specific menu items
 
- Highlight this season’s best-selling jackets
 
- Present a sampling of cooking tools and gadgets that are included in a kit

### Message

 Specifications | 
 Recommended properties | 

 Columns | 
 10 maximum | 

 Aspect ratio | 
 Rectangle: 1.51:1 
 Square: 1:1 | 

 Title | 
 40 characters maximum | 

### Image

 Specifications | 
 Recommended properties | 

 Image URL | 
 2,000 characters maximum | 

 Image format | 
 JPEG or PNG | 

 Width | 
 1,024 pixels | 

 File size | 
 1 MB | 

### Text

 Specifications | 
 Recommended properties | 

 Characters | 
 120 maximum (no image or title) 
 60 maximum (message with an image or title) | 

 Actions | 
 3 maximum | 

- 

New Stuff!
