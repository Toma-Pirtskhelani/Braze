---
url: https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
slug: docs__user_guide__messaging__design_and_edit__personalize__liquid__tutorials
title: "Tutorials: Writing Liquid code"
description: "This reference page contains beginner-friendly tutorials to help you get started with Liquid code."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Tutorials: Writing Liquid code

New to Liquid? These tutorials will help you get started with writing Liquid code for beginner-friendly use cases. Each tutorial covers a different combination of learning objectives, such as conditional logic and operators.

When you’re finished with these tutorials, you’ll be able to:

- Write Liquid code for common use cases
 
- String together Liquid conditional logic to personalize messages based on user data
 
- Use variables and filters to write equations that use the values of attributes
 
- Recognize basic commands in Liquid code and form a general understanding about what the code is doing

 Tutorial | 
 Learning objectives | 

 Personalize messages for user segments | 
 default values, conditional logic | 

 Abandoned cart reminders | 
 operators, conditional logic | 

 Event countdown | 
 variables, date filters | 

 Monthly birthday message | 
 variables, date filters, operators | 

 Promote a favorite product | 
 variables, date filters, equations, operators | 

## Personalized messages for user segments

Let’s customize messages for different user segments, like VIP customers and new subscribers.

- Open the message with personalized greetings to send when you have and don’t have a user’s first name. To do this, create a Liquid tag that includes the attribute first_name and a default value to use if first_name is blank. In this scenario, let’s use “traveler” as the default value.

```

1

```
 | 
```
Happy summer, {{${first_name} | default: "traveler"}}!

```
 | 

- Now, let’s provide the message to send if the user is a VIP customer. We’ll need to use a conditional logic tag for this: if. This tag will say that if the vip_status custom attribute is equal to VIP, the following Liquid will be carried out. In this case, a specific message will send.

```

1
2

```
 | 
```
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.

```
 | 

- Let’s send a customized message for users who are new subscribers. We’ll use the conditional logic tag elsif to specify that if the user’s vip_status is new, the following message will send.

```

1
2

```
 | 
```
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.

```
 | 

- What about the users who aren’t VIP or new? We can send a message to all other users with the else tag, which specifies that the following message should be sent if the previous conditions aren’t met. Then we can close the conditional logic with the endif tag, as there aren’t any more VIP statuses to consider.

```

1
2
3

```
 | 
```
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}

```
 | 

Full Liquid code

```

1
2
3
4
5
6
7
8

```
 | 
```
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}

```
 | 

## Abandoned cart reminders

Let’s send personalized messages to remind users of items left in their cart. We’ll further customize them to send based on how many items are in their cart, so that if they have more three items or fewer, we’ll list all the items. If there are more than three items, we’ll send a more concise message.

- Let’s check if the user’s cart is empty by opening a Liquid conditional logic with the operator !=, which means “does not equal”. In this case, we’ll set the condition to the custom attribute cart_items not equaling a blank value.

```

1

```
 | 
```
{% if {{custom_attribute.${cart_items}}} != blank %}

```
 | 

- We’ll then need to narrow our focus and check if the cart has more than three items by using the operator `>’, which means “greater than”.

```

1

```
 | 
```
{% if {{custom_attribute.${cart_items}}} | size > 3 %}

```
 | 

- Write a message that greets the user by their first name, or if that’s not available, use “there” as the default value. Include what should be stated if there are more than three items in the cart. Because we don’t want to overwhelm the user with a complete list, let’s list the first three cart_items.

```

1

```
 | 
```
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.

```
 | 

- Use the else tag to specify what should happen if the previous conditions aren’t met (in other words, if cart_items is blank or fewer than three), and then provide the message to send. Because three items don’t take up a lot of space, we can list them all. We’ll use the Liquid operator join and , to specify that the items should be listed with a comma separating them. Close the logic with endif.

```

1
2
3

```
 | 
```
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '} are waiting for you. 
{% endif %}

```
 | 

- Use else and then an abort_message to tell the Liquid code to not send a message if the cart doesn’t meet any of the previous conditions. In other words, if the cart is empty. Close the logic with endif.

```

1
2
3

```
 | 
```
{% else %}
{% abort_message('No items in cart') %}
{% endif %}

```
 | 

Full Liquid code

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
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '} are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}

```
 | 

## Event countdown

Let’s send users a message that states how many days are left until an anniversary sale. To do this, we’ll use variables so we can create equations that manipulate the values of attributes.

- First, let’s assign the variable sale_date to the custom attribute anniversary_date, and apply the date: "s" filter. This converts the anniversary_date to a timestamp format that is expressed in seconds, then assigns that value to sale_date.

```

1

```
 | 
```
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}

```
 | 

- We also need to assign a variable to capture today’s timestamp. Let’s assign the variable today to now (the current date and time), then apply the date: "%s" filter.

```

1

```
 | 
```
{% assign today = 'now' | date: "%s" %}

```
 | 

- Now let’s calculate how many seconds are between now (today) and the Anniversary Sale (sale_date). To do this, assign the variable difference to equal the value of sale_date minus today.

```

1

```
 | 
