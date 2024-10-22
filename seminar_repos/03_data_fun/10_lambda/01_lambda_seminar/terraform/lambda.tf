data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/../src/file_reader/reader.py"
  output_path = "${path.module}/../function.zip"
}


resource "aws_lambda_function" "s3_file_reader" {
  function_name = var.lambda_name
  s3_bucket     = aws_s3_bucket.code_bucket.bucket
  s3_key        = "s3_file_reader/function.zip"
  role          = aws_iam_role.lambda_role.arn
  handler       = "reader.lambda_handler"
  runtime       = "python3.12"
}
