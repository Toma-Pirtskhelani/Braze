---
url: https://www.braze.com/docs/developer_guide/platforms/web/accessibility
slug: docs__developer_guide__platforms__web__accessibility
title: "Accessibility"
description: "This article describes how Braze supports accessibility."
section: developer_guide/platforms
fetched: 2026-09-02
evidence: company-own (technical)
---
# Accessibility

This article provides an overview of how Braze supports accessibility within your integration.

Braze Web SDK supports the standards provided by the Web Content Accessibility Guidelines (WCAG 2.1). We maintain a 100/100 lighthouse score for content cards and in-app messages on all of our new builds to uphold our accessibility standard.

## Prerequisites

The minimum SDK version that satisfies WCAG 2.1 is close to v3.4.0. However, we recommend upgrading to at least v6.0.0 for major image tag fixes.

### Notable accessibility fixes

 Version | 
 Type | 
 Key changes | 

 6.0.0 | 
 Major | 
 Images as <img> tags, imageAltText or language fields, general UI accessibility improvements | 

 3.5.0 | 
 Minor | 
 Scrollable text accessibility improvements | 

 3.4.0 | 
 Fix | 
 Content Cards article role fix | 

 3.2.0 | 
 Minor | 
 45x45px minimum touch targets for buttons | 

 3.1.2 | 
 Minor | 
 Default alt text for images | 

 2.4.1 | 
 Major | 
 Semantic HTML (h1 or button), ARIA attributes, keyboard navigation, focus management | 

 2.0.5 | 
 Minor | 
 Focus management, keyboard navigation, labels | 

## Supported accessibility features

We support these features for content cards and in-app messages:

- ARIA roles and labels
 
- Keyboard navigation support
 
- Focus management
 
- Screen reader announcements
 
- Alt text support for images

## Accessibility guidelines for SDK integrations

Refer to Building accessible messages in Braze for general accessibility guidelines. This guide provides tips and best practices for maximum accessibility when integrating the Braze Web SDK into your web application.

### Content Cards

#### Setting a maximum height

To prevent Content Cards from taking up too much vertical space and improve accessibility, you can set a maximum height on the feed container, such as in this example:

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

```
 | 
```
/* Limit the height of the Content Cards feed */
.ab-feed {
 max-height: 600px; /* Adjust to your needs */
 overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
 max-height: 400px; /* Optional: limit individual card height */
 overflow: hidden;
}

```
 | 

#### Viewport considerations

For Content Cards that are displayed inline, consider viewport constraints, such as in this example.

```

1
2
3
4
5
6

```
 | 
```
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
 body > .ab-feed {
 max-height: 80vh; /* Leave space for other content */
 }
}

```
 | 

### In-app messages

warning

Do not put important information within slide up in-app messages, as they are not accessible for screen readers.

### Mobile considerations

#### Responsive design

The SDK includes responsive breakpoints. Confirm that your customizations work across screen sizes, such as in this example:

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
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
 /* Ensure readable font sizes */
 .ab-feed {
 font-size: 14px; /* Minimum 14px for mobile readability */
 }
 
 /* Ensure sufficient touch targets */
 .ab-card {
 padding: 16px; /* Adequate padding for touch */
 }
}

```
 | 

### Testing accessibility

#### Manual test checklist

Manually test your accessibility by completing these tasks:

- Navigate Content Cards and in-app messages with keyboard only (Tab, Enter, Space)
 
- Test with screen reader (NVDA, JAWS, VoiceOver)
 
- Verify all images have alt text
 
- Check color contrast ratios (use tools like WebAIM Contrast Checker)
 
- Test on mobile devices with touch
 
- Verify focus indicators are visible
 
- Test modal message focus trapping
 
- Verify all interactive elements are reachable by a keyboard

### Common accessibility issues

To avoid common accessibility issues, do the following:

- Keep focus styles: The SDK’s focus indicators are essential for keyboard users.
 
- Only use display: none on non-interactive elements: Use visibility: hidden or opacity: 0 to hide interactive elements.
 
- Don’t override ARIA attributes: The SDK sets appropriate ARIA roles and labels.
 
- Use tabindex attributes: These control keyboard navigation order.
 
- Provide a scroll if you set overflow: hidden: Confirm that scrollable content remains accessible.
 
- Don’t interfere with built-in keyboard handlers: Confirm that existing keyboard navigation works.

- 

New Stuff!
