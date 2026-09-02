---
url: https://www.braze.com/docs/partners/message_personalization/location/accuweather
slug: docs__partners__message_personalization__location__accuweather
title: "AccuWeather"
description: "This reference article outlines the partnership between Braze and AccuWeather, a weather API you can use to personalize your marketing campaigns."
section: partners/message_personalization
fetched: 2026-09-02
evidence: company-own (technical)
---
# AccuWeather

AccuWeather is a media company that provides weather forecasting services worldwide. With AccuWeather, you can enrich and personalize your marketing campaigns, as well as automate translations through the use of Braze Connected Content.

This integration is maintained by AccuWeather.

## Prerequisites

 Requirement | 
 Description | 

 AccuWeather API Key | 
 Contact your AccuWeather account manager for compatible API keys to use in your request URLs.

Further instructions can be found on the AccuWeather Enterprise API page. | 

## Available AccuWeather APIs

The following are the AccuWeather APIs you can reference within your Braze campaigns and Canvases.

 API | 
 Description | 

 Locations | 
 Get a location key for your desired location. Use the location key to retrieve weather data from the Forecast or Current Conditions API. | 

 Forecast | 
 Get forecast information for a specific location. | 

 Current Conditions | 
 Get Current Conditions data for a specific location. | 

 Indices | 
 Get daily index values for a specific location. Index availability varies by location. | 

 Weather Alarms | 
 Get Weather Alarms for a specific location. AccuWeather Weather Alarms are determined using the daily forecasts for a location. An alarm exists for a location if the forecast weather meets or exceeds specific thresholds. | 

 Alerts | 
 Get severe weather alerts from official Government Meteorological Agencies and leading global weather alert providers. | 

 Imagery | 
 Get radar and satellite images. | 

 Tropical | 
 Get current position, past positions, and forecasts for tropical cyclones worldwide. | 

 Translations | 
 Get a list of available languages. Get translations for specific groups of phrases. | 

## Connected Content example

The following example shows a Connected Content call displaying two different types of messages based on the current conditions of a user’s zip code in the US. The AccuWeather locations and current conditions API endpoints are used.

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
{% connected_content http:///dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}

{% if {{local_weather[0].WeatherText}} == 'Cloudy' %}
No sunscreen needed :)
{% elsif {{local_weather[0].WeatherText}} == 'Rain' %}
It's raining! Grab an umbrella!
{% else %}
Enjoy the weather!
{% endif %}

```
 | 

A breakdown of the two Connected Content calls can be found in the following examples.

- locations
 
- current conditions

### Locations API example

Within the first connected_content tag, a GET request is made to the Locations API. For this example, you can alternatively leverage the user’s {{${city}}} if you do not have a zip code custom attribute.

```

1

```
 | 
```
{% connected_content http://dataservice.accuweather.com/locations/v1/postalcodes/{{${country}}}/search?q={{custom_attribute.${Zip Code}}}&apikey={your API key} :save location_info %}

```
 | 

Here’s an example of what AccuWeather will return as the JSON object:

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
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73

```
 | 
```
[
 {
 "Version": 1,
 "Key": "41333_PC",
 "Type": "PostalCode",
 "Rank": 35,
 "LocalizedName": "Seattle",
 "EnglishName": "Seattle",
 "PrimaryPostalCode": "98102",
 "Region": {
 "ID": "NAM",
 "LocalizedName": "North America",
 "EnglishName": "North America"
 },
 "Country": {
 "ID": "US",
 "LocalizedName": "United States",
 "EnglishName": "United States"
 },
 "AdministrativeArea": {
 "ID": "WA",
 "LocalizedName": "Washington",
 "EnglishName": "Washington",
 "Level": 1,
 "LocalizedType": "State",
 "EnglishType": "State",
 "CountryID": "US"
 },
 "TimeZone": {
 "Code": "PDT",
 "Name": "America/Los_Angeles",
 "GmtOffset": -7.0,
 "IsDaylightSaving": true,
 "NextOffsetChange": "2018-11-04T09:00:00Z"
 },
 "GeoPosition": {
 "Latitude": 47.636,
 "Longitude": -122.327,
 "Elevation": {
 "Metric": {
 "Value": 26.0,
 "Unit": "m",
 "UnitType": 5
 },
 "Imperial": {
 "Value": 85.0,
 "Unit": "ft",
 "UnitType": 0
 }
 }
 },
 "IsAlias": false,
 "ParentCity": {
 "Key": "351409",
 "LocalizedName": "Seattle",
 "EnglishName": "Seattle"
 },
 "SupplementalAdminAreas": [
 {
 "Level": 2,
 "LocalizedName": "King",
 "EnglishName": "King"
 }
 ],
 "DataSets": [
 "Alerts",
 "DailyAirQualityForecast",
 "DailyPollenForecast",
 "ForecastConfidence",
 "MinuteCast"
 ]
 }
]

```
 | 

The “Key” ID is a useful variable as it is used in the second GET request. 
This JSON object can be stored into a local variable location_info by specifying :save location_info after the URL.

### Current conditions API example

For the second connected_content tag, a GET request is made to the Current Conditions API. The location key will need to be added to the request URL. Here is the example connected_content tag:

```

1

```
 | 
```
{% connected_content http://dataservice.accuweather.com/currentconditions/v1/{{location_info[0].Key}}?apikey={your API key} :save local_weather %}

```
 | 

Here is the returned JSON object:

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
20
21
22
23

```
 | 
```
[
 {
 "LocalObservationDateTime": "2018-04-10T09:35:00-07:00",
 "EpochTime": 1523378100,
 "WeatherText": "Rain",
 "WeatherIcon": 18,
 "IsDayTime": true,
 "Temperature": {
 "Metric": {
 "Value": 11.0,
 "Unit": "C",
 "UnitType": 17
 },
 "Imperial": {
 "Value": 52.0,
 "Unit": "F",
 "UnitType": 18
 }
 },
 "MobileLink": "http://m.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us",
 "Link": "http://www.accuweather.com/en/us/seattle-wa/98104/current-weather/41333_pc?lang=en-us"
 }
]

```
 | 

As seen in the connected_content tag, the JSON object is stored into a local variable local_weather by adding :save local_weather after the URL.

You can test what the output of the WeatherText should be by referencing {{local_weather[0].WeatherText}}.

If the API call responds with {{local_weather[0].WeatherText}} returning Rain, the user would then receive the push.

- 

New Stuff!
