---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/acquire_a_phone_number
slug: docs__user_guide__channels__whatsapp__whatsapp_setup__whatsapp_phone_numbers__acquire_a_phone_number
title: "Acquire a WhatsApp phone number"
description: "This reference article covers how to acquire a phone number from Twilio and Infobip."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Acquire a WhatsApp phone number

To use the WhatsApp messaging channel, you’ll need a phone number that meets WhatsApp’s requirements for its Cloud API or On-Premises API.

You must acquire your phone number yourself, as Braze won’t provision the number for you. You can either purchase a physical phone with a SIM card through your business phone provider or use one of our partners: Twilio or Infobip. You must have your own Twilio or Infobip account because this cannot be done through Braze.

## WhatsApp API requirements

Your phone number must meet these WhatsApp API requirements:

- Owned by your business
 
- Have a country and area code (such as a landline and cell numbers)
 
- Able to receive voice calls or SMS
 
- Accessible during account setup (to receive verification codes)
 
- Not a short code
 
- Not previously used with the WhatsApp Business Platform
 
- Not connected to a personal WhatsApp account

note

Braze strongly recommends using a number your business owns and has full, ongoing access to. During the WhatsApp embedded signup process, you need access to messages sent to this number to verify it. You may need to verify the number again later, so you must retain access to it.

## Acquiring a Twilio phone number

### Step 1: Buy a phone number from the Twilio console or API

- 
 
From the Twilio console, go to Develop > Phone Numbers > Manage > Buy a number. If you don’t see this option, select Explore Products, scroll to Super Networks, then select Phone Number > Buy a number. 

- 
 
Enter your desired area code or locality (if you have one). Find a number, then select Buy. 

- 
 
After purchasing your phone number, go to Active Numbers and select the phone number you just purchased. 

### Step 2: Configure your phone number

Configure your Twilio phone number to receive verification codes through email. Do not link your phone number to WhatsApp in the Twilio console.

warning

Do not link your phone number to WhatsApp in the Twilio console. If you do, the number will be registered to Twilio’s WhatsApp Business Account, which will prevent you from connecting it to Braze through the embedded sign up workflow.

- In the Twilio console, go to the Active Numbers page and select the phone number you purchased.
 
- Go to the Voice Configuration section and in the Configure with dropdown, select Webhook, TwiML Bin, Function, Studio Flow, Proxy Service.
 
- In the A call comes in row, select Webhook and set the URL to https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS, replacing YOUR_EMAIL_ADDRESS with your email address.

### Step 3: Complete the embedded sign up workflow

- 
 
After Twilio is configured, go to your Braze dashboard > Technology Partners > WhatsApp and select Begin integration or Add WhatsApp Business Account, whichever shows up, to trigger the embedded sign up workflow.

In the Add a phone number for WhatsApp step, select Phone call for how you’d like to verify your phone number. 

- 
 
Wait a few minutes for the verification code to send to your email inbox, then enter the verification code and complete your setup.

## Acquiring an Infobip phone number

- 
 
In the Infobip console, go to Channels and Numbers and select Numbers.

- 
 
Select Buy Number > the country where you want to send messages > SMS.

- 
 
Depending on your selected country, you might need to complete an additional registration process (such as selecting a 10 DLC or toll-free option for US phone numbers). Be sure to select the available option.

- 
 
Select the available offer, then proceed through the rest of the steps and wait for your request to be processed. You can check the status by going to Numbers > My Request. 

- 
 
Depending on your selected country, wait for the Infobip team to contact you for registration details (such as for 10DLC in the US).

- 
 
When your phone number is ready in Infobip, go to your Braze dashboard > Technology Partners > WhatsApp and select Begin integration or Add WhatsApp Business Account, whichever shows up, to trigger the embedded sign up workflow.

 In the Add a phone number for WhatsApp step, select Text message for how you’d like to verify your phone number.

- 
 
Check Infobip’s analyze logs in their customer portal for the verification code, which could take a few minutes to appear, then enter the verification code and complete setup.

- 

New Stuff!
