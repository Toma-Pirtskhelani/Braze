---
url: https://www.braze.com/docs/developer_guide/feature_flags
slug: docs__developer_guide__feature_flags
title: "Feature flags"
description: "This reference article covers an overview of feature flags including prerequisites and use cases."
section: developer_guide/feature_flags
fetched: 2026-09-02
evidence: company-own (technical)
---
# Feature flags

Feature flags allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

tip

When you’re ready to create your own feature flags, check out Creating feature flags.

## Prerequisites

These are the minimum SDK versions needed to start using feature flags:

   Swift: 5.9.0+     Web: 4.6.0+     Android: 24.2.0+     Roku: 1.0.0+  Flutter: 6.0.0+  Unity: 4.1.0+  React Native: 4.1.0+  Cordova: 5.0.0+  

## Use cases

### Gradual rollouts

Use feature flags to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early.

For example, let’s say we’ve decided to add a new “Live Chat Support” link to our app for faster customer service. We could release this feature to all customers at once. However, a wide release carries risks, such as:

- Our Support team is still in training, and customers can start support tickets after it’s released. This doesn’t give us any leeway in case the Support team needs more time.
 
- We’re unsure of the actual volume of new support cases we’ll get, so we might not be staffed appropriately.
 
- If our Support team is overwhelmed, we have no strategy to quickly turn this feature off again.
 
- There might be bugs introduced in the chat widget, and we don’t want customers to have a negative experience.

With Braze feature flags, we can instead gradually roll out the feature and mitigate all of these risks:

- We will turn on the “Live Chat Support” feature when the Support team says they’re ready.
 
- We will enable this new feature for only 10% of users to determine if we’re staffed appropriately.
 
- If there are any bugs, we can quickly disable the feature instead of rushing to ship a new release.

To gradually roll out this feature, we can create a feature flag named “Live Chat Widget.”

In our app code, we will only show the Start Live Chat button when the Braze feature flag is enabled:

- javascript
 
- java
 
- kotlin
 
- swift

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

```
 | 
```
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
 const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
 setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
 Need help? <button>Email Our Team</button>
 {liveChatEnabled && <button>Start Live Chat</button>}
</>)

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
16
17

```
 | 
```
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
 FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
 Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
 liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
 liveChatView.setVisibility(View.VISIBLE);
} else {
 liveChatView.setVisibility(View.GONE);
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

```
 | 
```
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
 val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
 liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
 liveChatView.visibility = View.VISIBLE
} else {
 liveChatView.visibility = View.GONE
}

```
 | 

note

Reading braze.featureFlags.featureFlags or braze.featureFlags.featureFlag(id:) blocks the calling thread until the SDK has completed its post-initialization operations. For main-thread or latency-sensitive contexts, use getAllFeatureFlags(_:) instead.

```

1
2
3
4
5

```
 | 
```
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
 let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
 liveChatView.isHidden = !liveChatEnabled
}

```
 | 

In Objective-C:

```

1
2
3

```
 | 
```
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
 // Use `flags` here.
}];

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

```
 | 
```
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in 
 let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
 liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled

```
 | 

### Remotely control app variables

Use feature flags to modify your app’s functionality in production. This can be particularly important for mobile apps, where app store approvals prevent rolling out changes quickly to all users.

For example, let’s say that our marketing team wants to list our current sales and promotions in our app’s navigation. Normally, our engineers require one week’s lead time for any changes and three days for an app store review. But with Thanksgiving, Black Friday, Cyber Monday, Hanukkah, Christmas, and New Year’s Day all within two months, we won’t be able to meet these tight deadlines.

With feature flags, we can let Braze power the content of our app navigation link, letting our marketing manager make changes in minutes rather than days.

To remotely configure this feature, we’ll create a new feature flag called navigation_promo_link and define the following initial properties:

In our app, we’ll use getter methods by Braze to retrieve this feature flag’s properties and build the navigation links based on those values:

- javascript
 
- java
 
- kotlin
 
- swift

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
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
 <div>
 <a href="/">Home</a>
 { promoEnabled && <a href={promoLink}>{promoText}</a> }
 <a href="/products">Products</a>
 <a href="/categories">Categories
 </div>
</>)

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

```
 | 
```
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
 liveChatView.setVisibility(View.VISIBLE);
} else {
 liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

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

```
 | 
```
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
 liveChatView.visibility = View.VISIBLE
} else {
 liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")

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

```
 | 
