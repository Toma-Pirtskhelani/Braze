---
url: https://www.braze.com/docs/partners/additional_channels_and_extensions/extensions/learning/edume
slug: docs__partners__additional_channels_and_extensions__extensions__learning__edume
title: "eduMe"
description: "This reference article outlines the partnership between Braze and eduMe, a mobile-based training tool that allows you to leverage Braze Connected Content to give your..."
section: partners/additional_channels_and_extensions
fetched: 2026-09-02
evidence: company-own (technical)
---
# eduMe

eduMe is a mobile-based training tool that gives your workforce the knowledge they need to succeed, when they need it, wherever they are.

This integration is maintained by eduMe.

## About the integration

The Braze and eduMe integration leverages Braze Connected Content to give your users access to eduMe courses and lessons in your Braze campaigns. Individual and group progress can then be tracked through eduMe reporting functionality.

## Prerequisites

 Requirement | 
 Description | 

 eduMe account | 
 An eduMe account is required to take advantage of this partnership. | 

 eduMe API key | 
 You must request an API key from your eduMe customer success contact. This key is used in your Braze Connected Content call. | 

 eduMe link signing secret | 
 You must request your customer success contact at eduMe to set up a link signing secret for your organization. This secret is used to enable seamless links in Connected Content. You not have to do anything with this secret. | 

 eduMe group and content IDs | 
 These identifiers are needed to set up your Connected Content calls. Contact your eduMe customer service contact for help obtaining these identifiers. | 

## Integration

### Create your Connected Content call

To give a user access to a course, lesson, or eNPS survey, and to track their progress against your internal user ID in eduMe, follow the API call shown in this example:

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

```
 | 
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
 https://connect.edume.com/
 EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
 :headers {
 "x-api-key": "YOUR-EDUME-API-KEY"
 }
%}

```
 | 

- Replace YOUR-EDUME-API-KEY with your eduMe API key.

- Replace the EDUME-CONTENT-LINK-AND-CONTENT-ID with the corresponding content link string and module, lesson, or survey identifier. These identifiers can be found in your eduMe account.

- Course: getCourseLink?moduleId=12087
 
- Lesson: getLessonLink?lessonId=25805
 
- eNPS survey: getSurveyLink?surveyId=654

- Users who arrive at eduMe through this link are added to an eduMe team or group of your choosing. Replace groupId with the relevant team ID or eduMe group ID. You typically use the team ID except for courses that require enrollment, in which case you should use the group ID

- Include an appropriate field to map the externalUserId field to. The example connected content call uses the driver_id, though your field will likely be different. This ID is available in eduMe reports, allowing you to correlate them with your systems.

- Lastly, customize and test your message as needed. We recommend you send at least one test message, access the eduMe content, complete the lesson or course, and verify the eduMe analytics are being recorded.

- 

New Stuff!
