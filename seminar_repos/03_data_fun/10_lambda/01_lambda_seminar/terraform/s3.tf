resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "nc-dc-de-code-"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket_prefix = "nc-dc-de-data-"
}

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key    = "s3_file_reader/function.zip"
  source = data.archive_file.lambda.output_path
}
