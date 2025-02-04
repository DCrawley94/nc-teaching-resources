data "aws_iam_policy_document" "assume_role" {
  # Who can hold the passport?
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

# Role: Passport
resource "aws_iam_role" "iam_for_lambda" {
  name               = "file_reader_iam_role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "aws_iam_policy_document" "cw_document" {
  statement {
    effect    = "Allow"
    actions   = ["logs:CreateLogGroup"]
    resources = ["arn:aws:logs:eu-west-2:026894960533:*"]
  }

  statement {
    effect  = "Allow"
    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]
    resources = [
    "arn:aws:logs:eu-west-2:026894960533:log-group:/aws/lambda/${var.lambda_name}:*"]
  }
}

resource "aws_iam_policy" "cw_policy" {
  name   = "lambda_cloudwatch_policy"
  policy = data.aws_iam_policy_document.cw_document.json
}

resource "aws_iam_role_policy_attachment" "lambda_cw_policy_attachment" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.cw_policy.arn
}



# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": "logs:CreateLogGroup",
#             "Resource": "arn:aws:logs:eu-west-2:026894960533:*"
#         },
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "logs:CreateLogStream",
#                 "logs:PutLogEvents"
#             ],
#             "Resource": [
#                 "arn:aws:logs:eu-west-2:026894960533:log-group:/aws/lambda/FUNCTION_NAME:*"
#             ]
#         }
#     ]
# }
