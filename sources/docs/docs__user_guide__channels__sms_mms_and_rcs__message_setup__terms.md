---
url: https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/terms
slug: docs__user_guide__channels__sms_mms_and_rcs__message_setup__terms
title: "Terms to Know"
description: "This glossary defines various SMS, MMS, and RCS terms you should know."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Terms to Know 

 Check out the following terms to learn more about SMS, MMS, and RCS ecosystems, technologies, and processes. 

 Search glossary
 Results update automatically as you type.

Alphanumeric Sender ID 
Alphanumeric Sender ID allows you to set your company name or brand as the Sender ID using alphanumeric characters when sending one-way messages to supported countries.

Basic RCS 
Text-only RCS messages up to 160 characters. Billed as a single message. This category is only used in the global model.

Encoding 
The conversion of anything into a coded form. SMS content can be encoded in either GSM-7 or UCS-2.

GSM-7 Encoding (Global System for Mobile Communications) 
GSM-7 is the most seen encoding standard for most SMS messaging. It uses most of the Greek and English alphabets, as well as some additional characters. You can learn more about GSM-7 encoding and which character sets you can use from Wikipedia. Languages such as Chinese, Korean, or Japanese must be transferred using the 16-bit UCS-2 character encoding. 
 
 You can estimate that the character limit per segment for this type of encoding is 128 characters.

Global STOP Keywords 
Variations include STOP, END, QUIT, UNSUBSCRIBE, CANCEL, STOPALL. These are referred to as Global-Stop-Keywords. If any of these keywords are texted in to a short or long code, it results in the mobile number (the originating mobile phone number) being opted-out of every active SMS program on that code it is associated with.

Keyword 
A short word that is sent to a short or long code to interact with a pre-defined SMS program or to request to OPT-OUT of a specific program or all programs on a code. For example, STOP. Keywords should 
 - be alphanumeric 
 - have no spaces 
 - be less than 10 characters. 
 
 A specific keyword and short code combination may only be used on one active program at a time. If a keyword is entered that is already in use by another program, a validation error will appear. 
 
 There are two mandatory keyword categories that all SMS content providers must comply with: STOP and HELP.

Long Code 
This is the standard, 10-digit phone number (in most countries) that allows senders to send more messages at the rate of one message per second.

Either a short or a long code is required.

MMS (Multimedia Message Service) 
MMS is used to send messages containing multimedia assets (JPEG, GIF, PNG) to mobile phones. Like SMS, MMS is a high urgency messaging channel that allows you to communicate with customers immediately. MMS extends the capabilities of SMS by giving you the ability to add media to otherwise text-only SMS.

Mandatory Keyword HELP 
For each program that is created in the SMS Campaign Manager platform, content for this keyword must be provided and has to meet the best practices and carrier compliance per country or region in which the SMS traffic is being sent and received. In most cases, this content should have a brief explanation of the SMS program, and how to OPT-OUT.

Message Segments 
A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments may result in additional charges.

Message Service 
A collection of long codes, short codes, and alphanumeric IDs used to send your SMS message with Braze.

One-Way Messaging 
One-way messaging allows you to communicate with your customers by sending text messages. One-way messaging is useful if you are implementing an alphanumeric sender ID in markets where long and short codes are not available.

RCS (Rich Communication Services) 
Rich Communication Services (RCS) enhances traditional SMS by enabling brands to deliver messages that are not only informative but also far more engaging. RCS brings features like high-quality media, interactive buttons, and branded sender profiles directly into users' pre-installed messaging apps.

RCS-Verified Sender 
The sending entity of an RCS message, or what the recipient sees on their device to identify where the message is coming from. RCS-verified senders contain a company name, caption, visual branding, and a verified badge. After you provide the necessary RCS sender registration information to Braze, Braze takes care of registration and subscription group setup.

Rich Media RCS 
RCS messages that include a media file (image, video) or a Rich Card. Billed as a single message, regardless of message length. This category is only used in the United States model.

Rich RCS 
Text-only RCS messages, with or without limited suggestions or buttons. Billed per segment (160 UTF-8 bytes). This category is only used in the United States model.

SMS (Short Message Service) 
A messaging channel created in 1980 and one of the oldest texting technologies. It also happens to be one of the most wide-spread and more frequently used, of all texting channels. This channel is a more direct way to reach your users and customers than most other messaging channels, as it utilizes their personal phone number to reach them. As such, SMS has more rules and regulations around it than other messaging channels.

SMS Fallback 
If an RCS message is unable to be delivered (for example, lack of carrier support in the region), Braze will still attempt to deliver the message through SMS when an SMS code exists within the subscription group.

Shared Short Code 
When using a shared short code, all text messages, no matter what business or organization sends them, arrives on a consumer's mobile device from the same 5-6 phone number. While shared short codes are relatively low cost and immediately available, this means that your business will not have a dedicated short code, and are subject to other businesses following the correct protocol with your shared short code.

Short Code 
This is a short, memorable 5-6 digit sequence that allows senders to send more messages at more consistent rates than long numbers (one message per second).

Either a short or a long code is required.

Single RCS 
Text-only RCS messages that are over 160 characters or include any rich elements, like buttons or media. This category is only used in the global model.

Subscription Groups for SMS 
Subscription groups are a Braze tool that allows you to target specific subscription levels of users or customers. subscription groups for SMS are constructed internally based on your message service and cannot be shared across workspaces.

Toll-Free Number 
An toll-free telephone number or freephone number is a telephone number that is billed for all arriving calls instead of incurring charges to the originating telephone subscriber. Toll-free numbers in the US and Canada are SMS-enabled, where subscribers are charged for incoming and outgoing texts.

Toll-Free messaging works best when your use case is person-to-person, such as customer support or sales, with both the sender and the recipient having a conversation via text.

Two-Way Messaging 
Two-way messaging allows you to carry on a conversation by both sending and receiving text messages.

UCS-2 Encoding (Universal Coded Character Set) 
UCS-2 encoding is a fallback encoding standard, especially when a message cannot be encoded using GSM-7 or when a language needs more than 128 characters to be rendered. USC-2 is better measured by code points, as opposed to "characters". Regardless, you could estimate that the character limit per segment for this type of encoding is 67 characters.

Vanity Code 
A vanity short code is a 5-6 digit phone number that is specifically selected by a brand. Vanity short codes are branded and easier for consumers to remember.

- 

New Stuff!
