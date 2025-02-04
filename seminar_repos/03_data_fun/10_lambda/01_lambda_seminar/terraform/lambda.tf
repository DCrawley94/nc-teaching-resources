variable "lambda_name" {
  type    = string
  default = "s3-file-reader"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../src/file_reader/reader.py"
  output_path = "${path.module}/../function.zip"
}

resource "aws_lambda_function" "file_reader" {
  filename      = data.archive_file.lambda_zip.output_path
  function_name = var.lambda_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "reader.lambda_handler"
  runtime       = "python3.12"
}