```
{% assign difference = event_date | minus: today %}

```
 | 

- Now we need to convert difference to a value that we can reference in a message, as it isn’t ideal to tell the user how many seconds there are until a sale. Let’s assign difference_days to the event_date and divide it by 86400 to get the number of days.

```

1

```
 | 
```
{% assign difference_days = difference | divided_by: 86400 %}

```
 | 

- Finally, let’s create the message to send.

```

1

```
 | 
```
Get ready! Our Anniversary Sale is in {{ difference_days }} days!

```
 | 

Full Liquid code

```

1
2
3
4
5

```
 | 
```
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!

```
 | 

## Monthly birthday message

Let’s send a special promotion to all users whose birthday falls within today’s month. Users who don’t have a birthday this month won’t receive any message.

- First, let’s pull today’s month. We’ll assign the variable this_month to now (the current date and time), then use the date: "%B" filter to specify that the variable should equal the month.

```

1

```
 | 
```
{% assign this_month = 'now' | date: "%B" %}

```
 | 

- Now, let’s pull the birth month from the user’s date_of_birth. We’ll assign the variable birth_month to date_of_birth, then use the date: "%B" filter.

```

1

```
 | 
```
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}

```
 | 

- Now that we have two variables that have a month as a value, we can compare them with conditional logic. Let’s set the condition to be date_of_birth equaling the user’s birth_month.

```

1

```
 | 
```
{% if {{this_month}} == {{birth_month}} %}

```
 | 

- Let’s create the message to send if this month is also the user’s birth month.

```

1

```
 | 
```
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.

```
 | 

- Use the else tag to specify what happens if the condition isn’t met (because this month isn’t the user’s birth month).

```

1

```
 | 
```
{% else %} 

```
 | 

- We don’t want to send a message if the user’s birth month isn’t this month, so we’ll use abort_message to cancel the message, then close the conditional logic with endif.

```

1
2

```
 | 
```
{% abort_message("Not their birthday month") %}
{% endif %}

```
 | 

Full Liquid code

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
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}

```
 | 

## Favorite product promotion

Let’s promote a user’s favorite product if their last purchase date was over six months ago.

- First, we’ll use conditional logic to check if we have the user’s favorite product and last purchase date.

```

1

```
 | 
```
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}

```
 | 

- Then we’ll state that if we don’t have the user’s favorite product or last purchase date, not to send a message.

```

1

```
 | 
```
{% abort_message("No favorite product or last purchase date") %}

```
 | 

- We’ll use else to specify what should happen if the condition earlier in this section isn’t met (because we do have the user’s favorite product and last purchase date).

```

1

```
 | 
```
{% else %}

```
 | 

- If we have purchase date, we need to assign it to a variable so we can compare it to today’s date. First, let’s create a value for today’s date by assigning the variable today to now (the current date and time) and using the date: "%s" filter to convert the value to a timestamp format that is expressed in seconds. We’ll add the plus: 0 filter to add a “0” to the timestamp. This doesn’t change the timestamp’s value, but is useful for using the timestamp in future equations.

```

1

```
 | 
```
{% assign today = 'now' | date: "%s" | plus: 0 %}

```
 | 

- Now let’s capture the last purchase date in seconds by assigning the variable last_purchase_date to the custom attribute last_purchase_date and using the date: "s" filter. We’ll again add the plus: 0 filter.

```

1

```
 | 
```
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}

```
 | 

- Because the last purchase date and today’s date are in seconds, we’ll need to calculate how many seconds are in six months. Let’s make an equation (approximately 6 months * 30.44 days * 24 hours * 60 minutes * 60 seconds) and assign it to the variable six_months. We’ll use times to specify the multiplication of time units.

```

1

```
 | 
```
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}

```
 | 

- Now that all our time values are in seconds, we can use their values in equations. Let’s assign a variable called today_minus_last_purchase_date that takes today’s value and subtracts from it the last_purchase_date. This gives us how many seconds it has been since the last purchase.

```

1

```
 | 
```
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}

```
 | 

- Now let’s directly compare our time values in conditional logic. Let’s define the condition as today_minus_last_purchase_date being greater than or equal (>=) to six months. In other words, the last purchase date was at least six months ago.

```

1

```
 | 
```
{% if today_minus_last_purchase_date >= six_months %}

```
 | 

- Let’s create the message to send if the last purchase was at least six months ago.

```

1

```
 | 
```
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?

```
 | 

- We’ll use the else tag to specify what should happen if the condition isn’t met (because the purchase wasn’t at least six months ago).

```

1

```
 | 
```
{% else %}

```
 | 

- We’ll include an abort_message to cancel the message.

```

1

```
 | 
```
{% abort_message("No favorite product or last purchase date") %}

```
 | 

- To finish, we’ll end the Liquid with two endif tags. The first endif closes the conditional check for the favorite product or last purchase date, and the second endif closes the conditional check for the last purchase date being at least six months ago.

```

1
2

```
 | 
```
{% endif %}
{% endif %}

```
 | 

Full Liquid code

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
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}

```
 | 

- 

New Stuff!
