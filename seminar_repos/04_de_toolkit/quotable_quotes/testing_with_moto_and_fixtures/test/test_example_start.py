import boto3
from moto import mock_aws
import pytest
import os

from src.example import create_file_report


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


def test_returns_empty_bucket_message(aws_credentials):
    with mock_aws():
        boto3.client("s3").create_bucket(
            Bucket="test_bucket",
            CreateBucketConfiguration={
                "LocationConstraint": "eu-west-2"
                # We need to specify the location otherwise it will default to 'us-east-1'
            },
        )

        result = create_file_report("test_bucket")

        assert result == "No objects found in test_bucket"


def test_returns_information_about_single_s3_object(aws_credentials):
    with mock_aws():
        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="test_bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )
        test_file_directory = f"{os.getcwd()}/test/test_files"
        s3.upload_file(
            f"{test_file_directory}/rocks.json", "test_bucket", "rocks.json"
        )

        result = create_file_report("test_bucket")

        assert result == {
            "test_bucket": {
                "object_count": 1,
                "object_information": [
                    {"key": "rocks.json", "file_size": 12568}
                ],
            }
        }


def test_returns_information_about_multiple_s3_objects(aws_credentials):
    with mock_aws():
        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="test_bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )
        test_file_directory = f"{os.getcwd()}/test/test_files"
        s3.upload_file(
            f"{test_file_directory}/rocks.json", "test_bucket", "rocks.json"
        )
        s3.upload_file(
            f"{test_file_directory}/lakes.csv", "test_bucket", "lakes.csv"
        )
        s3.upload_file(
            f"{test_file_directory}/mountains.yaml",
            "test_bucket",
            "mountains.yaml",
        )

        result = create_file_report("test_bucket")

        assert result == {
            "test_bucket": {
                "object_count": 3,
                "object_information": [
                    {"key": "lakes.csv", "file_size": 5159},
                    {"key": "mountains.yaml", "file_size": 13773},
                    {"key": "rocks.json", "file_size": 12568},
                ],
            }
        }
