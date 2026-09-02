---
url: https://www.braze.com/docs/user_guide/channels/email/inbox_vision
slug: docs__user_guide__channels__email__inbox_vision
title: "Inbox Vision"
description: "This page covers how to set up Inbox Vision, a feature that allows marketers to view their emails from the perspective of various email clients..."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Inbox Vision

Inbox Vision lets you view your emails from the perspective of various email clients and mobile devices. For example, you can test dark and light mode differences to confirm your emails render as intended.

important

Inbox Vision may not work if your email content relies on templating information such as user profile data. Braze templates an empty user when sending emails for this feature.

Add default values to any Liquid in your email message. Without defaults you may receive a false positive or the test may fail.

## Considerations

In general, your email won’t work with Inbox Vision if your email content relies on templating information, such as user profile information. This is because Braze templates an empty user when we send emails using this feature.

You can resolve this by adding default values or any values to the Liquid in your email message before you run Inbox Vision. When you finish testing in Inbox Vision, the original email message appears. If no values are provided, the test may fail to render the previews successfully.

Your company has a limit on how many emails you can preview with Inbox Vision. You can monitor this in the Email Previews tab of Inbox Vision.

Include a subject line and a valid sending domain to view previews. Be mindful of desktop versus mobile rendering differences. Use the previews to confirm the email appears as intended.

note

If previewing a campaign shows a permission error, clear your cache and cookies, or try an incognito window. Browser extensions sometimes block the preview.

To test your email message in Inbox Vision:

- Go to your drag-and-drop editor or HTML email editor.
 
- In your editor, select Preview & Test.
 
- Select Inbox Vision.
 
- Select Run Inbox Vision. This takes up to ten minutes.
 
- Next, select a tile to view the preview in more detail. These previews are grouped into these sections: Web Clients, Application Clients, and Mobile Clients.

- Select Run Inbox Vision. This may take between two to ten minutes to complete.

note

Inbox Vision doesn’t support email messages that include abort logic because these emails render as static content.

### Previewing as a user

When you preview as a random user, Inbox Vision doesn’t save user-specific settings or attributes (such as name or preferences). When you select a custom user, the Inbox Vision preview may differ from other previews because it uses specific user data.

## Code analysis

Code analysis highlights potential HTML issues, shows the number of occurrences, and indicates unsupported HTML elements.

### Viewing code analysis information

Find this information on the Inbox Vision tab by selecting List view. List view is available only for HTML email templates. For drag-and-drop templates, use previews to resolve issues instead.

note

Code analysis can appear faster than the preview for a particular client because Braze waits until the email arrives before taking the screenshot.

## Spam testing

Spam testing estimates whether mail might be filtered as spam. Tests run across filters such as IronPort, SpamAssassin, and Barracuda, and ISP filters such as Gmail and Outlook, using static seed inboxes that don’t open or click by default.

important

Inbox placement is driven mainly by live recipient engagement. Spam test results may not match what you see from real campaigns.

For a clearer read on deliverability, test content with small live cohorts—strong opens and clicks are the most reliable signal. Use spam tests as one input alongside engagement monitoring.

### Viewing spam test results

To check your spam test results:

- Select the Spam Testing tab in the Inbox Vision section. The Spam Test Result table lists the spam filter name, status, and type.
 
- Review these results and make any adjustments to your email campaign.
 
- Select Re-run Test to reload your spam test results.

## Accessibility testing

Accessibility testing highlights potential accessibility issues in your email and shows which elements don’t meet standards. Braze analyzes content against select Web Content Accessibility Guidelines (WCAG), a set of internationally recognized standards developed by the W3C to make web content more accessible.

### How it works

When you run Inbox Vision, Braze automatically checks for common accessibility issues in the WCAG 2.2 AA rule set (such as missing alt text, insufficient color contrast, improper heading structure) and categorizes severity to help you prioritize fixes. Note that even when alt text is present, how it displays is controlled by the recipient’s email client, not Braze.

important

Accessibility Testing may be used to support Customer’s compliance efforts of regulations or laws such as the European Accessibility Act; however, Customer acknowledges that Braze makes no representations or warranties with respect to whether or not use of Accessibility Testing satisfies Customer’s compliance obligations, and disclaims all liability in relation thereto.

### Viewing accessibility testing results

Accessibility testing generates results for each rule as passed, failed, or needs review in the Accessibility Testing tab. Braze categorizes each rule using POUR (Perceivable, Operable, Understandable, Robust), the four principles behind WCAG.

#### POUR categories

Inbox Vision categorizes issues under the four foundational POUR principles: Perceivable, Operable, Understandable, and Robust.

 Principle | 
 Definition | 

 Perceivable | 
 Information and user interface components must be presentable to users in ways they can perceive.

