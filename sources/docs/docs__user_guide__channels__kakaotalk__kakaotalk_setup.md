---
url: https://www.braze.com/docs/user_guide/channels/kakaotalk/kakaotalk_setup
slug: docs__user_guide__channels__kakaotalk__kakaotalk_setup
title: "Set up KakaoTalk"
description: "This reference article outlines how to set up your KakaoTalk channel, including how to set up users, reconcile user IDs, and create test users."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Set up KakaoTalk

This article covers how to set up the KakaoTalk messaging channel in Braze, including how to set up users, reconcile user IDs, and create KakaoTalk test users.

## Prerequisites

 Requirement | 
 Description | 

 Account with a supported KakaoTalk partner | 
 An account with a supported KakaoTalk partner, CJ OliveNetworks or Infobip, is required to use the KakaoTalk messaging channel. | 

 KakaoTalk Business channel | 
 Your KakaoTalk account must be a KakaoTalk Business channel to send KakaoTalk messages through Braze. When you create an account, its default status is basic. To make your account a Business channel, you’ll need to verify your business and provide relevant documentation. | 

 KakaoTalk Sender Key | 
 A valid KakaoTalk Sender Key. | 

 Contact phone number | 
 A contact phone number for your KakaoTalk channel’s administrator. | 

 Braze cluster IPs allowlisted | 
 IP allowlist registration is required for all customers. Register the Braze IP addresses for your cluster before you integrate KakaoTalk in Braze. | 

### Register Braze IP addresses

Register the Braze IP addresses for your cluster in your Comm.One dashboard.

- In your Comm.One dashboard, go to Account Management (계정 관리), select the menu icon, then select View Details (자세히보기).
 
- Select Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트).
 
- Add the IP addresses for your Braze cluster. For the complete list of IPs by cluster, see IP allowlisting.

### Types of KakaoTalk accounts

 Account type | 
 Description | 

 Basic channel | 
 A standard KakaoTalk channel that any organization can set up. It enables broadcast messaging and 1:1 chat through KakaoTalk. | 

 Business channel | 
 An upgraded, business-verified KakaoTalk channel that requires an application and verification process. It offers enhanced features, such as 
- Verified badge
- Appearance as a recommended channel
- Support for business messaging | 

#### Apply for a business channel

Before starting the application, gather the following business documentation:

- Korean Business Registration Certificate
 
- ID of the Business Representative
 
- Employment Certificate
 
- Industry-specific Licenses

important

The information on your KakaoTalk Channel (such as channel name, profile image, and others) must exactly match the information on your official submitted documents.

After gathering your documentation, follow these steps:

- Log into the KakaoTalk Channel Admin Center.
 
- Select the existing KakaoTalk channel you wish to upgrade.
 
- In the Management (관리) section, select the option for Business Channel Application (비즈니스 채널 신청).
 
- Select the Apply or Request button (신청) to begin the process.
 
- Provide the required information.
 
- Wait for a notification with the review results.

## Integrate KakaoTalk

### Connect the KakaoTalk channel to Braze

- Go to Partner Integrations > Technology Partners and select your KakaoTalk provider.
 
- Gather the required credentials for your provider (See the following section), then enter them into the Technology Partners page and save.
 
- Use the newly saved credentials for sending.

#### CJ OliveNetworks

Go to your Comm.One dashboard and gather the following information.

 Field | 
 Location | 

 Comm.One Login ID (로그인 아이디) | 
 Select your profile. | 

 Sender Key (발신프로필 키) | 
 Go to Template Management (템플릿 관리) > Sender Profile Management (발신프로필 관리). | 

 Channel name (카카오톡 채널 프로필명) | 
 In your Comm.One dashboard, go to Template Management (템플릿 관리) > Sender Profile Management (발신프로필 관리). | 

 Sender number (연락처) | 
 
- Go to Account Management (계정 관리), select the menu icon, then select View Details (자세히보기).
- Go to Business Detailed Information (업체 상세 정보) > Company Information (기업정보) | 

 Credential (ID) & Password (비밀번호) | 
 Go to the same location for the Sender number (사업자 등록번호), then go to API > Brand Message (브랜드 메시지). | 

- comm.one login id (로그인 아이디)
 
- sender key (발신프로필 키)
 
- channel name (카카오톡 채널 프로필명)
 
- credential (id) & password (비밀번호)

important

You can integrate a KakaoTalk Sender Key into only one workspace at a time. To use the same Sender Key in a different workspace, you must first archive the KakaoTalk subscription group in the original workspace, then contact Braze Support to remove the integration. After Braze removes the integration, you can set up the integration in the new workspace.

note

Only the channels mapped to a single common ID can be registered.

#### Infobip

Go to your Infobip dashboard and the KakaoTalk Channel Admin Center to gather the following information.

 Field | 
 Location | 

 API Base URL | 
 In the Infobip portal, go to Developer Tools > API Keys. | 

 API Key | 
 In the Infobip portal, go to Developer Tools > API Keys. | 

 Sender name / Sender key | 
 In the Infobip portal, go to Channels and Numbers > Channels, then select the Senders tab. | 

 Sender profile UUID | 
 In the KakaoTalk Channel Admin Center, go to Channels and find the Search ID in the channel information window. | 

 Channel name | 
 In the KakaoTalk Channel Admin Center, find the channel name in the same channel information window. | 

##### API key and base URL

- In the Infobip portal, select Developer Tools > API Keys.
 
- On the API keys page, copy the API base URL.

- Select CREATE API KEY.
 
- Enter the Name, select the Expiration date, then select the API scopes required for KakaoTalk. These scopes control which Infobip API actions your key can perform.

- Select CREATE to generate the key.
 
- Copy the generated key. You can return to this page to update the name, expiration date, or API scopes.

##### Sender profile UUID and channel name

- In the KakaoTalk Channel Admin Center, select Channels.
 
- In the Channel Information window, find the Channel name and Search id (sender UUID).
 
- Enter the Customer center contact information. This is required when sending ad messages.

- To view a different channel, select the channel icon at the top of the menu.
 
- In the My channel list, select the channel you want to view, then repeat the previous steps.

## Set user profiles

User profiles must have phone numbers in E.164 format to message them through KakaoTalk. Phone numbers are shown on the user profile. KakaoTalk requires phone numbers to be in E.164 format (for example, +821025749774). This differs from some other messaging channels that may accept phone numbers in multiple formats.

### Import phone numbers

Import phone numbers by uploading a CSV or using the API to create a user. Ensure phone numbers are in E.164 format before importing.

- 

New Stuff!
