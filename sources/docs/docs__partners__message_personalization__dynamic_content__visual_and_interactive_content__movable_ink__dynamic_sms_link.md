---
url: https://www.braze.com/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/dynamic_sms_link
slug: docs__partners__message_personalization__dynamic_content__visual_and_interactive_content__movable_ink__dynamic_sms_link
title: "Dynamic SMS link preview"
description: "This reference article outlines how to turn on and use Movable Ink's SMS link preview feature."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# Dynamic SMS link preview

With Movable Ink’s dynamic SMS link preview, you can leverage the immersiveness of MMS at the same cost of SMS. This allows you to use Braze and Movable Ink to deliver cost-effective, personalized rich messaging experiences.

## Prerequisites

 Requirement | 
 Description | 

 Movable Ink account | 
 A Movable Ink account is required to take advantage of this partnership. | 

 Data source | 
 You need to connect a data source to Movable Ink. This can be done through CSV, website import, or API. | 

 MMS sending capabilities | 
 Confirm that you’re set up for MMS through Braze. | 

 Link shortening | 
 Confirm that link shortening is turned on. | 

 Contact card | 
 Your brand (the sender) must be saved as a contact on the user’s phone for link preview to work with iOS. This can be done with a contact card or another method. | 

## Integration

Follow the respective steps in this section to send dynamic SMS links for iOS and Android operating systems.

### iOS

important

To allow link preview images for iOS, users must add your brand (the sender) as a contact.

#### Step 1: Create a contact card campaign

After users save your brand as a contact, either through a contact card or another method, they will be able to view Tap to Load Preview prompts and Movable Ink links.

#### Step 2: Send Movable Ink links

- Create an SMS campaign in Movable Ink and generate your click-through URL.
 
- In the Braze dashboard, go to Campaigns and set up a new SMS/MMS campaign from the Create Campaign dropdown.
 
- In the SMS campaign composer:

- Set your subscription group.
 
- Enter your message.
 
- Add your Movable Ink link last, after all other text in the message body. 

tip

Check out Liquid for a refresher on Liquid personalization.

- You’re all set to test and launch your dynamic SMS link preview campaign.

After users load the link preview, a personalized image will render with the ability to link out to your website, app, or landing page.

### Android (Google and Samsung devices)

Android users aren’t required to save your brand as a contact in order to receive dynamic SMS link previews. However, it is still recommended so that the device can automatically load the link previews.

Users who haven’t saved your brand as a contact and have turned on automatic previews will have to select Tap to load preview to load the preview image.

## Considerations

- Only include one preview link in your message. Content will not be generated with multiple links in your SMS body.
 
- Don’t include any characters after your preview link or the experience might break.

- 

New Stuff!
