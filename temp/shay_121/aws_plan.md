# Steps

## Create IAM role:

```hcl
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "monster-lambda-iam-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
```

## Deploy Lambda

Docs: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

```hcl
data "archive_file" "monster_lambda" {
  type        = "zip"
  source_file = "${path.module}/../monster_lambda.py"
  output_path = "${path.module}/../lambda_function_payload.zip"
}

resource "aws_lambda_function" "monster_lambda" {
  filename      = data.archive_file.monster_lambda.output_path
  function_name = "monster_lambda"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "monster_lambda.lambda_handler"

  runtime = "python3.13"

  environment {
    variables = {
      BUCKET = aws_s3_bucket.dnd_bucket.id
    }
  }
}
```

## Create lambda layer:

Docs: https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html

`pip install -t ...`

```hcl
resource "aws_lambda_layer_version" "requests_layer" {
  filename   = "${path.module}/../lambda_layer_payload.zip"
  layer_name = "requests_layer"

  compatible_runtimes = ["python3.13"]
}
```

```hcl
<!-- lambda -->
layers = [aws_lambda_layer_version.requests_layer.arn]
```

## Cloudwatch policy

Create an example lambda for demo:

```hcl
data "aws_iam_policy_document" "cw_document" {
  statement {
    effect    = "Allow"
    actions   = ["logs:CreateLogGroup"]
    resources = ["arn:aws:logs:eu-west-2:${data.aws_caller_identity.current.account_id}:*"]
  }

  statement {
    effect  = "Allow"
    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]
    resources = [
    "arn:aws:logs:eu-west-2:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/monster_lambda:*"]
  }
}

resource "aws_iam_policy" "cw_policy" {
  name   = "cw_policy"
  policy = data.aws_iam_policy_document.cw_document.json
}

resource "aws_iam_policy_attachment" "cw_policy_attach" {
  name       = "cw_policy_attach"
  roles      = [aws_iam_role.iam_for_lambda.name]
  policy_arn = aws_iam_policy.cw_policy.arn
}
```

## Other policies:

```hcl
data "aws_iam_policy_document" "s3_policy_doc" {
  statement {
    effect = "Allow"
    actions = [
      "s3:PutObject",
      "s3:GetObject",
    ]
    resources = [
      "${aws_s3_bucket.dnd_bucket.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "s3_policy" {
  name   = "s3_policy"
  policy = data.aws_iam_policy_document.s3_policy_doc.json
}

resource "aws_iam_policy_attachment" "s3_policy_attach" {
  name       = "s3_policy_attach"
  roles      = [aws_iam_role.iam_for_lambda.name]
  policy_arn = aws_iam_policy.s3_policy.arn
}
```
