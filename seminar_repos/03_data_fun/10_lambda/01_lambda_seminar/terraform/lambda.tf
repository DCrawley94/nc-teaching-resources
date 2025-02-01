data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/../src/file_reader/reader.py"
  output_path = "${path.module}/../function.zip"
}


resource "aws_lambda_function" "s3_file_reader" {
  function_name = var.lambda_name
  filename      = data.archive_file.lambda.output_path
  role          = aws_iam_role.lambda_role.arn
  handler       = "reader.lambda_handler"
  runtime       = "python3.12"
}
