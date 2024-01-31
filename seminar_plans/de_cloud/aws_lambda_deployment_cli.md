# AWS Cli Lambda Deployment

Figjam: https://www.figma.com/file/wxZmn9ldpEZy83zanySIhg/CLI-Lambda-Deployment?type=whiteboard&node-id=0-1&t=4VCxD270InbZHcTi-0

## Learning Objectives

- Understand the complexities involved with deploying Cloud Infrastructure
- Have an awareness of steps that need to be taken as part of infrastructure deployment
- Know that infrastructure needs to be deployed in a certain order

## Intro - Figjam

### Previous Deployment - Console

Remind students about how we deployed a Lambda previously - on the AWS Console

Talk through the previous steps:

- mention the AdminAccess, is this a good idea?

### New Deployment - CLI

Talk through the new steps, point out that the order is a little different and the deployment steps are more granular.

**Stress that this is just the deployment steps for this Lambda - it will be different depending on what needs to be deployed**

**Also stress that we will be providing detailed instructions after the lecture so don't bother with screenshots today**

Show the AWS Infrastructure diagram, don't discuss it too much but explain that we will be referring back to these steps/diagram as we work through the deployment.

## Step 1: Creating the Buckets

❓ Ask students what I need to consider when creating bucket names:

- need to be unique

Therefore first thing I'm going to do is create a Suffix I can add to my bucket names to try an ensure uniqueness:

```sh
SUFFIX=$(date +%s)
```

The I can use this to create two bucket names:

```sh
DATA_BUCKET_NAME=nc-de-dc-data-${SUFFIX}
CODE_BUCKET_NAME=nc-de-dc-code-${SUFFIX}
```

I'm going to create these variables as I will need them later!

Next let's create the buckets:

```sh
aws s3 mb s3://${DATA_BUCKET_NAME}
aws s3 mb s3://${CODE_BUCKET_NAME}
```

And check we've done it correctly:

```sh
aws s3 ls
```

---

**🎉 ✅ 🎉 Tick off step 1 on FigJam 🎉 ✅ 🎉**

---

## Step 2

Next we need to create a deployment package for the Python code.

Show that there is [documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) on the structure needed to deploy a Python Lambda.

I'm not just making these things up and the steps could be different if I needed to deploy Python code with external dependencies such as installed libraries.

```sh
FUNCTION_NAME=s3-file-reader-${SUFFIX}
```

Next we create a zip archive as specified in the documentation:

```sh
cd src/file_reader
zip ../../function.zip reader.py
cd ../..
```

Copy the zip file to the S3 code bucket

> I don't technically need to store my code here, I could put the code directly to Lambda. However there is a limit to the size of a Lambda function so it can be useful to store the code in S3 instead.

```sh
aws s3 cp function.zip s3://${CODE_BUCKET_NAME}/${FUNCTION_NAME}/function.zip
```

And we can check if the zip file has arrived like so:

```sh
aws s3 ls ${CODE_BUCKET_NAME} --recursive --human-readable --summarize
```

---

**🎉 ✅ 🎉 Tick off step 2 on FigJam 🎉 ✅ 🎉**

---

## The S3 IAM Policy

Start off by explaining that I'm going to be using the IAM create-policy command which can be seen [here](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html)

The main input for this function is an AWS policy file in `json` format.

Thankfully we already have a template.

Explain that I'm going to manually add in the relevant resource ARNs. I could do this a bit more programmatically but for learning purposes we're doing this manually.

File should looks like this:

