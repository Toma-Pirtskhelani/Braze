---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid__filters
title: "Filters"
description: "This reference page lists filters that can be used to reformat static or dynamic content."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Filters

This reference article provides an overview of filters in Liquid, and covers which filters are supported by Braze. Looking for ideas on how you can use these filters? Check out our Liquid use case library.

Filters are how you can modify the output of numbers, strings, variables, and objects in Liquid. You can use filters to reformat static or dynamic text, such as changing a string from lowercase to uppercase or to perform mathematical operations, like addition or division.

important

Braze does not support all Liquid filters from Shopify. This page attempts to outline the Liquid filters that Braze has tested, but it may not be a complete list. Always test your Liquid before sending out any messages. 

If you have any questions about a filter that is not listed here, contact your customer success manager.

## Filter syntax

Filters must be placed within an output tag {{ }} and are denoted by a pipe character |.

- input
 
- output

```

1

```
 | 
```
{{"Big Sale" | upcase}}

```
 | 

```

1

```
 | 
```
BIG SALE

```
 | 

In this example, Big Sale is a string, and upcase is the filter being applied.

note

Filters can be used in assign statements and output tags ({{ }}), but not in conditionals (if, elsif, unless), case/when, for loops, or array access brackets. To use a filtered value in one of those contexts, assign the result to a variable first. For more details, see Where to use operators and filters.

### Syntax for multiple filters

You can use multiple filters on one output. They are applied from left to right.

- input
 
- output

```

1

```
 | 
```
 {{ "Big Sale" | upcase | remove: "BIG" }}

```
 | 

```

1

```
 | 
```
SALE

```
 | 

## Array filters

Array filters are used to change the output of arrays.

 Filter | 
 Definition | 
 Supported | 

 join | 
 Joins the elements of an array with the character passed as the parameter. The result is a single string. | 
 ✅ Yes | 

 first | 
 Returns the first element of an array. In a custom attribute array, this is the oldest added value. | 
 ✅ Yes | 

 last | 
 Returns the last element of an array. In a custom attribute array, this is the most recently added value. | 
 ✅ Yes | 

 compact | 
 Removes any nil items from an array. | 
 ✅ Yes | 

 concat | 
 Combines an array with another array. | 
 ✅ Yes | 

 find_index | 
 Returns the item at the specified index location in an array. The first item in an array is referenced with [0]. | 
 ⛔ No | 

 map | 
 Accepts an array element’s attribute as a parameter and creates an array out of each array element’s value. | 
 ✅ Yes | 

 reverse | 
 Reverses the order of the items in an array. | 
 ✅ Yes | 

 size | 
 Returns the size of a string (the number of characters) or an array (the number of elements). | 
 ✅ Yes | 

 slice | 
 Returns a substring of a string or a subset of an array, starting at the specified index. | 
 ✅ Yes | 

 sort | 
 Sorts the elements of an array by a given attribute of an element in the array. | 
 ✅ Yes | 

 sort_natural | 
 Sorts the items in an array in case-insensitive alphabetical order. | 
 ✅ Yes | 

 uniq | 
 Removes any duplicate instances of elements in an array. | 
 ✅ Yes | 

 where | 
 Filters an array to only include items with a specific property value. | 
 ✅ Yes | 

## Color filters

Color filters are not supported in Braze.

## Font filters

Font filters are not supported in Braze.

## Math filters

Math filters allow you to perform mathematical operations. If you use multiple filters on one output, they will be applied from left to right.

 Filter | 
 Definition | 
 Supported | 

 abs | 
 Returns the absolute value of a number. | 
 ✅ Yes | 

 at_most | 
 Limits a number to a maximum value. | 
 ✅ Yes | 

 at_least | 
 Limits a number to a minimum value. | 
 ✅ Yes | 

 ceil | 
 Rounds an output up to the nearest integer. | 
 ✅ Yes | 

 divided_by | 
 Divides an output by a number. The output is rounded down to the nearest integer. Check out the following tip to prevent rounding. | 
 ✅ Yes | 

 floor | 
 Rounds an output down to the nearest integer. | 
 ✅ Yes | 

 minus | 
 Subtracts a number from an output. | 
 ✅ Yes | 

 plus | 
 Adds a number to an output. | 
 ✅ Yes | 

 round | 
 Rounds the output to the nearest integer or specified number of decimals. | 
 ✅ Yes | 

 times | 
 Multiplies an output by a number. | 
 ✅ Yes | 

 modulo | 
 Divides an output by a number and returns the remainder. | 
 ✅ Yes | 

