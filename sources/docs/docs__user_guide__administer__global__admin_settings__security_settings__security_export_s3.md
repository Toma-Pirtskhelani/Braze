---
url: https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/security_export_s3
slug: docs__user_guide__administer__global__admin_settings__security_settings__security_export_s3
title: "Security events export with Amazon S3"
description: "This reference article covers how to automatically export security events every day at midnight UTC to Amazon S3."
section: user_guide/administer
fetched: 2026-09-02
evidence: company-own (technical)
---
# Security events export with Amazon S3

You can automatically export security events to Amazon S3, a cloud storage provider, with a daily job that runs at midnight UTC. After setting up, you don’t need to manually export security events from the dashboard. The job exports the security events for the past 24 hours in CSV format to your configured S3 storage. The CSV file uses the same columns as a manually exported report, plus a Version column.

note

The 10,000-row limit applies only to the manual CSV report download from the dashboard. Security event exports to S3 aren’t subject to this row limit.

Braze supports two different S3 authentication and authorization methods for setting up Amazon S3 export:

- AWS secret access key method
 
- AWS role ARN method

## AWS secret access key method

This method generates a secret key and an access key ID that allows Braze to authenticate as a user on your AWS account to write data to your bucket.

### Step 1: Create an Identity and Access Management (IAM) user

To retrieve your secret access key and access key ID, you’ll need to create an IAM user, following the instructions in Setting up your AWS account.

### Step 2: Get credentials

- After creating a new user, generate the access key and download your access key ID and secret access key.

- Take note of these credentials somewhere or download the credential files, because you’ll need to input these into Braze later on.

### Step 3: Create policy

- Go to IAM (Identity and Access Management) > Policies > Create Policy to add permissions for your user.
 
- Select Create Your Own Policy, which gives limited permissions so Braze can only access the specified buckets.
 
- Specify a policy name of your choice.
 
- Input the following code snippet into the Policy Document section. Be sure to replace “INSERTBUCKETNAME” with your bucket name. Without these permissions, the integration will fail a credentials check and not be created.

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
{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
 "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
 },
 {
 "Effect": "Allow",
 "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
 "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
 }
 ]
}

```
 | 

### Step 4: Attach policy

- After creating a new policy, go to Users and select your specific user.
 
- In the Permissions tab, select Add Permissions, directly attach the policy, and then select that policy.

Now, you’re ready to link your AWS credentials to your Braze account!

### Step 5: Link Braze to AWS

- In Braze, go to Settings > Company Settings > Admin Settings > Security Settings and scroll to the Security Event Download section.
 
- Toggle on Export to AWS S3 under Export to cloud storage and select AWS secret access key, which enables the S3 export.
 
- Input the following:

- AWS access key ID
 
- AWS bucket name
 
- AWS secret access key

- When inputting this key, first select Test Credentials to confirm your credentials work.

- Select Save Changes.

You’ve integrated AWS S3 into your Braze account!

## AWS role ARN method

The AWS role ARN method generates a role Amazon Resource Name (ARN) that allows the Braze Amazon account to authenticate as a member of that role.

### Step 1: Create policy

- Sign in to the AWS management console as an account administrator.
 
- In the AWS console, go to the IAM (Identity and Access Management) section > Policies, and then select Create Policy.

- Open the JSON tab and input the following code snippet into the Policy Document section. Be sure to replace INSERTBUCKETNAME with your bucket name.

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
 {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
 "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
 },
 {
 "Effect": "Allow",
 "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
 "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
 }
 ]
}

```
 | 

- Select Next after reviewing the policy.

- Give the policy a name and description, and then select Create Policy.

### Step 2: Create role

- In Braze, go to Settings > Company Settings > Admin Settings > Security Settings and scroll to the Security Event Download section.
 
- Select AWS Role ARN.
 
- Take note of the identifiers, Braze account ID, and Braze external ID needed to create your role.

- In the AWS console, go to the IAM (Identity and Access Management) section > Roles > Create Role.
 
- Select Another AWS Account as the trusted entity selector type.
 
- Provide your Braze account ID, check the Require external ID box, and then enter your Braze external ID.
 
- Select Next when complete.

### Step 3: Attach policy

- Search for the policy you created earlier in the search bar, and then place a checkmark next to the policy to attach it.
 
- Select Next.

- Give the role a name and a description, and select Create Role.

Your newly created role will appear in the list!

### Step 4: Link to Braze AWS

- In the AWS Console, find your newly created role in the list. Select the name to open up the details of that role, and take note of the ARN.

- In Braze, go to Settings > Company Settings > Admin Settings > Security Settings and scroll to the Security Event Download section.

- Make sure AWS role ARN is selected, then input your role ARN and AWS S3 bucket name in the designated fields.
 
- Select Test Credentials to confirm your credentials work properly.
 
- Select Save Changes.

You’ve integrated AWS S3 into your Braze account!

- 

New Stuff!
