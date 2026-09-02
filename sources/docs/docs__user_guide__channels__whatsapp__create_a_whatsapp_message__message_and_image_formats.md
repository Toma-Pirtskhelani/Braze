---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats
slug: docs__user_guide__channels__whatsapp__create_a_whatsapp_message__message_and_image_formats
title: "WhatsApp message and image formats"
description: "This reference article covers message structure, component limits, and media asset requirements for creating WhatsApp messages and templates."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# WhatsApp message and image formats

Here are requirements for message structure, components, and media assets for creating WhatsApp messages and templates.

There are two types of WhatsApp messages in Braze: Template messages and response messages.

 Message type | 
 When it’s used | 
 Meta approval | 

 Template messages | 
 Business-initiated outreach; sent any time | 
 Required; templates must be submitted to Meta and approved before sending. | 

 Response messages | 
 Replies to user-initiated messages; within 24-hour conversation window only | 
 Not required | 

Template messages must be submitted to Meta for approval, which can take up to 24 hours. After approval, they can be sent at any time. Response messages (called “session messages” in Meta’s documentation) can only be sent while an active conversation window is open—within 24 hours of the last inbound message from the user.

## Template messages

WhatsApp template messages are pre-approved message formats used for business-initiated outreach. In Braze, they are built from components you define before submitting to Meta. All template messages are category-based: Marketing, utility, or authentication.

### Marketing templates

Marketing templates are the most common type used in Braze. They consist of up to four components:

 Component | 
 Required | 
 Notes | 

 Header | 
 No | 
 Supports text, image, video, document, or location. See Media Specifications for file type, size, and dimension requirements. | 

 Body | 
 Yes | 
 The main message content | 

 Footer | 
 No | 
 Supplementary text that follows the body | 

 Buttons | 
 No | 
 Include up to 10 buttons (all button types are supported) | 

#### Character length

 Component | 
 Maximum character length | 

 Body | 
 1,024 characters | 

 Footer | 
 60 characters | 

 Button label (URL, phone, quick reply) | 
 25 characters | 

 Phone number (in phone button) | 
 20 characters | 

 Template name | 
 512 characters (lowercase, alphanumeric, and underscores only) | 

#### Button types

 Button type | 
 Behavior | 
 Notes | 

 Quick reply | 
 Sends the button label text as a reply in the conversation | 
   | 

 URL | 
 Opens a URL in the user’s default browser; supports 1 variable appended to the end of the URL (max 2,000 characters) | 
 URLs containing special characters (such as &, %, <, >) may cause message send failures. Use the url_param_escape or url_escape Liquid filter to properly encode URLs with special characters. | 

 Phone number | 
 Initiates a call to the specified phone number | 
   | 

 Copy coupon code | 
 Copies a coupon code to the user’s clipboard | 
 Always requires Meta approval | 

#### Parameter formatting

Template variables can use either named parameters (such as {{first_name}}) or positional parameters (such as {{1}}). In Braze, variables can be replaced with Liquid or plain text. Always include default values for Liquid variables; messages with missing variable values will not be sent.

### Limited time offer templates

Limited time offer templates display a time-sensitive promotional offer with an optional countdown as the offer nears expiration. Use this layout for time-boxed promotions, such as seasonal sales or offers personalized to a user attribute.

 Component | 
 Required | 
 Notes | 

 Header | 
 No | 
 Select None or add media (image or video). See Media Specifications for file type, size, and dimension requirements. | 

 Offer details | 
 Yes | 
 Offer title, offer code, and an optional expiration. | 

 Body | 
 Yes | 
 The main message content. Supports Liquid. | 

 Footer | 
 No | 
 Supplementary text displayed after the body. | 

 Buttons | 
 Yes | 
 Copy offer code is included automatically. You can add one Visit website button; no other button types are supported for this template type. | 

#### Offer details

 Field | 
 Required | 
 Notes | 

 Title | 
 Yes | 
 A short line describing the offer. | 

 Code | 
 Yes | 
 The offer code recipients will copy. This populates the Copy offer code button automatically. | 

 Expiration | 
 No | 
 Set a fixed date and time (for example, an end date for a summer sale), or personalize it based on a user attribute (for example, each user’s birthday). | 

