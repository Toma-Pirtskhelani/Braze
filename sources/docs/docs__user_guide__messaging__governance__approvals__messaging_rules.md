---
url: https://www.braze.com/docs/user_guide/messaging/governance/approvals/messaging_rules
slug: docs__user_guide__messaging__governance__approvals__messaging_rules
title: "Messaging rules"
description: "This page covers how to use messaging rules in the approval workflow for campaigns and Canvases with a large send volume."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Messaging rules

Use messaging rules in your approval workflow to limit the number of reachable users before an additional approval is required—this way, you can review your campaigns and Canvases before you target a larger audience.

## Prerequisites

Only Braze administrators can set messaging rules, but any Braze user can be a messaging rule approver (including users without general approval permissions).

## How it works

Messaging rules apply to a workspace and are made up of a message type and a maximum number of reachable users.

- Message type: Defines what message type the rule is applied to: campaign, Canvas, or both Canvas and campaigns.
 
- Maximum reachable users: Determines what audience size requires an additional approval.

### Separate approvers

Two rules can share the same user maximum so that you can organize and separate your rules by approvers. For example, you create the following two rules:

- Rule A for Canvas with a maximum of 100,000 users with approvers on your legal team
 
- Rule B for Canvas with a maximum of 100,000 users with approvers on your marketing team

### No overlapping reachable users

To avoid confusion, you cannot set identical rules with an overlapping number of users for the same message type and approvers. For example, the following messaging rule can’t be set:

- Rule C for Canvas with a maximum of 10,000 users
 
- Rule D for Canvas with a maximum of 1,000,000 users

## Creating a messaging rule

### Step 1: Add a rule

note

You can create up to five messaging rules.

- Go to Settings > Approval Workflow > Messaging Rules.
 
- Select Create rule.
 
- Give this rule a name (for example, “All user subscriptions”).
 
- For Message type, select Campaign, Canvas, or Both Canvas and Campaigns to apply the approval rule.
 
- Enter a number for Maximum reachable users. For more information, refer to Audience statistics.
 
- Select Save.

### Step 2: Determine launching with approval (optional)

Select Allow launching with approval. Next, for With Approval From, select the approvers who have permission to approve the Canvas or campaign if the maximum is met.

Note the following details on launching messages with approval:

- If the maximum is met and an approver is selected, the Braze user with the approval permission can select Approved from the Target Audience approval dropdown.
 
- If the maximum is met and an approver is not selected, the Canvas or campaign is prevented from launching.

## Frequently asked questions

### Do I have to reconfigure my permissions to use messaging rules?

No. Any user, regardless of their current permissions, can be selected as a target population approver.

### How do messaging rules relate to the Target Audience step?

Messaging rules don’t take into account details such as triggering events. For example, a campaign might target all your users. However, the campaign is event triggered, so the actual users who receive it is lower.

### Will anything automatically change when messaging rules are turned on?

No. After this feature is turned on, you must manually enter the maximum number of users and select approvers to use the feature.

- 

New Stuff!
