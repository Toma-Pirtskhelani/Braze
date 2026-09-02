---
url: https://www.braze.com/docs/user_guide/data/distribution/braze_currents/use_cases/transferring_data_to_redshift
slug: docs__user_guide__data__distribution__braze_currents__use_cases__transferring_data_to_redshift
title: "Transfer data to Redshift"
description: "This how-to article will walk you through how to transfer data from Amazon S3 to Redshift through an Extract, Transform, Load (ETL) process."
section: user_guide/data
fetched: 2026-09-02
evidence: company-own (technical)
---
# Transfer data to Redshift

Amazon Redshift is a popular data warehouse that runs on Amazon Web Services alongside Amazon S3. Braze data from Currents is structured for direct transfer to Redshift.

The following describes how to transfer data from Amazon S3 to Redshift through an Extract, Transform, Load (ETL) process. For the full source code, refer to the Currents examples GitHub repository.

important

This is only one of many options you can choose from when it comes to transferring your data to places that would be most advantageous to you.

## S3 to Redshift loader overview

The s3loader.py script uses a separate manifest table in the same Redshift database to keep track of the files that have already been copied. The general structure is as follows:

- List all of the files in S3, then identify the new files since the last time you ran s3loader.py by comparing the list with the contents in the manifest table.
 
- Create a manifest file containing the new files.
 
- Execute a COPY query to copy the new files from S3 to Redshift using the manifest file.
 
- Insert the names of the files that are copied into the separate manifest table in Redshift.
 
- Commit.

## Dependencies

You must install the AWS Python SDK and Psycopg in order to run the loader:

```

1
2

```
 | 
```
pip install boto3
pip install psycopg2

```
 | 

## Permissions

### Redshift role with S3 read access

If you have not done so, follow the AWS documentation to create a role that can execute COPY commands on your files in S3.

### Redshift VPC inbound rules

If your Redshift cluster is in a VPC, you must configure the VPC to allow connections from the server that you are running the S3 Loader on. Go into your Redshift Cluster and select the VPC Security Groups entry that you want the loader to connect to. Then, add a new inbound rule: Type = Redshift, Protocol = TCP, Port = the port for your cluster, Source = the IP of the server running the loader (or “Anywhere” for testing).

### Identity and Access Management (IAM) user with S3 full access

The S3 loader requires read access to the files containing your Currents data, and full access to the location for the manifest files that it generates for the Redshift COPY commands. Create a new Identity and Access Management (IAM) user with the AmazonS3FullAccess permission from the IAM console. Save the credentials, as you’ll need to pass them to the loader.

You can pass the access credentials to the loader through environment variables, the shared credential file (~/.aws/credentials), or the AWS config file. Alternatively, you may include them directly in the loader by assigning them to the aws_access_key_id and the aws_secret_access_key fields within an S3LoadJob object, but we do not recommend hard coding credentials within your source code.

## Usage

### Sample usage

The following sample program loads data for the users.messages.contentcard.Impression event from S3 to the content_card_impression table in Redshift.

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

```
 | 
```
if __name__ == '__main__':
 host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
 port = 5439
 database = '{YOUR_DATABASE}'
 user = '{YOUR_USER}'
 password = '{YOUR_PASSWORD}'
 role = '{YOUR_REDSHIFT_ROLE_ARN}'

 # Do not hard code these credentials.
 aws_access_key_id = None
 aws_secret_access_key = None

 # Content Card Impression Avro fields:
 # id - string
 # user_id - string
 # external_user_id - string (nullable)
 # app_id - string
 # content_card_id - string
 # campaign_id - string (nullable)
 # send_id - string (nullable)
 # time - int
 # platform - string (nullable)
 # device_model - string (nullable)

 print('Loading Content Card Impression...')
 cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
 cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
 cc_impression_redshift_table = 'content_card_impression'
 cc_impression_redshift_column_def = [
 ('id', 'text'),
 ('user_id', 'text'),
 ('external_user_id', 'text'),
 ('app_id', 'text'),
 ('content_card_id', 'text'),
 ('campaign_id', 'text'),
 ('send_id', 'text'),
 ('time', 'integer'),
 ('platform', 'text'),
 ('device_model', 'text')
 ]

 cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
 cc_impression_redshift_table, cc_impression_redshift_column_def)
 cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

 cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
 aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
 cc_impression_job.perform()

```
 | 

### Credentials

To run the loader, you must first provide the host, port, and database of your Redshift cluster as well as the user and password of a Redshift user that can run COPY queries. Additionally, you must provide the ARN of the Redshift role with S3 read access that you created in a previous section.

```

1
2
3
4
5
6

```
 | 
```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'

```
 | 

### Job configuration

You must provide the S3 bucket and prefix of your event files, as well as the Redshift table name that you want to COPY into.

In addition, to COPY Avro files with the “auto” option as required by the loader, the column definition in your Redshift table must match the field names in the Avro schema as shown in the sample program, with the appropriate type mapping (for example, string to text, int to integer).

You may also pass a batch_size option to the loader if you find that it takes too long to copy all of the files at once. Passing a batch_size allows the loader to incrementally copy and commit one batch at a time without having to copy everything at the same time. The time it takes to load one batch depends on the batch_size as well as the size of your files and the size of your Redshift cluster.

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

```
 | 
```
# Content Card Impression Avro fields:
# id - string
# user_id - string
# external_user_id - string (nullable)
# app_id - string
# content_card_id - string
# campaign_id - string (nullable)
# send_id - string (nullable)
# time - int
# platform - string (nullable)
# device_model - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
 ('id', 'text'),
 ('user_id', 'text'),
 ('external_user_id', 'text'),
 ('app_id', 'text'),
 ('content_card_id', 'text'),
 ('campaign_id', 'text'),
 ('send_id', 'text'),
 ('time', 'integer'),
 ('platform', 'text'),
 ('device_model', 'text')
]
cc_impression_batch_size = 1000

```
 | 

- 

New Stuff!
