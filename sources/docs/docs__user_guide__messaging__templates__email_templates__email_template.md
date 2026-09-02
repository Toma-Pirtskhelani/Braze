---
url: https://www.braze.com/docs/user_guide/messaging/templates/email_templates/email_template
slug: docs__user_guide__messaging__templates__email_templates__email_template
title: "Create an email template"
description: "This reference article covers how to create, customize, and manage email templates."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Create an email template

The Braze dashboard has an email template editor that allows you to create custom-tailored, eye-catching emails and save them for later use in campaigns. You can also upload your own HTML email template.

## Step 1: Navigate to the email template editor

In the Braze dashboard, go to Content > Email.

## Step 2: Select your editing experience

Select between Drag-and-drop Editor or HTML code editor for your editing experience.

You can also choose from predesigned Braze templates, create a new template, or edit an existing template (plain or mobile responsive).

note

Any existing custom HTML templates must be re-created using the drag-and-drop editor.

## Step 3: Customize your template

After selecting your editor experience, this is your opportunity to get creative with customizing your email template. You can use HTML to create and emulate your branding in the HTML editor, or include a variety of creative details in the drag-and-drop editor.

### Include an unsubscribe link

As you design your email template, if you do not include an unsubscribe link, Braze will prompt you to add this in your email as it’s required by law on all marketing emails. You can add this unsubscribe link as a footer at the bottom of your emails by using the Liquid tag ${email_footer}, or by customizing the footer in your template.

## Step 4: Check for email errors

Email errors are presented on the Compose tab of the message workflow. Errors prevent you from progressing forward. “Warnings” indicate reminders to help you follow best practices. Depending on your business, you might choose to ignore them.

Here’s a list of errors that are accounted for in our editor:

- Incorrect Liquid syntax
 
- Email bodies larger than 400kb; bodies are highly recommended to be less than 102kb
 
- Templates without an unsubscribe link
 
- Emails with a blank Body or Subject
 
- Emails with no unsubscribe link

## Step 5: Preview and test your message

After you finish composing your template, you can test it before sending it out.

From the bottom of the overview screen, select Preview and Test. Here, you can preview how your email will appear in a customer’s inbox. With Preview as User selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

Then, you can Copy preview link to generate and copy a shareable preview link that shows what the email looks like for a random user. For more information, see Shareable preview.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message appears in different contexts.

tip

Curious about what your email looks like for dark mode users? Select the Dark Mode Preview toggle located in the Preview and Test section (drag-and-drop editor only).

When you’re ready for a final check, select Test Send and send a test message to yourself or a group of content testers to ensure that your email displays properly on a variety of devices and email clients.

If you see any issues with your template or want to make any changes, select Edit Email to return to the editor. Note that edits made in the Classic editor may not be reflected in the HTML editor or the email preview.

## Step 6: Save your template

Be sure to save your template by selecting Save Template. You’re now ready to use this template in any campaign or Canvas component you choose. To access your template, select the editing experience you built it with, and then select it from the list of available templates.

note

If you make any edits to an existing template, those changes will not be reflected in campaigns created using previous versions of that template.

### Manage your templates

You can view email templates at Templates > Email Templates, filtering by status, type, tags, the user who created it, or searching by template name. You need the relevant user permissions, such as View Email Templates, to view these templates. For more details, see User permissions.

As you create more email templates, you can duplicate and archive email templates. Learn more about creating and managing your library of templates and creative content in Templates and Media.

### Use your templates in API campaigns

To use your email for an API campaign, you need an email_template_id, which can be found at the bottom of any email template created in Braze.

### Comment on email templates

You can collaborate and comment on email templates in the drag-and-drop editor.

- Select the Content Block or row in the email body that you’d like to comment on.
 
- Select the comment icon.
 
- Enter your comment in the sidebar, then select Submit.
 
- After entering your comments, select Done.
 
- Select Save Template to save your comments.

After your template is saved, users can see icons over unaddressed comments. Select Resolve to resolve these comments.

For answers to frequently asked questions about email templates, check out our Templates FAQ.

- 

New Stuff!