```
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
 liveChatView.isHidden = !featureFlag.enabled
} else {
 liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")

```
 | 

Now, the day before Thanksgiving, we only have to change those property values in the Braze dashboard.

As a result, the next time someone loads the app, they will see the new Thanksgiving deals.

### Message coordination

Use feature flags to synchronize a feature’s rollout and messaging and strengthen collaboration between product and marketing teams. By coordinating feature releases and messaging through feature flags, both teams can align their strategies and create consistent user experiences.

For example, let’s say that we’re launching a new loyalty rewards program for our users. It can be difficult for marketing and product teams to perfectly coordinate the timing of promotional messaging with a feature’s rollout. However, with feature flags in Canvas, our product team can apply sophisticated logic to enable a feature for a specific audience, while our marketing team controls the related messaging to those same users.

To effectively coordinate feature rollout and messaging, we’ll create a new feature flag called show_loyalty_program. For our initial phased release, we’ll let Canvas control when and for whom the feature flag is enabled. For now, we’ll leave the rollout percentage at 0% and not select any target segments.

Then, in Canvas, we’ll create a Feature Flag step that enables the show_loyalty_program feature flag for our “High Value Customers” segment:

Now, users in this segment start to see the new loyalty program, and after it’s enabled, an email and survey are sent out automatically to help our teams gather feedback.

### Feature experimentation

Use feature flags to experiment and confirm your hypotheses around your new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

For feature flag experiments, you can have up to nine total groups: one control group plus up to eight variants.

An A/B test is a powerful tool that compares users’ responses to multiple versions of a variable.

In this example, our team has built a new checkout flow for our eCommerce app. Even though we’re confident it’s improving the user experience, we want to run an A/B test to measure its impact on our app’s revenue.

To begin, we’ll create a new feature flag called enable_checkout_v2. We won’t add an audience or rollout percentage. Instead, we’ll use a feature flag experiment to split traffic, enable the feature, and measure the outcome.

In our app, we’ll check if the feature flag is enabled or not and swap out the checkout flow based on the response:

- javascript
 
- java
 
- kotlin
 
- swift

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
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
 return <NewCheckoutFlow /> 
} else {
 return <OldCheckoutFlow />
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
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
 return new NewCheckoutFlow();
} else {
 return new OldCheckoutFlow();
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
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
 return NewCheckoutFlow()
} else {
 return OldCheckoutFlow()
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
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
 return NewCheckoutFlow()
} else {
 return OldCheckoutFlow()
}

```
 | 

We’ll set up our A/B test in a Feature Flag Experiment.

Now, 50% of users will see the old experience, while the other 50% will see the new experience. We can then analyze the two variants to determine which checkout flow resulted in a higher conversion rate.

Conversion Rate is the percentage of times a defined event occurred compared to all recipients of a message. This defined event is determined when you build the campaign.

Once we determine our winner, we can stop this campaign and increase the rollout percentage on the feature flag to 100% for all users while our engineering team hard-codes this into our next app release.

### Segmentation

Use the Feature Flag filter to create a segment or target messaging at users based on whether they have a feature flag enabled. For example, say you have a feature flag that controls premium content in your app. You could create a segment that filters for users who don’t have the feature flag enabled, and then send that segment a message urging them to upgrade their account to view premium content.

- Open your segment or message audience.
 
- Add the Feature Flag filter.
 
- Select the feature flag.
 
- Set the comparator to is to include users who have the feature flag enabled, or is not to include users who do not.

For more information about filtering on segments, see Creating a segment.

note

To prevent recursive segments, it is not possible to create a segment that references other feature flags.

## Plan limitations

These are the feature flag limitations for free and paid plans.

 Feature | 
 Free version | 
 Paid version | 

 Active feature flags | 
 10 per workspace | 
 110 per workspace | 

 Active campaign experiments | 
 1 per workspace | 
 100 per workspace | 

 Feature Flag Canvas steps | 
 Unlimited | 
 Unlimited | 

A feature flag is considered active and will count toward your limit if any of the following apply:

- Rollout is more than 0%
 
- Used in an active Canvas
 
- Used in an active experiment

Even if the same feature flag matches multiple criteria, such as if it’s used in a Canvas and the rollout is 50%, it will only count as 1 active feature flag toward your limit.

note

To purchase the paid version of feature flags, contact your Braze account manager, or request an upgrade in the Braze dashboard.

- 

New Stuff!
