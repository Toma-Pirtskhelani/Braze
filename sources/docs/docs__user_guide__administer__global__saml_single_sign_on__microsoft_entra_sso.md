---
url: https://www.braze.com/docs/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso
slug: docs__user_guide__administer__global__saml_single_sign_on__microsoft_entra_sso
title: "Microsoft Entra SSO"
description: "This article walks you through how to set up Microsoft Entra single sign-on capabilities with Braze."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Microsoft Entra SSO

Microsoft Entra SSO is Microsoft’s cloud-based identity and access management service, which helps your employees sign in and access resources. You can use Entra SSO to control access to your apps and your app resources, based on your business requirements.

## Requirements

Upon setup, you are asked to provide an Assertion Consumer Service (ACS) URL.

 Requirement | 
 Details | 

 Assertion Consumer Service (ACS) URL | 
 https://<SUBDOMAIN>.braze.com/auth/saml/callback 
 For some identity providers, this can also be referred to as the Reply URL, Audience URL, or Audience URI. | 

 Entity ID | 
 braze_dashboard by default. 

 To give this dashboard a unique Entity ID, enable a custom Entity ID and use the generated value (braze_dashboard_<COMPANY_ID>) instead. For steps, refer to Using a custom Entity ID. | 

 RelayState API key | 
 To enable identity provider login, go to Settings > API Keys and create an API key with sso.saml.login permissions. | 

## Service Provider (SP) initiated login within Microsoft Entra SSO

### Step 1: Add Braze from the gallery

- In your Microsoft Entra admin center, go to Identity > Applications > Enterprise Applications, and then select New application.
 
- Search for Braze in the search box, select it from the result panel, and then select Add.

### Step 2: Configure Microsoft Entra SSO

- In your Microsoft Entra admin center, go to your Braze application integration page and select Single sign-on.
 
- On the Select a single sign-on method page, select SAML as your method.
 
- On the Set up Single Sign-On with SAML page, select the edit icon for Basic SAML Configuration.
 
- Configure the application in IdP-initiated mode by entering a Reply URL that combines your Braze instance with the following pattern: https://<SUBDOMAIN>.braze.com/auth/saml/callback.
 
- In the same Basic SAML Configuration section, leave Identifier (Entity ID) set to braze_dashboard unless you’re using a custom Entity ID. In that case, enter your dashboard’s generated value (braze_dashboard_<COMPANY_ID>) so it matches the value shown in your Braze security settings.
 
- Configure RelayState by entering your Relay State generated API key into the Relay State field.

important

Do not set the Sign-On URL field. Leave this field blank to prevent issues with your IdP-initiated SAML SSO.

- Format SAML assertions in the specific format expected by Braze. Refer to the following tabs on user attributes and user claims to understand how these attributes and values must be formatted.

- user attributes
 
- user claims

You can manage the values of these attributes from the User Attributes section on the Application Integration page.

Use the following attribute pairings:

- givenname = user.givenname
 
- surname= user.surname
 
- emailaddress = user.mail
 
- name = user.userprincipalname
 
- email = user.userprincipalname
 
- first_name = user.givenname
 
- last_name = user.surname
 
- Unique User Identifier = user.userprincipalname

important

The email field must match what is set up for your users in Braze. In most cases, this is the same as user.userprincipalname; however, if you have a different configuration, work with your system administrator to ensure that these fields match exactly.

On the Set up Single Sign-On with SAML page, select Edit to open the User Attributes dialog. Then, edit the user claims according to the proper format.

Use the following claim name pairings:

- claims/givenname = user.givenname
 
- claims/surname = user.surname
 
- claims/emailaddress = user.userprincipalname
 
- claims/name = user.userprincipalname
 
- claims/nameidentifier = user.userprincipalname

important

The email field must match what is set up for your users in Braze. In most cases, this is the same as user.userprincipalname; however, if you have a different configuration, work with your system administrator to ensure that these fields match exactly.

You can manage these user claims and values from the Manage claim section.

- Go to the Set up Single Sign-On with SAML page, then scroll to the SAML Signing Certificate section and download the appropriate Certificate (Base64) based on your requirements.
 
- Go to the Set up Braze section and copy the appropriate URLs for use in the Braze configuration.

### Step 3: Configure Microsoft Entra SSO within Braze

After you’ve set up Braze within Microsoft Entra admin center, Microsoft Entra provides a target URL (login URL) and x.509 certificate, which you input into your Braze account.

After your account manager has enabled SAML SSO for your account, do the following:

- Go to Settings > Company Settings > Admin Settings > Security Settings and toggle the SAML SSO section to ON.
 
- On the same page, add the following:

 Requirement | 
 Details | 

 SAML Name | 
 This will appear as the button text on the login screen. This is typically your identity provider’s name, like “Microsoft Entra.” | 

 Target URL | 
 This is the login URL provided by Microsoft Entra. | 

 Certificate | 
 The x.509 PEM encoded certificate is provided by your identity provider. | 

tip

If you want your Braze account users to only sign in with SAML SSO, you can restrict single sign-on authentication on the Security Settings page under Authentication Rules.

- 

New Stuff!
