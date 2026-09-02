---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks
slug: docs__user_guide__messaging__design_and_edit__editor_blocks
title: "Drag-and-drop editor blocks"
description: "This reference article covers editor blocks in the drag-and-drop editor for email, in-app messages, landing pages, Banners, and drag-and-drop email preference centers."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Drag-and-drop editor blocks

Editor blocks are the tiles you drag into rows and columns in the drag-and-drop editor.

Select the editor you’re using:

- email
 
- in-app messages
 
- landing pages
 
- banners
 
- preference center

## Email editor blocks

Editor blocks are in the Content section for email messages. Drag a block inside a column in the Drag-And-Drop Editor; it auto-adjusts to the column width.

For more information about creating emails in the Drag-And-Drop Editor, see Create an email with drag-and-drop and Other customizations in that article.

tip

You can also add custom attributes to any URL within the Image, Button, or Text editor blocks.

### Title

Adds text for headers within the email.

 Property | 
 Description | 

 Title | 
 Selects the heading style. | 

 Font family | 
 The font style for your title. | 

 Font weight | 
 The overall boldness of the font. | 

 Font size | 
 Determines the size of your text. | 

 Text color | 
 Modifies the color of the title. | 

 Link color | 
 Modifies the color of the link. | 

 Align | 
 Moves the title to be left, center, or right-oriented. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text direction | 
 Default left-to-right, but can be edited to be right-to-left. | 

### Paragraph

Enters text into the message. A toolbar helps with font and text editing functionality.

 Property | 
 Description | 

 Font family | 
 The font style for your paragraph text. | 

 Font weight | 
 The overall boldness of the font. | 

 Font size | 
 Determines the size of your text. | 

 Text color | 
 Modifies the color of the text. | 

 Link color | 
 Modifies the color of the link. | 

 Align | 
 Moves the text to be left, center, or right-oriented. | 

 Paragraph spacing | 
 Modifies the space between paragraphs. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text direction | 
 Default left-to-right, but can be edited to be right-to-left. | 

### List

Adds a bulleted list.

 Property | 
 Description | 

 List type | 
 The type of list. Can be either bulleted or numbered. | 

 List style type | 
 Determines the style of your list. | 

 Start list from | 
 Determines the starting number for your list. | 

 Font family | 
 The font style for your paragraph text. | 

 Font weight | 
 The overall boldness of the font. | 

 Font size | 
 Determines the size of your text. | 

 Text color | 
 Modifies the color of the text. | 

 Link color | 
 Modifies the color of the link. | 

 Align | 
 Moves the text to be left, center, or right-oriented. | 

 List items spacing | 
 Modifies the space between list items. | 

 List items indent | 
 Modifies the indentation of list items. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text direction | 
 Default left-to-right, but can be edited to be right-to-left. | 

### Button

Adds a standard button. Properties allow for editing styling and setting link behavior.

 Property | 
 Description | 

 Button options | 
 Sets various button options, such as font, size, width, color, and padding. | 

 Button hover | 
 The style of the button when a user hovers over it using a mouse or trackpad. Includes the button’s background color, font color, and border styles. | 

#### On-click behavior

 Property | 
 Description | 

 Link type | 
 Determines the action when clicking the button and sets the appropriate protocol. | 

 URL | 
 Dynamic based on the Open web page link type. | 

 Mail to, subject, and body | 
 For the Send email link type, sets the recipient email address, subject, and content that will populate in a draft email when the user selects the button. | 

 Tel | 
 For the Make call and Send SMS link type, sets the phone number the user will call or text when selecting the button. | 

 Message | 
 For the Send SMS link type, sets the content that will populate in a draft SMS message when the user selects the button. | 

### Divider

Inserts a solid, dotted, or dashed line to help with spacing.

 Property | 
 Description | 

 Transparent | 
 If enabled, the line and width options are removed. | 

 Line | 
 The different line formats, whether dotted, dashed, or solid. You can also modify the thickness and color of the divider line. | 

 Width | 
 Adjusts the spread of the divider in increments of 5. | 

 Align | 
 Moves the line to be either left, center, or right-oriented. | 

### Spacer

Adds space or padding between other blocks.

 Property | 
 Description | 

 Height | 
 Adjusts the height of the spacer block. The default is 60px. | 

### Image