tip

When dividing integers (whole numbers) by integers in Liquid, if the answer is a float (number with a decimal), Liquid will automatically round down to the nearest integer. However, dividing integers by floats will always give you a float. That means you can turn your integers into a float (1.0, 2.0, 3.0) to return a float.

For example,{{15 | divided_by: 2}} will output 7, whereas {{15 | divided_by: 2.0}} will output 7.5.

### Mathematical operations with custom attributes

Keep in mind that you can’t perform mathematical operations between two custom attributes.

```

1

```
 | 
```
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}

```
 | 

This example wouldn’t work because you can’t reference multiple custom attributes in one line of Liquid. Instead, you would need to assign a variable to at least one of these values before the math functions take place. Adding two custom attributes together would require two lines of Liquid:

- One to assign the custom attribute to a variable,
 
- One to perform the addition.

#### Use case: Calculate current balance

Let’s say we want to calculate a user’s current balance by adding their gift card balance and rewards balance.

- Use the assign tag to substitute the custom attribute of current_rewards_balance with the term “balance”. This means that you now have a variable named balance, which you can manipulate.

```

1

```
 | 
```
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}

```
 | 

- Use the plus filter to combine each user’s gift card balance with their rewards balance, signified by the {{balance}} object.

- input
 
- output

```

1
2

```
 | 
```
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!

```
 | 

```

1

```
 | 
```
You have $35 to spend!

```
 | 

## Money filters

If you’re updating a user on their purchase, an account balance, or anything regarding money, you should use money filters. Money filters ensure that your decimals are in the proper place and that no piece of your update is lost (like that pesky 0 at the end).

 Filter | 
 Definition | 
 Supported | 

 money | 
 Formats numbers to ensure that decimals are in the proper place, and zeros are not dropped off the end of any numbers. | 
 ✅ Yes | 

 money_with_currency | 
 Formats numbers with the currency symbol. | 
 ⛔ No | 

 money_without_currency | 
 Formats numbers without the currency symbol. | 
 ⛔ No | 

important

To properly format a number with the money filter, remove any commas in the number and add the plus: 0 filter before the money filter. For example, see the following Liquid:

```

1
2

```
 | 
```
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}

```
 | 

### Shopify money filter versus Braze money filter

warning

The behavior of the Shopify money filter differs from how it’s used in Braze. Refer to the following examples for an accurate depiction of the expected behavior.

In the event you are inputting a custom attribute (like account_balance), you should always use the money filter to put your decimals in the proper place and prevent zeros from dropping off the end of any numbers:

```

1

```
 | 
```
${{custom_attribute.${account_balance} | money}}

```
 | 

 WITH THE MONEY FILTER | 
 WITHOUT THE MONEY FILTER | 

 | 
 | 

 Where account_balance is input at 17.8. | 
 Where account_balance is input at 17.8. | 

The money filter in Braze differs from Shopify because it doesn’t automatically apply decimal points according to a preset setting. For example, take the following scenario where rewards_redeemed contains a value of 145:

- input
 
- output

```

1

```
 | 
```
${{event_properties.${rewards_redeemed} | money }}

```
 | 

```

1

```
 | 
```
$145.00

```
 | 

According to Shopify’s money filter, this should have an output of $1.45, however in Braze, this will have an output of $145.00. As a workaround, we can use the divided_by filter to manipulate the number into a decimal, before applying the money filter:

- input
 
- output

```

1

```
 | 
```
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}

```
 | 

```

1

```
 | 
```
$1.45

```
 | 

## String filters

String filters are used to manipulate the outputs and variables of strings. Strings are a combination of alphanumeric characters and must be wrapped in straight quotes.

note

Straight quotes are different from curly quotes in Liquid. Be careful when copying and pasting Liquid from a text editor into Braze, as curly quotes will cause errors with your Liquid. If you’re writing your Liquid directly into Braze, straight quotes will be applied automatically.

 Filter | 
 Description | 
 Supported | 

 append | 
 Appends characters to a string. | 
 ✅ Yes | 

 camelize | 
 Converts a string into CamelCase. | 
 ⛔ No | 

 capitalize | 
 Capitalizes the first word in a string and downcases the remaining characters. | 
 ✅ Yes | 

 downcase | 
 Converts a string into lowercase. | 
 ✅ Yes | 

 escape | 
 Escapes a string. | 
 ✅ Yes | 

 handleize | 
 Formats a string into a handle. | 
 ⛔ No | 

 md5 | 
 Converts a string into an MD5 hash. Refer to Encoding Filters for more. | 
 ✅ Yes | 

 sha1 | 
 Converts a string into a SHA-1 hash. Refer to Encoding Filters for more. | 
 ✅ Yes | 

 hmac_sha1_hex
