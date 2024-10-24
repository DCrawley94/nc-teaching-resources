import pytest
import os
import boto3
from moto import mock_aws

from src.example import create_file_report


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope="function")
def s3_client(aws_credentials):
    with mock_aws():
        # create bucket in fake aws (empty bucket)
        s3 = boto3.client("s3")
        yield s3  # PAUSES EXECUTION

        # CONTINUES AFTER TEST COMPLETION ...
        # IMPLICIT RETURN - CONTEXT CLOSES


@pytest.fixture(scope="function")
def s3_with_bucket(s3_client):
    s3_client.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    return s3_client


def test_returns_empty_bucket_message(s3_with_bucket):
    # invoked file_report - check the output
    result = create_file_report("test_bucket")

    assert result == "No objects found in test_bucket"


def test_returns_information_about_single_s3_object(s3_with_bucket):
    # create object within bucket
    s3_with_bucket.upload_file(
        f"{os.getcwd()}/test/test_files/rocks.json", "test_bucket", "rocks.json"
    )
    # invoked function + check return
    result = create_file_report("test_bucket")

    assert result == {
        "test_bucket": {
            "object_count": 1,
            "object_information": [{"key": "rocks.json", "file_size": 12568}],
        }
    }


@pytest.mark.skip
def test_returns_information_about_s3_objects():
    pass