If you set an expiration, recipients see a countdown in the message that updates as the offer nears its end. For example, the message could initially show the end date, then switch to something like “5 days left” when the end date is closer. If you don’t set an expiration, the offer displays without a countdown. Braze prevents messages from sending when the expiration is in the past (for example, if the expiration is November 1, 2026 but the send time is November 15, 2026).

#### Button types

 Button type | 
 Notes | 

 Copy offer code | 
 Included automatically. Button text is “Copy offer code”, and can’t be edited. | 

 Visit website | 
 The only other button you can add. Maximum of 1. | 

### Media Card carousel templates

Carousel templates display a message body followed by 2–10 horizontally scrollable product cards, each with its own media asset and buttons. They are only available for marketing template messages.

#### Top-level message

 Component | 
 Required | 
 Maximum properties | 
 Notes | 

 Body text | 
 Yes | 
 1,024 characters | 
 Supports variables | 

 Cards | 
 Yes | 
 2-10 cards | 
 Card count is fixed at template creation. An approved carousel template can only be sent with the exact number of cards defined during creation. | 

#### Per-card specifications

 Component | 
 Required | 
 Notes | 

 Header (image or video) | 
 Yes | 
 All cards must use the same format (all image or all video). This includes the same component structure; you cannot mix cards with and without body text or buttons.

 Card header assets are automatically cropped to a wide ratio based on the user’s device. | 

 Body text | 
 No | 
 If any card includes body text, all cards must include body text | 

 Buttons | 
 No | 
 Maximum 2 buttons per card | 

#### Per-card character lengths

 Component | 
 Maximum character length | 
 Notes | 

 Card body text | 
 160 characters | 
   | 

 Button label | 
 25 characters | 
   | 

 Phone number (in phone button) | 
 20 characters | 
   | 

 URL (in URL button) | 
 2,000 characters; supports 1 variable appended to end | 
 URL buttons open in the user’s default browser, outside of WhatsApp. No order or conversion webhooks are triggered from that point. | 

## Response messages

Response messages (also called “session messages” by Meta) can only be sent within the 24-hour conversation window. They are opened and reset when a user sends your business a message.

Response messages that are composed directly in the Braze campaign or Canvas editor do not require Meta approval.

Braze supports seven response message layouts:

 Message layout | 
 Description | 

 Text | 
 Plain message body text | 

 Media | 
 Message with an image, video, audio, or document attachment | 

 Quick reply | 
 Message with up to 3 tappable reply buttons | 

 Call-to-action (CTA) button | 
 Message with a URL button or phone number button | 

 List message | 
 Message with a structured, scrollable list of selectable options | 

 Flow message | 
 Message that prompts users to complete a form or interactive task in WhatsApp, with the output returning to Braze | 

 Meta product message | 
 Message that highlights a single product, multiple products, or an entire catalog from a connected Meta catalog | 

### List message components

 Component | 
 Maximum properties | 

 Body text | 
 4,096 characters | 

 Button label (to open list) | 
 20 characters | 

 Number of sections | 
 Up to 10 | 

 Number of rows per section | 
 Up to 10 | 

 Section title | 
 24 characters | 

 Row title | 
 24 characters | 

 Row description | 
 72 characters | 

### Quick reply components

 Component | 
 Maximum properties | 

 Button | 
 Up to 3 | 

 Button label | 
 20 characters per button | 

## Media specifications

The following specifications apply to all media in WhatsApp template headers, response messages, or standalone media messages.

note

The Braze media library supports images and video only. Audio files and documents must be referenced through a hosted URL.

### Images

These specifications apply to template headers, response media messages, and image messages.

 Property | 
 Specifications | 
 Notes | 

 Supported formats | 
 JPEG, PNG | 
 Meta officially supports only JPEG and PNG for image messages. WebP is only supported for stickers (not standard image messages). | 

 Maximum file size | 
 5 MB | 
   | 

 Color mode | 
 8-bit, RGB or RGBA | 
   | 

 Caption (image messages only) | 
 Optional; 1,024 characters maximum | 
   | 

 Recommended dimensions | 
 1,125 × 600 px | 
 We recommend using JPEG or PNG images sized at 1,125×600 px (1.91:1) for consistent rendering across devices and compliance with Meta’s requirements. | 

 Recommended aspect ratio | 
 1.91:1 (wide) | 
 Square (1:1) and wide (16:9) formats are accepted, but images may be cropped or enlarged depending on the user’s device.

 For carousel cards, header images are automatically cropped to a wide ratio by WhatsApp, unless there is no body text, in which case it renders as a square. | 