Users must be able to perceive the information being presented (it can’t be invisible to all of their senses). | 

 Operable | 
 User interface components and navigation must be operable.

Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). | 

 Understandable | 
 Information and the operation of the user interface must be understandable.

Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). | 

 Robust | 
 Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.

Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). | 

#### Severity levels

Inbox Vision classifies accessibility issues by severity to help you prioritize remediation.

 Status | 
 Definition | 

 Critical | 
 Issues that can block access to content or functionality for users with disabilities. These are the most severe and should be prioritized for fixing. | 

 Serious | 
 Issues that can cause significant barriers but may not completely block access. These should be addressed promptly. | 

 Moderate | 
 Issues that may cause some difficulty for users with disabilities, but are less likely to block access entirely. | 

 Minor | 
 Issues that have a relatively low impact on accessibility and may cause only minor inconvenience. | 

 Needs review | 
 Unable to detect if there might be an issue or not. This can occur when we are unable to determine the contrast ratio as the text is placed on a background image. You must manually review because it cannot be automatically determined. | 

 Passed | 
 Passed WCAG A, AA, or accessibility best practice. | 

important

The drag-and-drop editor does not support setting a document <title> element, so the accessibility scanner always fails this check.

This limitation is tracked for future improvements. If you have feedback about the drag-and-drop editor document title limitation in Inbox Vision, open the Support menu in the global header and select Share feedback to send us your thoughts.

### Understanding automated accessibility testing

Automated accessibility testing helps catch common issues like missing alt text or low color contrast based on WCAG Level AA standards. It’s a powerful starting point for building more inclusive messages.

But automation can’t catch everything. Some issues need a human eye—like whether the focus order makes sense, if links and buttons are clearly labeled, or if your instructions are easy to follow. Think of these checks as a diagnostic tool, not a final verdict. We recommend reviewing flagged issues manually and using your best judgment when something is marked as “Needs review.”

For extra support, our Accessibility at Braze guide shares practical tips for making your content easier for everyone to use, including:

- Headings and structure
 
- Alt text and images
 
- Links and buttons
 
- Color contrast
 
- Touch targets

When you combine automated testing with thoughtful manual review, you’ll catch more issues—and create a better experience for all your users.

## Best practices

### Review your email subscriber list

Reference the email insights dashboard to determine the most popular device type and providers where your subscribers are engaging.

If you need more granularity, such as the browser, device model, and more, you can leverage your Currents data or Query Builder to retrieve this level of detail about your users’ recent email engagement.

### Select meaningful previews and impacted previews

If your business is primarily based in the US, there may be specific previews, such as international previews like GMX.de, that are only used by a nominal number of users. We recommend prioritizing and optimizing for inboxes with a sizable subscriber impact and reserving your previews for higher-impact inboxes.

When making fixes that affect specific previews, be sure to select only the impacted previews to prevent consuming unused previews.

### Run Inbox Vision on the final email version

We suggest running Inbox Vision when the email message is production-ready or close to it. This allows you to reduce the number of generated previews, as the email goes through multiple iterations before it’s finalized and ready to be sent to users.

Running Inbox Vision every time you make a single edit or change can quickly consume previews. We suggest making all the necessary changes to the email first, and then running Inbox Vision to preview how all your changes can affect the rendering of your email across environments.

Braze runs tests through actual email clients and works to ensure renderings are accurate. Braze defaults to the top 20 previews based on general industry and expert data, which covers the majority of where your users are engaging with your emails. If your data analysis points to other, more popular previews, you can define a default set of previews every time you run Inbox Vision.

If you consistently see an issue with a client, open a support ticket.

### Test accuracy versus live inboxes

A sent message can look different from the editor preview because providers interpret the same HTML differently. Download a copy of the sent HTML to compare, and use CSS inlining where clients strip <style> blocks.

#### Blank email bodies

If recipients report blank email bodies but can still see the sender name or subject line:

- Confirm which email clients are affected.
 
- Use Inbox Vision to test the variant in those clients and identify HTML or CSS compatibility issues.
 
- If a client strips <style> blocks, add style attributes to the affected HTML elements. For more on inlining behavior and its limitations, see CSS inlining. In Gmail, too much CSS can cause the entire <style> block to be dropped, which is a common cause of blank email bodies.
 
- In the HTML editor, you can also turn on Enable inline CSS under Sending Info > Advanced to inline stylesheet rules for the entire message. This option isn’t available for drag-and-drop emails, which are already inlined by the editor.
 
- Retest in Inbox Vision before sending future campaigns.

- 

New Stuff!
