---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables
slug: docs__user_guide__messaging__design_and_edit__personalize__connected_content__local_connected_content_variables
title: "Local Connected Content variables"
description: "This reference article covers how to use and store local Connected Content variables."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Local Connected Content variables

This page provides an overview of local Connected Content variables and how to use and store them.

Braze makes a standard GET request at send time to the endpoint specified within the connected_content tag. If the endpoint returns JSON, it’s automatically parsed and stored in a variable called connected. If the endpoint returns text, it will be directly inserted into the message in place of the connected_content tag.

If you want to save your response to a variable, it’s recommended to return JSON objects. And if you want the response of Connected Content to replace the tag with the text, make sure the response isn’t valid JSON (as defined by json.org)

You can also specify :save your_variable_name after the URL to save the data as something else. For example, the following connected_content tag will store the response to a local variable called localweather (you can save multiple connected_content JSON variables):

```

1

```
 | 
```
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}

```
 | 

Metaweather is a free weather API that uses a “Where-on-Earth ID” to return weather in an area. Use this code for testing and learning purposes only.

The stored variable can only be accessed within the field that contains the connected_content request. For example, if you want to use the localweather variable in both the message and title field, make the connected_content request within both fields.

GET requests are typically cached by default, with a few exceptions (such as URLs that include high-cardinality user attributes, :no_cache, or response bodies larger than 1 MB). When identical GET requests appear in more than one field, Braze reuses the cached response instead of calling the endpoint again. For cache behavior details, see Caching responses.

Connected Content calls made through HTTP POST are not cached by default. To cache POST responses, add :cache_max_age to the tag. See Default cache settings.

## JSON parsing

Connected Content will interpret any JSON-formatted results into a local variable, when you specify :save. For example, a weather-related Connected Content endpoint returns the following JSON object, which you store into a local variable localweather by specifying :save localweather.

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

```
 | 
```
{
 "consolidated_weather": [
 {
 "id": 5.8143475362693e+15,
 "weather_state_name": "Clear",
 "weather_state_abbr": "c",
 "wind_direction_compass": "WSW",
 "created": "2017-06-12T14:14:46.268110Z",
 "applicable_date": "2017-06-12",
 "min_temp": 22.511666666667,
 "max_temp": 31.963333333333,
 "the_temp": 27.803333333333,
 "wind_speed": 6.8884690250312,
 "wind_direction": 251.62921994166,
 "air_pressure": 1021.335,
 "humidity": 50,
 "visibility": 14.945530601288,
 "predictability": 68
 },
 .
 .
 .
 "title": "New York",
 "location_type": "City",
 "woeid": 2459115,
 "latt_long": "40.71455,-74.007118",
 "timezone": "US\/Eastern"
 }

```
 | 

You can test whether or not it’s raining by referencing {{localweather.consolidated_weather[0].weather_state_name}}, which if used on this object would return Clear. If you want to also personalize with the resulting location name, {{localweather.title}} returns New York.

The following image illustrates the type of syntax highlighting you should see in the dashboard if you’re setting things up correctly. It also demonstrates how you could leverage the example connected_content request!

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
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}

```
 | 

If the API responded with {{localweather.consolidated_weather[0].weather_state_name}} returning Rain, the user would then receive this push.

By default, Connected Content will set a Content-Type header on a GET HTTP request that it makes to application/json with Accept: */*. If you require another content type, specify it explicitly by adding :content_type your/content-type to the tag. Braze will then set both the Content-Type and Accept header to the type you specify.

```

1

```
 | 
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :content_type application/json %}

```
 | 

## HTTP POST

By default, Connected Content makes an HTTP GET request to the specified URL. To make a POST request instead, specify :method post.

You can optionally provide a POST body by specifying :body followed by either a query string of the format key1=value1&key2=value2&... or a reference to captured values. Content-Type defaults to application/x-www-form-urlencoded. If you specify :content_type application/json and provide a form-urlencoded body such as key1=value1&key2=value2, Braze will automatically JSON-encode the body before sending.

Connected Content also does not cache POST calls by default. You can update this behavior by adding :cache_max_age to the Connected Content POST call.

- default content-type
 
- application/json content-type

```

1

```
 | 
```
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}

```
 | 

```

1

```
 | 
```
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}

```
 | 

### Providing JSON body

If you want to provide your own JSON body, you can write it inline if there are no spaces. If your body has spaces, you should use an assign or capture statement. That is, any of these three are acceptable:

##### Inline: spaces not allowed

```

1

```
 | 
```
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}

```
 | 

##### Body in a capture statement: spaces allowed

```

1
2
3
4

```
 | 
```
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}

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
8
9
10
11
12
13
14
15

```
 | 
```
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
 https://example.com/api/endpoint
 :method post
 :headers {
 "Content-Type": "application/json"
 }
 :body {{postbody}}
 :save result
%}

```
 | 

##### Body in an assign statement: spaces allowed

```

1
2

```
 | 
```
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}

```
 | 

## HTTP status codes

You can utilize the HTTP status from a Connected Content call by first saving it as a local variable and then using the __http_status_code__ key. For example:

```

1
2
3
4

```
 | 
```
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
 {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}

```
 | 

important

This key will only be automatically added to the Connected Content object if the endpoint returns a valid JSON object and a 2XX response. If the endpoint returns an array or other type, that key cannot be automatically set in the response.

- 

New Stuff!
