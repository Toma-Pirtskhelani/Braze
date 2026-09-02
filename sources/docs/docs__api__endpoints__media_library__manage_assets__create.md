---
url: https://www.braze.com/docs/api/endpoints/media_library/manage_assets/create
slug: docs__api__endpoints__media_library__manage_assets__create
title: "Upload an asset to the media library"
description: "This article outlines details about the `POST /media_library/create` endpoint."
section: api/endpoints
fetched: 2026-09-02
evidence: company-own (technical)
---
# Upload an asset to the media library

post

/media_library/create

Use this endpoint to add an asset to the Braze media library using either an externally hosted URL (asset_url) or binary file data sent in the request body (asset_file). This endpoint supports images, documents, and ZIP files that contain them. For the full list, refer to Supported file types.

## Supported file types

This endpoint accepts the following file types, whether you upload them through asset_url or asset_file.

 Asset type | 
 Supported file types | 
 Maximum size | 

 Image | 
 GIF, ICO, JPEG, JPG, PNG, WebP | 
 5 MB | 

 Vector image | 
 SVG | 
 5 MB | 

 Document | 
 DOC, DOCX, PDF, PPT, PPTX, XLS, XLSX | 
 5 MB | 

 Archive | 
 ZIP | 
 50 MB total, 5 MB per file within the ZIP | 

If you upload a file type that isn’t listed here, the endpoint returns an UNSUPPORTED_FILE_TYPE error.

For ZIP files, each file inside the archive must also be one of the supported file types listed here, and all files must be in the root of the ZIP file (no subdirectories). Any file that isn’t supported is skipped and returned in the errors array of the response, and the rest of the archive is still uploaded.

note

Virtual Contact Files (.vcf) and video files can be uploaded to the media library, but only through the dashboard UI (Content > Media Library), not through this API endpoint.

tip

You can also call this endpoint through the Braze MCP server using the create_media_library_asset function. This lets AI tools like Claude and Cursor upload assets to your media library through natural language prompts.

## Prerequisites

To use this endpoint, you’ll need an API key with the media_library.create permission.

## Rate limit

This endpoint has a rate limit of 100 requests per hour, as documented in API rate limits.

## Request body

When you include asset_url, the endpoint downloads the file from the URL. When you include asset_file, the endpoint uses the binary data in the request body.

Example request body for asset_url:

```

1
2
3
4

```
 | 
```
{
 "asset_url": "https://cdn.example.com/assets/cat.jpg",
 "name": "Cat Graphic"
}

```
 | 

Example request body for asset_file:

```

1
2
3
4

```
 | 
```
{
 "asset_file": <BINARY FILE DATA>,
 "name": "Cat Graphic"
}

```
 | 

The request body includes the following parameters:

 Parameter | 
 Required | 
 Data Type | 
 Description | 

 asset_url | 
 Optional | 
 String | 
 A publicly accessible URL for the asset to be uploaded into Braze. | 

 asset_file | 
 Optional | 
 Binary | 
 Binary file data. | 

 name | 
 Optional | 
 String | 
 A name to appear in the media library for this asset. | 

important

asset_url and asset_file are mutually exclusive, you must only include one of them in your API request.

### Uploaded file names

This section explains how the endpoint assigns names to uploaded files based on whether you include the name parameter.

#### Single file uploads

 Scenario | 
 Result | 

 name provided | 
 The name value is used as the asset name in the media library. | 

 name excluded | 
 The original filename from the URL or uploaded file is used. | 

#### ZIP file uploads

 Scenario | 
 Result | 

 name provided | 
 The name value is used as a prefix, with an incrementing number appended as a suffix (for example, “My File 1”, “My File 2”, “My File 3”). | 

 name excluded | 
 Each file retains its original filename from within the ZIP file. | 

## Example request

This section includes two example curl requests, one for adding an asset using a URL and another using binary file data.

This request shows an example of adding an asset to the media library using an asset_url.

```

1
2
3
4

```
 | 
```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'

```
 | 

This request shows an example of adding an asset to the media library using an asset_file.

```

1
2
3
4

```
 | 
```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'

```
 | 

### Error responses

This section lists potential errors and their corresponding messages and descriptions.

#### Validation errors

Validation errors return a structure like this:

```

1
2
3

```
 | 
```
{
 "message": (String) Human-readable error description
}

```
 | 

This table lists possible validation errors.

 HTTP Status | 
 Message | 
 Description | 

 400 | 
 “Either asset_url or asset_file must be provided.” | 
 No asset parameter was provided in the request. | 

 400 | 
 “Both asset_url and asset_file cannot be provided. Please provide only one.” | 
 Both asset parameters were provided; only one is allowed. | 

 403 | 
 “Media Library Public APIs are not enabled for this company.” | 
 Media library feature is not enabled for this workspace. | 

#### Processing errors

Processing errors return a different response with error codes:

```

1
2
3
4
5

```
 | 
```
{
 "message": (String) Human-readable error description,
 "error_code": (String) error code,
 "meta": { }
}

```
 | 

This table lists possible processing errors.

 Error Code | 
 HTTP Status | 
 Description | 

 UNSUPPORTED_FILE_TYPE | 
 400 | 
 The uploaded file type is not supported. Refer to Supported file types. The meta object includes the file_type that was rejected. | 

 ASSET_SIZE_EXCEEDS_LIMIT | 
 400 | 
 The file exceeds the maximum allowed size of 5 MB. | 

 MEDIA_LIBRARY_LIMIT_REACHED | 
 400 | 
 The workspace has reached its maximum number of assets (200 by default for free trial companies, unlimited otherwise). The meta object includes the current limit. | 

 ASSET_UPLOAD_FAILED | 
 400 | 
 The asset failed to upload due to processing issues. | 

 INVALID_ASSET_URL | 
 400 | 
 The asset_url value is not a valid URI. The meta object includes asset_url. | 

 ZIP_UPLOAD_ERROR | 
 400 | 
 The ZIP file is corrupted or could not be opened. The meta object includes the original_error message. | 

 ZIP_FILE_TOO_LARGE | 
 400 | 
 The total uncompressed size of the ZIP file exceeds the 50 MB limit. The meta object includes the zip_file_name and zip_file_size. | 

 ZIPPED_ENTITY_HAS_NO_NAME | 
 400 | 
 A file entry inside the ZIP has no name. Ensure the ZIP file is not corrupted and add a name for any unnamed file entries. | 

 ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY | 
 400 | 
 The ZIP file contains nested directories, which are not supported. All files must be at the root level of the ZIP. | 

 GENERIC_ERROR | 
 500 | 
 An unexpected error occurred during upload. The meta object includes the original_error message for debugging. Try again or contact Support. | 

## Response

There are five status code responses for this endpoint: 200, 400, 403, 429, and 500.

The following JSON shows the expected shape of the response.

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
 "new_assets": [
 {
 "name": (String) the name of the asset,
 "size": (Integer) the byte size of the asset,
 "url": (String) the URL to access the asset,
 "ext": (String) the file extension (e.g., "png", "jpg", "gif")
 }
 ],
 "errors": [
 {
 "name": (String) the name of the asset,
 "size": (Integer) the byte size of the asset,
 "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
 "error": (String) the error that occurred
 }
 ],
 "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}

```
 | 

- 

New Stuff!