Inserts an image from the media library. For dynamic images (images with Liquid or Connected Content), you must set a fallback image to use the auto-width settings. For image specifications, see email image specifications.

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

 Property | 
 Description | 

 Auto width | 
 Modifies the width of the image in pixels. | 

 Align | 
 Sets image alignment to left, center, or right within the block. | 

 Image with Liquid | 
 Use Liquid logic to dynamically set different images within the same block of content. | 

 URL | 
 Set an image using the address to where it’s hosted. | 

 Alternate text | 
 A short description of the image that gives users the same information shown in the image. Essential for screen-reader accessibility or when the image fails to load. | 

 Image with rounded corners | 
 Renders the image with rounded corners. By default, images are rendered with squared corners. | 

 Action | 
 Triggers an action when the user clicks the image. | 

 Block options | 
 Sets padding around the image block. | 

tip

For Auto width, automatic image resizing picks the best size for the image based on a combination of image width and available space in the layout:

- Images wider than the available space are set at 100% width and keep this ratio on mobile, using the entire device display width.
 
- Images smaller than the available space use the image’s natural size to avoid distortion effects or blurry pictures.

#### Gmail download button behavior

Gmail automatically appends a download button to images that do not have a hyperlink (href) associated with them. However, if the image’s aspect ratio is 299 x 524 px or smaller, Gmail will not display the download button.

To prevent the download button from appearing on larger images, you can apply the “#” link workaround:

- Select the Image block.
 
- In the Block Options panel, go to the Link section.
 
- Set the Link type to Open web page.
 
