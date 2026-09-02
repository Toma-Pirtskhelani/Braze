---
url: https://www.braze.com/docs/api/endpoints/apps/post_update_push_credential
slug: docs__api__endpoints__apps__post_update_push_credential
title: "Update push credentials"
description: "This article outlines details about the Update push credentials Braze endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Update push credentials

post

/apps/push_credential/update

core endpoint

Use this endpoint to programmatically update the push credentials for a single app, so you can manage credentials without using the dashboard UI.

Each request updates the push credentials for one app and one push platform. Credential files, such as the iOS authentication key or the Firebase service account, are passed as Base64-encoded strings inside the JSON request body.

This endpoint supports the following push platforms:

 Platform | 
 Credentials | 

 iOS (APNs) | 
 .p8 authentication key only. .p12 and .pem certificates aren’t supported by this endpoint. | 

 Android (Firebase Cloud Messaging) | 
 Service account JSON | 

 Android (Huawei Mobile Services) | 
 App ID and app secret | 

 Kindle (Amazon Device Messaging) | 
 Client ID and client secret | 

## Prerequisites

To use this endpoint, you’ll need an API key with the apps.push_credential permission.

## Request body

```

1
2

```
 | 
```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY

```
 | 

Include one platform object per request: apple, firebase, huawei, or kindle.

- ios (apns)
 
- android (firebase cloud messaging)
 
- android (huawei mobile services)
 
- kindle (amazon device messaging)

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
{
 "app_id": (required, string) the app identifier API key found under Settings > App Settings,
 "apple": {
 "certificate": (required, string) the Base64-encoded .p8 authentication key,
 "jwt_key_id": (required, string) the key ID for the .p8 authentication key,
 "jwt_team_id": (required, string) your Apple Developer team ID,
 "jwt_bundle_id": (required, string) your app's bundle ID,
 "apns_gateway": (required, string) either "prod" or "dev"
 }
}

```
 | 

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
{
 "app_id": (required, string) the app identifier API key found under Settings > App Settings,
 "firebase": {
 "credential": (required, string) the Base64-encoded Firebase service account JSON
 }
}

```
 | 

```

1
2
3
4
5
6
7

```
 | 
```
{
 "app_id": (required, string) the app identifier API key found under Settings > App Settings,
 "huawei": {
 "app_id": (required, string) your Huawei app ID,
 "app_secret": (required, string) your Huawei app secret
 }
}

```
 | 

```

1
2
3
4
5
6
7

```
 | 
```
{
 "app_id": (required, string) the app identifier API key found under Settings > App Settings,
 "kindle": {
 "client_id": (required, string) your Amazon Device Messaging client ID,
 "client_secret": (required, string) your Amazon Device Messaging client secret
 }
}

```
 | 

## Request parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 app_id | 
 Required | 
 String | 
 The app identifier API key for the app you want to update. Find it in the dashboard under Settings > App Settings, next to the API Key field. | 

 apple | 
 Required* | 
 Object | 
 The iOS (APNs) credentials. | 

 firebase | 
 Required* | 
 Object | 
 The Android (Firebase Cloud Messaging) credentials. | 

 huawei | 
 Required* | 
 Object | 
 The Android (Huawei Mobile Services) credentials. | 

 kindle | 
 Required* | 
 Object | 
 The Kindle (Amazon Device Messaging) credentials. | 

* Include exactly one platform object per request.

### iOS (APNs) parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 certificate | 
 Required | 
 String | 
 The Base64-encoded .p8 authentication key. Only .p8 authentication keys are supported; .p12 and .pem certificates aren’t supported by this endpoint. | 

 jwt_key_id | 
 Required | 
 String | 
 The key ID for the .p8 authentication key. | 

 jwt_team_id | 
 Required | 
 String | 
 Your Apple Developer team ID. | 

 jwt_bundle_id | 
 Required | 
 String | 
 Your app’s bundle ID. | 

 apns_gateway | 
 Required | 
 String | 
 The APNs environment. Available values are prod and dev. | 

### Android (Firebase Cloud Messaging) parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 credential | 
 Required | 
 String | 
 The Base64-encoded Firebase service account JSON. | 

### Android (Huawei Mobile Services) parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 app_id | 
 Required | 
 String | 
 Your Huawei app ID. | 

 app_secret | 
 Required | 
 String | 
 Your Huawei app secret. | 

### Kindle (Amazon Device Messaging) parameters

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 client_id | 
 Required | 
 String | 
 Your Amazon Device Messaging client ID. | 

 client_secret | 
 Required | 
 String | 
 Your Amazon Device Messaging client secret. | 

## Example requests

### iOS (APNs)

The apple.certificate value must be Base64-encoded, and apple.apns_gateway must be set to either prod or dev.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "app_id": "{YOUR_APP_IDENTIFIER}",
 "apple": {
 "certificate": "{BASE64_ENCODED_STRING}",
 "jwt_key_id": "{YOUR_KEY_ID}",
 "jwt_team_id": "{YOUR_TEAM_ID}",
 "jwt_bundle_id": "{YOUR_BUNDLE_ID}",
 "apns_gateway": "prod"
 }
}'

```
 | 

### Android (Firebase Cloud Messaging)

The firebase.credential value must be Base64-encoded.

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

```
 | 
```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "app_id": "{YOUR_APP_IDENTIFIER}",
 "firebase": {
 "credential": "{BASE64_ENCODED_STRING}"
 }
}'

```
 | 

### Android (Huawei Mobile Services)

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
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "app_id": "{YOUR_APP_IDENTIFIER}",
 "huawei": {
 "app_id": "{YOUR_HUAWEI_APP_ID}",
 "app_secret": "{YOUR_HUAWEI_APP_SECRET}"
 }
}'

```
 | 

### Kindle (Amazon Device Messaging)

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
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
 "app_id": "{YOUR_APP_IDENTIFIER}",
 "kindle": {
 "client_id": "{YOUR_ADM_CLIENT_ID}",
 "client_secret": "{YOUR_ADM_CLIENT_SECRET}"
 }
}'

```
 | 

## Example response

If the credentials are updated successfully, you’ll receive a response with the status code 201.

```

1
2
3

```
 | 
```
{
 "message": "success"
}

```
 | 

- 

New Stuff!
