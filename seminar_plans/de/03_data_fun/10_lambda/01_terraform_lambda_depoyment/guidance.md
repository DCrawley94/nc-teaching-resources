# Lambda Deployment with Terraform

Figjam: https://www.figma.com/board/S680JokHvjJXv2FnQf56Uh/Deploying-Lambdas-with-Terraform?node-id=1-2&t=M7rOEXmU1BmJb71e-1

## Learning Objectives

- Be aware of the steps we need to take when deploying a simple lambda function
- Know how to create the infrastructure required for lambda deployment in terraform
- Continue following good practices when writing terraform

## Introduction

Students should be familiar with the file reader function as it is the same one used for the lecture.

Ask them to think back and identify the steps that were taken in the console to deploy the file reader lambda.

Key steps taken:

- Lambda Creation:

  - function name
  - runtime
  - possibly changed the timeout?

- Code was pasted in directly

- IAM role (handled by the wizard 🪄)

  - Cloudwatch permissions

- S3 Read Permissions - added to the Lambda's IAM role

- S3 Event Notification - behind the scenes this created a resource based policy and also gave permission for s3 to invoke

We need to re-create that in terraform

## Creating the deployment package

- [AWS Documentation for Python Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
- [AWS Documentation for Python Deployment Packages](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
- [Terraform Archive File Data Source](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file)

During the lecture they will have seen the code pasted. Creating a deployment package will be new to them so don;t expect them to know how to do this. It will be useful to show them the docs to prove you aren't making it up and also give them a hint that they will need to do it a little different if their lambda has dependencies.

Information about `path.module`: https://developer.hashicorp.com/terraform/language/expressions/references#filesystem-and-workspace-info

```hcl
data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/../src/file_reader/reader.py"
  output_path = "${path.module}/../function.zip"
}
```

Reasons for uploading to S3 include [storage limitations](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), [benefits of bucket versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) and [security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) among others.

## Creating the lambda function

Look at the example usage in the [docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) and get students to point out things they recognise from the console deployment.

This will probably include `function_name`, `role`, `runtime`. New things will be `filename`, `handler`. Things that we're gonna ignore for now are `source_code_hash` and `environment`.

Look at the argument reference and point out that there are different args if you're using s3.

### IAM role

[Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role)

As seen in the example we need an IAM role so might as well start there.

**It will probably be helpful to show how the console wizard creates the IAM role and use it for reference.**

Ask students to tell you what their understanding of a role is. Address any misunderstandings. The passport analogy can be helpful here.

I'd recommend creating the trust policy as a separate resource (show what this is in the console).

```hcl
data "aws_iam_policy_document" "lambda_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}
```

Next create the IAM role:

```hcl
resource "aws_iam_role" "lambda_role" {
  name_prefix        = "role-${var.lambda_name}"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json
}
```

**This demos good practices with a variable that will be used later**

### Creating the lambda

Create the following resource block. Ask students to suggest what values to give for the arguments.

Students won't have seen `handler` before so quiz them on it and make sure they understand what is meant by an **entry point** for the code.

```hcl
resource "aws_lambda_function" "s3_file_reader" {
  function_name = var.lambda_name
  filename      = data.archive_file.lambda.output_path
  role          = aws_iam_role.lambda_role.arn
  handler       = "reader.lambda_handler"
  runtime       = "python3.12"
  timeout       = 10 # default 3 seconds can lead to timeout
}
```

---

Take a moment to run terraform apply and see the code get deployed.

Look at the IAM role permissions in the console and get students to tell you what is missing. This will lead you into writing the Cloudwatch permissions.

## Adding Cloudwatch Permissions

For this you can have look at how the cloudwatch permissions are created by the console wizard and essentially just recreate it wit students help.

For the resource arns you can make use of the data sources for region and caller identity to make your life easier and show their usefulness.

> Policy Doc data source

**START OFF BY COPYING STRAIGHT FROM CONSOLE INSTEAD OF USING DATA ATTRIBUTES**

```hcl
# data.tf

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}
```

AWS caller identity: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity

AWS region: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region

```hcl
data "aws_iam_policy_document" "cw_document" {
  statement {

    actions = ["logs:CreateLogGroup"]

    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
    ]
  }

  statement {

    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]

    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.lambda_name}:*"
    ]
  }
}
```

> Creation of policy resource

```hcl
resource "aws_iam_policy" "cw_policy" {
  name_prefix = "cw-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.cw_document.json
}
```

> Attaching policy to the role

```hcl
resource "aws_iam_role_policy_attachment" "lambda_cw_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.cw_policy.arn
}
```

**At this point re-deploy the code and see the changes**

Take questions and if there's time move onto the other parts of the deployment shown below.

## Extra Time:

### S3 Read Permissions for the data bucket

```hcl
data "aws_iam_policy_document" "s3_document" {
  statement {

    actions = ["s3:GetObject"]

    resources = [
      "${aws_s3_bucket.data_bucket.arn}/*",
    ]
  }
}
```

```hcl
resource "aws_iam_policy" "s3_policy" {
  name_prefix = "s3-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.s3_document.json
}
```

```hcl
resource "aws_iam_role_policy_attachment" "lambda_s3_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.s3_policy.arn
}
```

### S3 invoke Permission

```hcl
resource "aws_lambda_permission" "allow_s3" {
  action         = "lambda:InvokeFunction"
  function_name  = aws_lambda_function.s3_file_reader.function_name
  principal      = "s3.amazonaws.com"
  source_arn     = aws_s3_bucket.data_bucket.arn
  source_account = data.aws_caller_identity.current.account_id
}
```

### S3 Bucket Notification

```hcl
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.data_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.s3_file_reader.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}
```
