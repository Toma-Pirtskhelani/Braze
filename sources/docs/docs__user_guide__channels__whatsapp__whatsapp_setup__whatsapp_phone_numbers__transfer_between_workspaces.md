---
url: https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces
slug: docs__user_guide__channels__whatsapp__whatsapp_setup__whatsapp_phone_numbers__transfer_between_workspaces
title: "Transfer WhatsApp phone numbers and subscription groups between workspaces"
description: "This reference article covers how to transfer your WhatsApp phone number and subscription groups between workspaces."
section: user_guide/channels
fetched: 2026-09-02
evidence: company-own (technical)
---
# Transfer WhatsApp phone numbers and subscription groups between workspaces

This page covers how you can move a WhatsApp Business Account (WABA) phone number and its associated subscription group from one workspace to another within Braze. This process streamlines your experience using WhatsApp with Braze, and reduce the need for engineering help.

## Prerequisites

- Confirm you have the user permission “Manage Subscription Groups” in both the original and new workspaces.
 
- The WABA can’t cross multiple Braze clusters. This is unlikely to happen if you’re working within one company.

## Transferring a phone number and subscription group

### Step 1: Archive the subscription group

To archive a WhatsApp subscription group, follow these steps:

- Go to the workspace where the subscription group currently exists.
 
- Go to Audience > Subscription Group Management and find the subscription group associated with the WhatsApp phone number you want to move.
 
- Hover over the status for the subscription group and select Archive, which will mark the subscription group as inactive but won’t delete it.

### Step 2: Integrate the WhatsApp phone number into the new workspace

- Go to the workspace where you want to move the WhatsApp phone number.
 
- Go to Partner Integrations > Technology Partners > WhatsApp, then scroll to the WhatsApp Messaging Integration section.
 
- Select the option to Create new subscription group and phone number
 
- Begin the integration process, during which you can select the phone number from the archived subscription group.

### Step 3: Verify the integration

- After completing the integration, confirm that the WhatsApp phone number is now associated with the subscription group in the new workspace.
 
- Test to confirm that messages can be sent and received through that WhatsApp phone number.

## Considerations

- If you need to transfer the WhatsApp phone number back to the original workspace, repeat the steps. Archive the subscription group in the destination workspace, then integrate it into the original workspace.
 
- You don’t need to remove the WhatsApp phone number from your Meta Business Manager during the transfer.

- 

New Stuff!