(previously hmac_sha_1) | 
 Converts a string into a SHA-1 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. Refer to Encoding Filters for more. | 
 ✅ Yes | 

 hmac_sha256 | 
 Converts a string into a SHA-256 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. | 
 ✅ Yes | 

 hmac_sha512 | 
 Converts a string into a SHA-512 hash using a hash message authentication code (HMAC). Pass the secret key for the message as a parameter to the filter. | 
 ✅ Yes | 

 newline_to_br | 
 Inserts a <br> line break HTML tag in front of each line break in a string. | 
 ✅ Yes | 

 pluralize | 
 Outputs the singular or plural version of an English string based on the value of a number. | 
 ⛔ No | 

 prepend | 
 Prepends characters to a string. | 
 ✅ Yes | 

 remove | 
 Removes all occurrences of a substring from a string. | 
 ✅ Yes | 

 remove_first | 
 Removes only the first occurrence of a substring from a string. | 
 ✅ Yes | 

 replace | 
 Replaces all occurrences of a string with a substring. | 
 ✅ Yes | 

 replace_first | 
 Replaces the first occurrence of a string with a substring. | 
 ✅ Yes | 

 slice | 
 The slice filter returns a substring, starting at the specified index. | 
 ✅ Yes | 

 split | 
 The split filter takes on a substring as a parameter. The substring is used as a delimiter to divide a string into an array. | 
 ✅ Yes | 

 strip | 
 Strips tabs, spaces, and newlines (all whitespace) from the left and right side of a string. | 
 ✅ Yes | 

 lstrip | 
 Strips tabs, spaces, and newlines (all whitespace) from the left side of a string. | 
 ⛔ No | 

 rstrip | 
 Strips tabs, spaces, and newlines (all whitespace) from the right side of a string. | 
 ⛔ No | 

 strip_html | 
 Strips all HTML tags from a string. | 
 ✅ Yes | 

 strip_newlines | 
 Removes any line breaks/newlines from a string. | 
 ✅ Yes | 

 truncate | 
 Truncates a string down to the number of characters passed as the first parameter. An ellipsis (…) is appended to the truncated string and is included in the character count. | 
 ✅ Yes | 

 truncatewords | 
 Truncates a string down to the number of words passed as the first parameter. An ellipsis (…) is appended to the truncated string. | 
 ✅ Yes | 

 upcase | 
 Converts a string into uppercase. | 
 ✅ Yes | 

## Additional filters

The following general filters serve many purposes, including formatting or converting content.

 Filter | 
 Description | 
 Supported | 

 date | 
 Converts a timestamp into another date format. Refer to Date Filter for more. | 
 ✅ Yes | 

 default | 
 Sets a default value for any variable with no assigned value. Can be used with strings, arrays, and hashes. | 
 ✅ Yes | 

 format_address | 
 Formats an address to print the elements of the address in order according to their locale. | 
 ⛔ No | 

 highlight | 
 Wraps words inside search results with an HTML <strong> tag with the class highlight if it matches the submitted search terms. | 
 ⛔ No | 

You can find more supported filters, such as encoding and URL filters, on our Advanced Filters page.

### Date filter

The date filter can be used to convert a timestamp into a different date format. You can pass in parameters to the date filter to reformat the timestamp. For examples of these parameters, refer to strfti.me.

For example, let’s say that the value of date_attribute is the timestamp 2021-06-03 17:13:41 UTC.

- input
 
- output

```

1

```
 | 
```
{{custom_attribute.${date_attribute} | date: '%b %d'}}

```
 | 

```

1

```
 | 
```
03 June

```
 | 

In addition to the strftime formatting options, Braze also supports converting a timestamp to Unix time with the %s date filter. For example, to get the date_attribute in Unix time:

- input
 
- output

```

1

```
 | 
```
{{custom_attribute.${date_attribute} | date: '%s' }}

```
 | 

```

1

```
 | 
```
1433351621

```
 | 

- 

New Stuff!