### Video

The following specifications apply to template headers, response media messages, video messages, and carousel card headers.

 Property | 
 Specifications | 

 Supported formats | 
 MP4, 3GPP | 

 File size | 
 16 MB maximum | 

 Video codec | 
 H.264 only | 

 Audio codec | 
 AAC only | 

 Audio streams | 
 Single audio stream or no audio stream | 

 Caption (video messages only) | 
 Optional; 1,024 characters maximum | 

 Recommended aspect ratio | 
 1.91:1 (wide) | 

important

Meta has a known issue that can prevent some MP4 videos from playing on Android devices due to specific encoding or container settings. Until a permanent fix is available, reformatting the MP4 file resolves the issue for most senders. Test all videos on Android devices to confirm correct deliverability. 

You can reformat the MP4 file by MP4 using a web tool, such as CloudConvert. Upload your MP4 file into the tool, convert it to MP4 again, and then download the converted file.

#### Android compatibility

H.264 “High” profile encoded with B-frames is not supported on Android WhatsApp clients. Use the H.264 “Main” profile without B-frames or the “Baseline” profile for the broadest compatibility. If re-encoding with ffmpeg, use the -movflags faststart flag to place moov boxes before mdat boxes.

### Audio

The following specifications apply to response media messages and audio messages, and are based on their audio type: Voice message or basic audio message.

#### Voice message

A voice message functions like a recorded voice note, with playback controls and transcription support.

 Property | 
 Specifications | 

 Required format | 
 OGG only | 

 Required codec | 
 OPUS only (mono input) | 

 File size | 
 16 MB maximum | 

 Play icon | 
 This icon only appears if the file is 512 KB or smaller; larger files display a download icon | 

 Transcription | 
 This automatically displays if user has enabled WhatsApp voice transcripts | 

#### Basic audio message

The following specifications apply to standard audio file sharing (music clips, audio ads, and sound files).

 Format | 
 Extension | 
 Maximum file size | 
 Notes | 

 AAC | 
 .aac | 
 16 MB | 
   | 

 AMR | 
 .amr | 
 16 MB | 
   | 

 MP3 | 
 .mp3 | 
 16 MB | 
   | 

 MP4 Audio | 
 .m4a | 
 16 MB | 
   | 

 OGG (OPUS codec) | 
 .ogg | 
 16 MB | 
 OGG files must use the OPUS codec. Base audio/ogg without OPUS is not supported.

 OGG/OPUS files sent as basic audio messages will display a microphone icon (same as voice messages) rather than a music icon. | 

#### Considerations

note

The Braze media library supports images and video only. Audio files and documents must be referenced through a hosted URL.

- No caption support for audio messages.
 
- A common error is mismatched MIME types. Verify your file’s MIME type matches its extension before sending.

### Documents

The following specifications apply to template headers (document format), response media messages, and document messages.

 Document type | 
 File types | 
 Maximum file size | 

 PDF | 
 PDF | 
 100 MB | 

 Microsoft Word | 
 DOC, DOCX | 
 100 MB | 

 Microsoft Excel | 
 XLS, XLSX | 
 100 MB | 

 Microsoft PowerPoint | 
 PPT, PPTX | 
 100 MB | 

 Plain text | 
 TXT | 
 100 MB | 

#### Considerations

note

The Braze media library supports images and video only. Audio files and documents must be referenced through a hosted URL.

- Captions are optional and can be 1,024 characters maximum.
 
- Filename is optional. WhatsApp uses the file extension to determine which document icon to display in the conversation.
 
- Only the listed formats are officially supported. Other file types may send but are not guaranteed to render correctly in WhatsApp

## Quick reference: WhatsApp media specifications

 Media type | 
 File types | 
 Maximum file size | 
 Caption availability | 

 Image | 
 JPEG, PNG | 
 5 MB | 
 Yes (1,024 characters maximum) | 

 Video | 
 MP4, 3GPP | 
 16 MB | 
 Yes (1,024 characters maximum) | 

 Audio (voice) | 
 OGG (OPUS) | 
 16 MB | 
 No | 

 Audio (basic) | 
 AAC, AMR, MP3, M4A, OGG | 
 16 MB | 
 No | 

 Document | 
 PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 
 100 MB | 
 Yes (1,024 characters maximum) | 

- 

New Stuff!