- Enter a pound sign (#) in the URL input field.

Adding this link prevents Gmail from displaying the download button while not affecting the user experience.

### Video

Creates a link to video content. Only YouTube and Vimeo are supported.

 Property | 
 Description | 

 URL | 
 The URL for the video. | 

 Title | 
 Auto-generated from the video metadata or can be customized. | 

 Play icon style | 
 Includes different options for the play button located at the top of a video image. | 

 Play icon color | 
 Option to select either Light or Dark for the play button. | 

 Play icon size | 
 Choose the pixel size for the play button. Predefined range from 50 px to 80 px (incremented by 5 px). | 

tip

Videos hosted by Vimeo only work if they are set to public. All other security settings available within Vimeo (for example, “Hide from Vimeo.com”) generate a different link format that is not supported by this Content Block. These types of links are altered by the builder, which prevents Braze from generating a thumbnail.

### Social

Inserts social media platform icons. You can upload custom images for brand-specific icons.

 Property | 
 Description | 

 Select icon collection | 
 Sets the style of your icon collection. | 

 Configure icon collection | 
 Sets the URL for each social icon. Includes the More options toggle to edit the title and alternative text. | 

 Align | 
 Moves the social icon to be left, center, or right-oriented. | 

 Icon spacing | 
 Determines the spacing between each social icon. | 

### Icons

Inserts an icon. You can upload custom images. Braze uses an oversized placeholder icon until you upload an image.

 Property | 
 Description | 

 Font family | 
 The font style for your paragraph text. | 

 Font weight | 
 The overall boldness of the font. | 

 Font size | 
 Determines the size of your text. | 

 Text color | 
 Modifies the color of the title. | 

 Link color | 
 Modifies the color of the link. | 

 Align | 
 Moves the icon to be left, center, or right-oriented. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Icon size | 
 Determines the size of your icon. | 

 Icon spacing | 
 Modifies the space of the icon. | 

 Icon padding | 
 Modifies the padding of the icon. | 

### HTML

Inserts raw HTML. Recommended for Liquid, such as Connected Content or conditional statements.

 Property | 
 Description | 

 HTML | 
 Add or edit raw HTML, including Liquid for personalization or conditional logic. | 

### Menu

Creates a flexible menu for the message you’re designing.

 Property | 
 Description | 

 Configure menu items | 
 Add a menu item. | 

 Font family | 
 The font style for the menu. | 

 Font size | 
 The size of your menu. | 

 Text color | 
 Modifies the color of the menu. | 

 Link color | 
 Modifies the color of the menu text. | 

 Align | 
 Moves the menu to be left, center, or right-oriented. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Layout | 
 Determines the layout to be either horizontal or vertical. | 

 Separator | 
 Adds character(s) between the menu options. | 

 Mobile menu | 
 Includes options to modify the icon size, color, and icon type when shown on a mobile device. | 

 Item padding | 
 Modifies the padding by using either the + or - button, or by entering a specific number. | 

 All sides | 
 Sets a consistent padding number if item padding is disabled. | 

### Product

Renders product rows from a Product Catalog, either as static items from a catalog Selection (up to 12) or as dynamic products driven by a Canvas eCommerce trigger (up to 24).

 Property | 
 Description | 

 Content type | 
 Sets whether products come from a fixed catalog Selection (Static, up to 12 products) or from a Canvas eCommerce recommendation trigger (Dynamic, up to 24 products). Dynamic is only available in Canvas message steps. | 

 Catalog | 
 Selects which Product Catalog supplies product data and field mappings. | 

 Selection | 
 (Static only) Selects which filtered set on the catalog defines which products appear. | 

 Show source details | 
 Toggles help text showing the underlying catalog or event field mapped to each product field. | 

 Variant image | 
 Shows or hides the variant image for each product tile. | 

 Product title | 
 Shows or hides the product title for each tile. | 

 Price | 
 Shows or hides the product price. | 

 Button for product URL | 
 Shows or hides a call-to-action button linking to the product URL. | 

 Quantity | 
 (Dynamic, Canvas only, when the entry trigger is not a product view event) Shows or hides the product quantity from the trigger event. | 

 Product orientation | 
 Sets the image position within each tile: Image left, Image center, or Image right. | 

 Alignment | 
 Sets the horizontal alignment of content within each tile. | 

 Max products per row | 
 Sets how many products appear per row: 1, 2, or 3 (3 is only available when orientation is Image center). | 

 Product spacing | 
 Sets spacing between products: Auto or Custom. | 

 Custom spacing | 
 (When Custom is selected) Sets the gap in pixels between products. | 

## Personalization

You can add personalization to your email using Liquid or Connected Content.

- Liquid: Under Content > Personalization, select an attribute, copy the snippet, and paste it into an HTML block. While basic Liquid snippets may work in Title, Paragraph, and List blocks, placing Liquid in these blocks can cause unexpected behavior and layout issues. To avoid issues, use HTML blocks for any Liquid logic. Note that Liquid isn’t supported in image blocks or in button URL fields.
 
- Connected Content: Add an HTML block and place your {% connected_content %} call there.

## In-app message editor blocks

Editor blocks are in the Build section for in-app messages. Drag a block into a column; it auto-adjusts to the column width. Select a block to edit its settings in the right-side panel.

For more information about creating in-app messages in the Drag-And-Drop Editor, see Create an in-app message with drag-and-drop.

### Title and paragraph

Adds title or paragraph text to the message.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Text color | 
 Modifies the color of the text. | 

### Button

Adds a standard button with configurable styling, links, and analytics.

 Property | 
 Description | 

 Button width | 
 Modifies the width of the button to be automatic or manual. | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Button alignment | 
 Moves the button to be left, center, or right-oriented. | 

 Button text color | 
 Modifies the color of the text on the button. | 

 Background color | 
 Modifies the color of the button’s background. | 

 Border style | 
 Determines the style of the button’s border. | 

 Border radius | 
 Determines how round the corners are. | 

#### On-click behavior

 Action | 
 Description | 

 Submit form when button is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the button for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the button, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the button updates the user’s profile with custom data. You can also select the identifier for reporting. | 

### Radio button

Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute, which must be a string to be saved. Custom attributes with other data types do not save to the user profile.

 Property | 
 Description | 

 Custom attribute name | 
 Selects which custom user attribute stores the user’s selected option when the form is submitted. | 

 Total choices | 
 The list of options; each option has a Label text (what users see) and an Attribute value (what is stored). You can add up to 15 choices, with a minimum of 2. | 

 Font family | 
 Typeface for the radio group text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the option label text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the choices within the block. | 

 Accent color | 
 Color used for the radio button controls (such as the selected state indicator). | 

 Padding | 
 Spacing around the block. | 

### Image

Inserts an image from the media library.

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

 Property | 
 Description | 

 URL | 
 The hosted address for the image. | 

 Alignment | 
 Moves the image to be left, center, or right-oriented. | 

 Background color | 
 Modifies the color of the image’s background. | 

 Border style | 
 Determines the style of the image’s border. | 

 Border radius | 
 Determines how round the corners of the image are. | 

For image specifications, refer to our in-app message image specifications.

#### On-click behavior

 Action | 
 Description | 

 Alt text | 
 The written copy that appears in place of an image if the image fails to load. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. | 

 Submit form when image is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the image for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the image, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the image updates the user’s profile with custom data. You can also select the identifier for reporting. | 

### Link

Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text color | 
 Modifies the color of the text. | 

#### On-click behavior

 Action | 
 Description | 

 URL | 
 The hyperlink to navigate to. | 

 Identifier for Reporting | 
 Determines the identifier for reporting. | 

### Spacer

Adds space or padding between other blocks.

 Property | 
 Description | 

 Background color | 
 Modifies the background color of the spacer. | 

 Height | 
 Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. | 

### Custom code

Inserts custom HTML, CSS, or JavaScript for advanced customization.

 Property | 
 Description | 

 Custom code | 
 Allows you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message. | 

### Phone capture

Inserts a form field for phone numbers. When submitted, the user is subscribed to the SMS or WhatsApp subscription group.

 Property | 
 Description | 

 Subscription group | 
 The SMS or WhatsApp subscription group the user is subscribed to on submit. Includes an option to collect phone numbers from all countries. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder phone number to display. | 

### Email capture

Inserts a form field for email addresses. When submitted, the email address is added to that user’s profile in Braze.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Text color | 
 Modifies the color of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder email address to display. | 

### Short text

Inserts a form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice.

 Property | 
 Description | 

 Required input field | 
 Marks whether the field must be filled before the form can be submitted. | 

 Maximum characters | 
 Limits how many characters a user can type (string custom attributes cap at 255). | 

 Placeholder text | 
 Text shown inside the input until the user types. | 

 Attribute | 
 Stores the submitted value as First name, Last name, or a Custom attribute on the user profile. | 

 Custom attribute name | 
 Selects which string custom attribute receives the submitted value (available when Attribute is set to Custom attribute). | 

 Font family | 
 Typeface for the input text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the input text. | 

 Font size | 
 Size of the input text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Color | 
 Color of the text typed in the field. | 

 Text alignment | 
 Horizontal alignment of the input text within the field. | 

 Padding | 
 Spacing around the block. | 

### Dropdown

Inserts a dropdown with a predefined list of items from which users can select one. You can add any custom attribute strings to the list.

 Property | 
 Description | 

 Required input field | 
 Marks whether the user must select an option before the form can be submitted. | 

 Placeholder text | 
 Text shown in the dropdown until a user selects an option. | 

 Custom attribute name | 
 Selects which custom user attribute receives the selected value. | 

 Total options | 
 The list of options; each option has an Option label (what users see) and an Attribute value (what is stored). | 

 Font family | 
 Typeface for the dropdown text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical line spacing. | 

 Text color | 
 Color of the dropdown text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the dropdown (left or center). | 

 Padding | 
 Spacing around the block. | 

### Checkbox

Inserts a checkbox. If the user checks the box, the block’s boolean custom attribute is set to true. If left unchecked, its attribute is set to false.

 Property | 
 Description | 

 Required input field | 
 Marks whether the checkbox must be checked before the form can be submitted. | 

 Custom attribute name | 
 Selects which boolean custom attribute receives true when checked or false when unchecked. | 

 Accent color | 
 Color used for the checkbox control styling. | 

 Padding | 
 Spacing around the block. | 

### Checkbox group

Users can select from multiple choices. Values are set or added to a defined array custom attribute.

 Property | 
 Description | 

 Required input field | 
 Marks whether the user must select at least the minimum number of options before submitting. | 

 Minimum choices | 
 Minimum number of options a user must select (when the field is required). | 

 Maximum choices | 
 Maximum number of options a user can select. | 

 Custom attribute name | 
 Selects which array custom attribute the selected values write to. | 

 Action | 
 Sets whether submission Sets items (replaces the array) or Adds items (appends to the array). | 

 Total choices | 
 The list of options; each option has a Label text (what users see) and an Attribute value (what is stored). | 

 Font family | 
 Typeface for option labels. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the option label text. | 

 Font size | 
 Size of the option label text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the option label text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the group (start or center). | 

 Accent color | 
 Color of the checkbox controls. | 

 Padding | 
 Spacing around the block. | 

### Long text

Multi-line text field for survey-style flows. If you don’t see this block, contact Braze Support or your Braze customer success manager.

 Property | 
 Description | 

 Required input field | 
 Marks whether the field must be filled before the form can be submitted. | 

 Minimum characters | 
 The minimum number of characters a user must enter. | 

 Maximum characters | 
 The maximum number of characters a user can enter. | 

 Hide character count | 
 Hides or shows the live character counter for the text area. | 

 Placeholder text | 
 Text shown inside the empty text area until the user types. | 

 Height (rows of text) | 
 Controls how tall the text area appears, measured in rows. | 

 Font family | 
 Typeface for the text area text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

## Things to know

- Video: The standard composer does not include a dedicated video block. Use Custom code to embed a player if needed. For more information, see In-app messages: Frequently asked questions.

## Landing page editor blocks

Editor blocks for landing pages are in the Build section of the Drag-And-Drop Editor, under Rows and block categories. Drag a block into a row column; it auto-adjusts to the column width. Select a block to edit its settings in the right-side properties panel.

For more information about creating and publishing landing pages, see Create landing pages.

### Title and paragraph

Adds heading or body text. Useful for structuring sections and improving readability.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Text color | 
 Modifies the color of the text. | 

### Button

Adds a clickable element for actions such as opening a link or submitting a form.

 Property | 
 Description | 

 Button width | 
 Modifies the width of the button to be automatic or manual. | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Button alignment | 
 Moves the button to be left, center, or right-oriented. | 

 Button text color | 
 Modifies the color of the text on the button. | 

 Background color | 
 Modifies the color of the button’s background. | 

 Border style | 
 Determines the style of the button’s border. | 

 Border radius | 
 Determines how round the corners are. | 

#### On-click behavior

 Action | 
 Description | 

 Submit form when button is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the button for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the button, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the button updates the user’s profile with custom data. You can also select the identifier for reporting. | 

important

If you configure a button with Submit form when button is clicked and open a web URL in a new tab, iOS Safari may block the navigation. Open the post-submit URL in the same tab when submitting forms. For more information, see Create landing pages.

### Radio button

Adds a list of options from which users can select one. Use the properties panel to configure the available options and the custom attribute that receives the selected value. The user profile logs the selected value as a string custom attribute when the form is submitted. Custom attributes with other data types do not save to the user profile.

 Property | 
 Description | 

 Custom attribute name | 
 Selects which custom user attribute stores the user’s selected option when the form is submitted. | 

 Total choices | 
 The list of options; each option has a Label text (what users see) and an Attribute value (what is stored). You can add up to 15 choices, with a minimum of 2. | 

 Font family | 
 Typeface for the radio group text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the option label text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the choices within the block. | 

 Accent color | 
 Color used for the radio button controls (such as the selected state indicator). | 

 Padding | 
 Spacing around the block. | 

### Image

Displays an image from an upload or external URL.

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

 Property | 
 Description | 

 URL | 
 The hosted address for the image. | 

 Alignment | 
 Moves the image to be left, center, or right-oriented. | 

 Background color | 
 Modifies the color of the image’s background. | 

 Border style | 
 Determines the style of the image’s border. | 

 Border radius | 
 Determines how round the corners of the image are. | 

#### On-click behavior

 Action | 
 Description | 

 Alt text | 
 The written copy that appears in place of an image if the image fails to load. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. | 

 Submit form when image is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the image for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the image, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the image updates the user’s profile with custom data. You can also select the identifier for reporting. | 

### Link

Adds a hyperlink users can select to go to a URL. Can sit in text or stand alone.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text color | 
 Modifies the color of the text. | 

#### On-click behavior

 Action | 
 Description | 

 URL | 
 The hyperlink to navigate to. | 

 Identifier for Reporting | 
 Determines the identifier for reporting. | 

### Spacer

Adds vertical spacing between elements.

 Property | 
 Description | 

 Background color | 
 Modifies the background color of the spacer. | 

 Height | 
 Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. | 

### Custom code

Inserts custom HTML, CSS, or JavaScript for advanced customization, such as Google Tag Manager.

 Property | 
 Description | 

 Custom code | 
 Allows you to add, edit, or delete HTML, CSS, and JavaScript. | 

### Email capture

Adds a form field for email addresses. On submit, the address is saved to the user’s Braze profile.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Text color | 
 Modifies the color of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder email address to display. | 

### Phone capture

Adds a form field for phone numbers. On submit, subscribes the user to your selected SMS or WhatsApp subscription group.

 Property | 
 Description | 

 Subscription group | 
 The SMS or WhatsApp subscription group the user is subscribed to on submit. Includes an option to collect phone numbers from all countries. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder phone number to display. | 

### Input field

Adds a form field for standard attributes (for example, first or last name) or a custom attribute string.

 Property | 
 Description | 

 Required input field | 
 Marks whether the field must be filled before the form can be submitted. | 

 Maximum characters | 
 Limits how many characters a user can type (string custom attributes cap at 255). | 

 Placeholder text | 
 Text shown inside the input until the user types. | 

 Attribute | 
 Stores the submitted value as First name, Last name, or a Custom attribute on the user profile. | 

 Custom attribute name | 
 Selects which string custom attribute receives the submitted value (available when Attribute is set to Custom attribute). | 

 Font family | 
 Typeface for the input text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the input text. | 

 Font size | 
 Size of the input text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Color | 
 Color of the text typed in the field. | 

 Text alignment | 
 Horizontal alignment of the input text within the field. | 

 Padding | 
 Spacing around the block. | 

### Dropdown

A predefined list of items; users pick one. You can map values to custom attribute strings.

 Property | 
 Description | 

 Required input field | 
 Marks whether the user must select an option before the form can be submitted. | 

 Placeholder text | 
 Text shown in the dropdown until a user selects an option. | 

 Custom attribute name | 
 Selects which custom user attribute receives the selected value. | 

 Total options | 
 The list of options; each option has an Option label (what users see) and an Attribute value (what is stored). | 

 Font family | 
 Typeface for the dropdown text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical line spacing. | 

 Text color | 
 Color of the dropdown text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the dropdown (left or center). | 

 Padding | 
 Spacing around the block. | 

### Checkbox

When checked, sets the block’s boolean custom attribute to true; when unchecked, to false.

 Property | 
 Description | 

 Required input field | 
 Marks whether the checkbox must be checked before the form can be submitted. | 

 Custom attribute name | 
 Selects which boolean custom attribute receives true when checked or false when unchecked. | 

 Accent color | 
 Color used for the checkbox control styling. | 

 Padding | 
 Spacing around the block. | 

### Checkbox group

Users pick multiple options; values set or append to a defined array custom attribute.

 Property | 
 Description | 

 Required input field | 
 Marks whether the user must select at least the minimum number of options before submitting. | 

 Minimum choices | 
 Minimum number of options a user must select (when the field is required). | 

 Maximum choices | 
 Maximum number of options a user can select. | 

 Custom attribute name | 
 Selects which array custom attribute the selected values write to. | 

 Action | 
 Sets whether submission Sets items (replaces the array) or Adds items (appends to the array). | 

 Total choices | 
 The list of options; each option has a Label text (what users see) and an Attribute value (what is stored). | 

 Font family | 
 Typeface for option labels. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the option label text. | 

 Font size | 
 Size of the option label text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the option label text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

 Align | 
 Horizontal alignment of the group (start or center). | 

 Accent color | 
 Color of the checkbox controls. | 

 Padding | 
 Spacing around the block. | 

### Manage subscriptions

Adds a checklist of email subscription groups so visitors can opt in to or manage their subscriptions when they submit the form. Configure it after you add subscription groups to the block. This block only supports email subscription groups; it doesn’t support SMS, RCS, or WhatsApp subscription groups.

For identified users who open the page through the landing page’s Liquid tag, the block pre-fills each checkbox with the user’s current subscription state, so it can also serve as a preference management page.

Select the block in the editor to:

- Reorder subscription groups
 
- Add or remove subscription groups
 
- Add or remove descriptions
 
- Add or remove a “Subscribe to all” checkbox that selects every subscription group in the block

 Property | 
 Description | 

 Subscription groups | 
 Add, remove, or reorder the subscription groups shown in the block. | 

 Include descriptions | 
 Displays each subscription group’s description alongside its name. | 

 Subscribe to all checkbox | 
 Adds a checkbox that selects every subscription group in the block. | 

For the full setup flow, see Manage Subscriptions block.

### Long text

Multi-line text field for survey-style flows. If you don’t see this block, contact Braze Support or your Braze customer success manager. This block is not available for standard landing pages.

 Property | 
 Description | 

 Required input field | 
 Marks whether the field must be filled before the form can be submitted. | 

 Minimum characters | 
 The minimum number of characters a user must enter. | 

 Maximum characters | 
 The maximum number of characters a user can enter. | 

 Hide character count | 
 Hides or shows the live character counter for the text area. | 

 Placeholder text | 
 Text shown inside the empty text area until the user types. | 

 Height (rows of text) | 
 Controls how tall the text area appears, measured in rows. | 

 Font family | 
 Typeface for the text area text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

## Things to know

- Video: The standard composer does not include a dedicated video block. Use Custom code to embed a player if needed. For more information, see Landing pages.

## Banner editor blocks

In the Banner composer, drag rows and blocks from the Build section into the canvas to lay out your message. Select Styles to adjust page-level styling, or select a block or row to edit its properties in the side panel.

For the full Banner creation flow, see Create a Banner.

The Banner composer offers the same kinds of layout blocks as other drag-and-drop surfaces, but not the full form block set (for example no radio button, short text, dropdown, or checkbox blocks). You can add Phone capture and Email capture blocks; only one phone capture and one email capture block are allowed per message.

### Title and paragraph

Adds heading or body text with rich text options.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Text color | 
 Modifies the color of the text. | 

### Button

Adds a clickable button. You can set links and analytics options in the properties panel.

 Property | 
 Description | 

 Button width | 
 Modifies the width of the button to be automatic or manual. | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Button alignment | 
 Moves the button to be left, center, or right-oriented. | 

 Button text color | 
 Modifies the color of the text on the button. | 

 Background color | 
 Modifies the color of the button’s background. | 

 Border style | 
 Determines the style of the button’s border. | 

 Border radius | 
 Determines how round the corners are. | 

#### On-click behavior

 Action | 
 Description | 

 Submit form when button is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the button for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the button, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the button updates the user’s profile with custom data. You can also select the identifier for reporting. | 

For more information, see Define on-click behavior in the Banner article.

### Image

Displays an image from a hosted URL. Configure display options in the properties panel.

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

 Property | 
 Description | 

 URL | 
 The hosted address for the image. | 

 Alignment | 
 Moves the image to be left, center, or right-oriented. | 

 Background color | 
 Modifies the color of the image’s background. | 

 Border style | 
 Determines the style of the image’s border. | 

 Border radius | 
 Determines how round the corners of the image are. | 

#### On-click behavior

 Action | 
 Description | 

 Alt text | 
 The written copy that appears in place of an image if the image fails to load. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. | 

 Submit form when image is clicked | 
 Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. | 

 Set separate behaviors for each platform | 
 Customizes the behavior of the image for each platform separately. | 

 On-click behavior | 
 Determines the action when the user clicks the image, such as closing the message, opening a web URL, deep linking into a specific page of the app, going to another page, or requesting push permission. | 

 Log custom attributes or events | 
 Determines whether clicking the image updates the user’s profile with custom data. You can also select the identifier for reporting. | 

### Link

Inserts a hyperlink users can select.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text color | 
 Modifies the color of the text. | 

#### On-click behavior

 Action | 
 Description | 

 URL | 
 The hyperlink to navigate to. | 

 Identifier for Reporting | 
 Determines the identifier for reporting. | 

### Spacer

Adds vertical spacing between blocks.

 Property | 
 Description | 

 Background color | 
 Modifies the background color of the spacer. | 

 Height | 
 Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. | 

### Custom code

Inserts custom HTML for advanced layouts or embedded content (for example video). Clicks inside custom HTML are not tracked unless you call brazeBridge.logClick() — see Custom code and JavaScript bridge for Banners.

 Property | 
 Description | 

 Custom code | 
 Add or edit HTML (and related assets) for the Banner. | 

### Phone capture

Collects a phone number. On submit, subscribes the user to your selected SMS or WhatsApp subscription group. Only one per Banner.

 Property | 
 Description | 

 Subscription group | 
 The SMS or WhatsApp subscription group the user is subscribed to on submit. Includes an option to collect phone numbers from all countries. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder phone number to display. | 

### Email capture

Collects an email address and adds it to the user’s Braze profile on submit. Only one per Banner.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Text color | 
 Modifies the color of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Placeholder text | 
 A placeholder email address to display. | 

### Long text

Multi-line text field for survey-style flows. If you don’t see this block, contact Braze Support or your Braze customer success manager.

 Property | 
 Description | 

 Required input field | 
 Marks whether the field must be filled before the form can be submitted. | 

 Minimum characters | 
 The minimum number of characters a user must enter. | 

 Maximum characters | 
 The maximum number of characters a user can enter. | 

 Hide character count | 
 Hides or shows the live character counter for the text area. | 

 Placeholder text | 
 Text shown inside the empty text area until the user types. | 

 Height (rows of text) | 
 Controls how tall the text area appears, measured in rows. | 

 Font family | 
 Typeface for the text area text. | 

 Font weight | 
 Thickness (such as light, normal, or bold) of the text. | 

 Font size | 
 Size of the text. | 

 Line height | 
 Vertical spacing between lines of text. | 

 Text color | 
 Color of the text. | 

 Letter spacing | 
 Horizontal spacing between characters. | 

## Things to know

- Video: The standard composer does not include a dedicated video block. Use Custom code to embed a player if needed. For more information, see Banners: Frequently Asked Questions.
 
- Liquid: Most Liquid is supported; there are exceptions such as catalog rerender tags. For more information, see Banners: Frequently Asked Questions.

## Preference center editor blocks

Drag blocks from the Build section into a row in the drag-and-drop preference center editor. Each block has its own settings; the right-side panel switches to properties or styling for the selected element.

Before you edit blocks, add subscription groups and configure the subscription smart block (see the following section). For the full setup flow, see Create an email preference center with drag-and-drop.

### Title and paragraph

Adds heading or body copy with rich text options.

 Property | 
 Description | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Line height | 
 Modifies the distance between lines of text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Text alignment | 
 Moves the text to be aligned left, center, right, or justified. | 

 Text color | 
 Modifies the color of the text. | 

### Button

Adds a clickable button (for example Save or navigation).

 Property | 
 Description | 

 Button width | 
 Modifies the width of the button to be automatic or manual. | 

 Font family | 
 The font style for the text. | 

 Font weight | 
 Determines the thickness of the text. | 

 Font size | 
 Determines the size of the text. | 

 Letter spacing | 
 Modifies the distance in between each character. | 

 Button alignment | 
 Moves the button to be left, center, or right-oriented. | 

 Button text color | 
 Modifies the color of the text on the button. | 

 Background color | 
 Modifies the color of the button’s background. | 

 Border style | 
 Determines the style of the button’s border. | 

 Border radius | 
 Determines how round the corners are. | 

### Image

Displays an image from the media library or a URL.

important

If you are pulling in images with Connected Content or Liquid, ensure that your image URL begins with https://. Using http:// will crash your app.

 Property | 
 Description | 

 URL | 
 The hosted address for the image. | 

 Alignment | 
 Moves the image to be left, center, or right-oriented. | 

 Background color | 
 Modifies the color of the image’s background. | 

 Border style | 
 Determines the style of the image’s border. | 

 Border radius | 
 Determines how round the corners of the image are. | 

### Spacer

Adds vertical spacing between blocks.

 Property | 
 Description | 

 Background color | 
 Modifies the background color of the spacer. | 

 Height | 
 Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. | 

### Subscription groups (smart block)

Adds a template block that lists subscription groups, optional Subscribe to all / Unsubscribe from all controls, and descriptions. Configure it after you add groups in the preference center workflow.

After you add subscription groups, select the smart block in the canvas to:

- Reorder subscription groups
 
- Add or remove groups
 
- Add or remove descriptions
 
- Toggle Subscribe to all and Unsubscribe from all for the groups in that block

The Unsubscribe from all control at the bottom of the default template is required and performs a global unsubscribe from email.

## Things to know

- Common styles: You can set page-wide defaults under Common Styles before adjusting individual blocks. For more information, see Customize the preference center using the drag-and-drop editor.
 
- Confirmation page: Switch to Confirmation Page at the top of the editor to style the post-save experience using the same block types.

- 

New Stuff!
