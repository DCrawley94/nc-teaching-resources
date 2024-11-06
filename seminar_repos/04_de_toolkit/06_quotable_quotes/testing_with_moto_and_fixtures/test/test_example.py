from src.example import create_file_report

from moto import mock_aws
import boto3
import pytest
import os


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


# fixture that creates and s3 bucket


@pytest.fixture
def s3_client(aws_credentials):
    with mock_aws():
        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="test-bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )
        yield s3  # pause execution for the duration of the test

    # .... carry on execution after test


def test_returns_empty_bucket_message(s3_client):
    """
    Function should return "No objects found in BUCKET_NAME" when
    given bucket is empty.
    """

    assert create_file_report("test-bucket") == "No objects found in test-bucket"


def test_returns_information_about_single_s3_object(s3_client):
    """
    Function should return a file report for a bucket containing
    a single object.
    """

    test_file_directory = f"{os.getcwd()}/test/test_files"
    s3_client.upload_file(
        f"{test_file_directory}/rocks.json", "test-bucket", "rocks.json"
    )

    assert create_file_report("test-bucket") == {
        "test-bucket": {
            "object_count": 1,
            "object_information": [{"key": "rocks.json", "file_size": 12568}],
        }
    }


@pytest.mark.skip
def test_returns_information_about_multiple_s3_objects():
    """
    Function should return a file report for a bucket containing
    a single object.
    """
