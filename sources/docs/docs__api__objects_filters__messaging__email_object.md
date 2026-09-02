---
url: https://www.braze.com/docs/api/objects_filters/messaging/email_object
slug: docs__api__objects_filters__messaging__email_object
title: "Email object"
description: "This reference article explains the different components of the Braze email object."
section: api/objects_filters
fetched: 2026-09-02
evidence: company-own (technical)
---
# Email object

The email object allows you to modify or create emails through our messaging endpoints.

## Email object

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
{
 "app_id": (required, string), see App Identifier,
 "subject": (optional, string),
 "from": (required, valid email address in the format "Display Name <[email protected]>"),
 "reply_to": (optional, valid email address in the format "[email protected]" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
 "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address gets added to your outbound message as a BCC address,
 "body": (required unless email_template_id is given, valid HTML),
 "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
 "preheader": (optional*, string) recommended length 50-100 characters,
 "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
 "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
 "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
 "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
 "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
 "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
 "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
 "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
 "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
}

```
 | 

- App identifier

- Any valid app_id from an app configured in your workspace works for all users in your workspace, regardless of whether the user has the specific app on their profile or not.

- For more information and best practices on preheaders, see Email styling.

warning

Braze recommends that you avoid using Google Drive links for your attachment’s url, as this can block our servers’ calls to get the file and result in the email message not sending.

Valid attachment types include: txt, csv, log, css, ics, jpg, jpe, jpeg, gif, png, bmp, psd, tif, tiff, svg, indd, ai, eps, doc, docx, rtf, odt, ott, pdf, pub, pages, mobi, epub, mp3, m4a, m4v, wma, ogg, flac, wav, aif, aifc, aiff, mp4, mov, avi, mkv, mpeg, mpg, wmv, xls, xlsx, ods, numbers, odp, ppt, pptx, pps, key, zip, vcf, and pkpass.

An email_template_id can be retrieved from the bottom of any email template created with the HTML editor. The following shows an example of what this ID looks like:

## Example email object with attachment

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

```
 | 
```
{
 "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
 "messages":{
 "email":{
 "app_id":"YOUR_APP_ID",
 "attachments":[{
 "file_name":"YourFileName",
 "url":"https://exampleurl.com/YourFileName.pdf"
 }]
 }
 }
}

```
 | 

## Authentication for email file attachments

Use a stored basic authentication credential when an attachment URL requires a login. This applies to attachments in the email object on /messages/send and to the top-level attachments array on /campaigns/trigger/send.

- Go to Settings > Connected Content.
 
- Select Add credential.
 
- Select Basic authentication.
 
- Enter a credential name, username, and password.
 
- Include a basic_auth_credential property on each attachment that requires authentication, and set it to that credential name. The following example uses the credential name company_basic_auth_credential_name in an email object:

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

```
 | 
```
{
 "external_user_ids": ["recipient_user_id"],
 "messages":{
 "email":{
 "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
 "subject": "Basic auth attachment test",
 "from": "mail <[email protected]>",
 "body": "my attachment test",
 "attachments":[
 { "file_name":"checkout_receipt.pdf",
 "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
 "basic_auth_credential": "company_basic_auth_credential_name" }
 ]
 }
 }
}

```
 | 

## Attachment retrieval, caching, and performance

When Braze fetches a file from an attachment url:

- Caching: Braze may reuse a recently retrieved file for up to approximately 24 hours. If you need every send to pick up a new version of the file immediately, use a distinct URL per version (for example, a path or query that changes when the file changes).
 
- Timeouts: Hosts should respond quickly. If the attachment URL is slow or hangs, the message send can fail—aim for responses within about two minutes.
 
- Security: Do not put personally identifiable information (PII) or secrets in attachment URLs (including query strings), because URLs can appear in logs or downstream systems.
 
- Firewalls: If the URL is only reachable from specific networks, allow traffic from Braze in line with Connected Content IP allowlisting. Use basic authentication credentials when the file requires login.

- 

New Stuff!
