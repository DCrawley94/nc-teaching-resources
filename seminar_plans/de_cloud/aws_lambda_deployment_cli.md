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

**🎉 ✅ 🎉 Tick off step one on FigJam 🎉 ✅ 🎉**

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

**🎉 ✅ 🎉 Tick off step two on FigJam 🎉 ✅ 🎉**

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
			"Resource": ["arn:aws:s3:::BUCKET_NAME/*", "arn:aws:s3:::BUCKET_NAME/*"]
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

**🎉 ✅ 🎉 Tick off step two on FigJam 🎉 ✅ 🎉**

---