**REMEMBER THE TRAILING /\***

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": ["s3:GetObject"],
			"Resource": [
				"arn:aws:s3:::CODE_BUCKET_NAME/*",
				"arn:aws:s3:::DATA_BUCKET_NAME/*"
			]
		}
	]
}
```

> Highlight that the trailing '/\*' allows GetObject to the contents on the bucket

> If we just had this policy for the bucket itself it wouldn't work

Now we can run the `create-policy` command. It will be useful later to have the ARN for this policy so I'm going to extract it from the command response with `jq`.

```sh
S3_READ_POLICY_ARN=$(aws iam create-policy --policy-name s3-read-policy-${FUNCTION_NAME} \
--policy-document file://deployment/templates/s3_read_policy_template.json | jq .Policy.Arn | tr -d '"')
```

---

**🎉 ✅ 🎉 Tick off step 3 on FigJam 🎉 ✅ 🎉**

---

## Step 4 - Cloudwatch Policy

The steps to creating a Cloudwatch Policy is very similar.

The Cloudwatch Policy should end up looking like this:

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "logs:CreateLogGroup",
			"Resource": "arn:aws:logs:eu-west-2:AWS_ACCOUNT_ID:*"
		},
		{
			"Effect": "Allow",
			"Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
			"Resource": [
				"arn:aws:logs:eu-west-2:AWS_ACCOUNT_ID:log-group:/aws/lambda/FUNCTION_NAME:*"
			]
		}
	]
}
```

For this I need to know my Account ID. Thankfully there's a nice way to get this on the command line:

```sh
AWS_ACCOUNT_ID=$(aws sts get-caller-identity | jq .Account | tr -d '"')
```

I'm going to save it to a variable as it will come in useful later.

Once I've edited the policy document I can create the policy:

```sh
CLOUDWATCH_POLICY_ARN=$(aws iam create-policy --policy-name cloudwatch-policy-${FUNCTION_NAME} \
--policy-document file://deployment/templates/cloudwatch_log_policy_template.json | jq .Policy.Arn | tr -d '"')
```

---

**🎉 ✅ 🎉 Tick off step 4 on FigJam 🎉 ✅ 🎉**

**☕ BREAK TIME ☕**

---

## Step 5 : The IAM Role

Next we need to create a role, we can do this with [this command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html).

The main thing we need to provide is a Trust Policy.

A trust policy simply says who or what holds the permissions. In this case, the AWS Lambda service can be granted the permissions. If I tried to give this role to another service (or user) I would not be able to.

**PASSPORT ID PAGE**

```txt
Passport Analogy:

Trust Policy is like ID page (I couldn't use Joe's passport) - controls which identity can can assume a role
Role is the Passport itself, allowing travel - gives access to multiple services etc..
Policy is a boarding pass, the thing that actually let's you board a flight - you are not allowed access unless specifically allowed
```

In this case a trust policy has been provided, we don't need to change anything. The trust policy will allow only lambda functions to assume the role.

We can create it like this:

```sh
EXECUTION_ROLE_ARN=$(aws iam create-role --role-name lambda-execution-role-${FUNCTION_NAME} \
--assume-role-policy-document file://deployment/trust_policy.json | jq .Role.Arn | tr -d '"')
```

This creates a role but currently it has no permissions attached to it. So now we need to attach the policies we created earlier:

```sh
aws iam attach-role-policy --policy-arn ${CLOUDWATCH_POLICY_ARN} --role-name lambda-execution-role-${FUNCTION_NAME}
aws iam attach-role-policy --policy-arn ${S3_READ_POLICY_ARN} --role-name lambda-execution-role-${FUNCTION_NAME}
```

---

**🎉 ✅ 🎉 Tick off step 5 on FigJam 🎉 ✅ 🎉**

---

## Step 6: Creating the function

Time to create a function. [Documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html)

```sh
aws lambda create-function \
--function-name ${FUNCTION_NAME} \
--runtime python3.11 \
--role ${EXECUTION_ROLE_ARN} \
--package-type Zip \
--handler reader.lambda_handler \
--code S3Bucket=${CODE_BUCKET_NAME},S3Key=${FUNCTION_NAME}/function.zip
```

To explain the arguments individually:

- function-name is compulsory and we just pass our previously defined variable for this.
- role is compulsory and we use the variable that contains our role ARN.
- runtime is required when a zip file is used so that Lambda knows what language and version to expect. At the time of writing, python3.11 is the default (and latest) Python version allowed.
- package-type could be Image (for a Docker image), but for us a zip file is adequate.
- handler tells Lambda which file and function to use as the entry point for code execution.
- code indicates the code location.

---

**🎉 ✅ 🎉 Tick off step 6 on FigJam 🎉 ✅ 🎉**

---

## Step 7: Resource Permission

There is one more permission to add: We need to allow the Lambda Function to be called by S3.

For this we need a [**resource-based permission**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html)

First we need to make a small edit to the provided policy template:

```json
{
	"LambdaFunctionConfigurations": [
		{
			"LambdaFunctionArn": "arn:aws:lambda:eu-west-2:AWS_ACCOUNT_ID:function:FUNCTION_NAME",
			"Events": ["s3:ObjectCreated:*"]
		}
	]
}
```

And run the command to add the permission:

```sh
aws lambda add-permission \
--function-name ${FUNCTION_NAME} \
--principal s3.amazonaws.com \
--statement-id s3invoke \
--action "lambda:InvokeFunction" \
--source-arn arn:aws:s3:::${DATA_BUCKET_NAME} \
--source-account ${AWS_ACCOUNT_ID}
```

The statement_id field is nothing special - just a human-readable indicator to remind us what this is for.

---

**🎉 ✅ 🎉 Tick off step 7 on FigJam 🎉 ✅ 🎉**

---

## Step 8: Event Notification

The final step is to add an event notification to S3 so that the Lambda is triggered when any new object is added to the data bucket.

For that we need a configuration file in this structure:

```json
{
	"LambdaFunctionConfigurations": [
		{
			"LambdaFunctionArn": "arn:aws:lambda:eu-west-2:AWS_ACCOUNT_ID:function:FUNCTION_NAME",
			"Events": ["s3:ObjectCreated:*"]
		}
	]
}
```

We just need to substitute the value in for `AWS_ACCOUNT_ID` and `FUNCTION_NAME`.

And the command to create the event notification is this:

```sh
aws s3api put-bucket-notification-configuration \
--bucket ${DATA_BUCKET_NAME} \
--notification-configuration file://deployment/templates/s3_event_config_template.json
```

## Wrapping Up

Let's test the deployment works. For that I need a small text file - Blue Peter styles have one ready.

Then I can copy it to the S3 Data Bucket like so:

```sh
aws s3 cp zen.txt s3://${DATA_BUCKET_NAME}/data/zen.txt
```

Wait a moment for it to complete and then check the Lambda logs:

```sh
aws logs tail /aws/lambda/${FUNCTION_NAME}
```

If this **does work** then 🎉🎉🎉🎉🎉🎉🎉 - ww can see the file contents being logged.

If it **doesn't work** then 😢😢😢😢😢😢😢 - talk about how a tiny little mistake can break a deployment. My next step would be to inspect the policies manually and identify the issue.

## Conclude

So has this actually helped us at all?

- It's still a very step by step process
- It's still very manual
- **However** what we've seen is that we can perform the deployment with _code_. This means that the process can be automated, making it repeatable, efficient and much less susceptible to human error.

We could be all means take these commands and turn them into a bash script. However there are better tools for the job, namely Terraform, that we will show you tomorrow.
