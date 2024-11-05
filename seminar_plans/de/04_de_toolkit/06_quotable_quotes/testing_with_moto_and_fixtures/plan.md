# Testing with Moto and Fixtures

## Learning Objectives

- Know how to test python code with moto
- Explore how we can make use of pytest fixtures to improve out testing

## Warm Up

On Figjam:

Why do we need a tool like `moto` when testing code that uses `boto3`?

- we don't want to accidentally create/update/delete infrastructure on our actual AWS accounts
- can be done with Mock/Patch but `moto` makes it much easier

## Write Initial Tests

Have the code pre-written and test functions written but not implemented - no credentials fixture yet

### First test:

**PSEUDOCODE ALL TESTS BEFORE IMPLEMENTING**

**Suppress deprecation warning:** `pytest -W ignore::DeprecationWarning` **OR** `pytest --disable-warnings`

Work towards the solution shown below. Key points to make:

- `aws_credentials` fixture to avoid affecting real infra (will cover your back if you forget to use `mock_aws`) - **MAKE SURE THIS FIXTURE IS USED IN TESTS**
  - This will act in a similar way for moto but also covers your back if you make a mistake
- `create_bucket` region
  - invoke `create_bucket` without config at first unless students tell me otherwise - see the error and ask students to identify the issue (defaults to `us-east-1`)
- context manager for `mock_aws` to ensure that any created infra is done with moto - not on my actual account
  - can illustrate the use of this by showing what happens if I "forget" to use `mock_aws`

**If students really want to we can make an s3 client fixture but no bucket one!**

```py
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
            Bucket="test-bucket",
            CreateBucketConfiguration={
                "LocationConstraint": "eu-west-2"
                # We need to specify the location otherwise it will default to 'us-east-1'
            },
        )

        result = create_file_report("test-bucket")

        assert result == "No objects found in test-bucket"
```

**STUDENTS MIGHT ASK TO DO S3_CLIENT FIXTURE - THIS IS A GREAT OPPORTUNITY FOR AN EARLY FIXTURE REFACTOR - START WITH CODE ABOVE AND REFACTOR TO FIXTURE BELOW**

**REALLY HAMMER HOME THAT YIELD IS PAUSING THE EXECUTION WHILE STILL IN MOCK_AWS CONTEXT!!!**

```py
@pytest.fixture
def s3_client(aws_credentials):
    with mock_aws():
        yield boto3.client("s3")


def test_returns_empty_bucket_message(s3_client):
    s3_client.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={
            "LocationConstraint": "eu-west-2"
            # We need to specify the location otherwise it will default to 'us-east-1'
        },
    )

    result = create_file_report("test_bucket")

    assert result == "No objects found in test_bucket"
```

### Second Test

**PSEUDOCODE BEFORE IMPLEMENTING**

Work towards the solution shown below. Key points to make:

- We need to recreate the s3 connection and bucket each time - _Wouldn't it be nice if we didn't have to do this each time? 👀_
- Upload local file to bucket, I'm gonna use method from `os` library (`os.getcwd()`) to get path to test file
- could do put object but a more appropriate one could be `upload_file`
- I know what the file size is by checking with a cheeky bash command: `wc -c test/test_files/*`

```py
@pytest.mark.skip
def test_returns_information_about_single_s3_object(aws_credentials):
    with mock_aws():
        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="test-bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )

        test_file_directory = f"{os.getcwd()}/test/test_files"
        s3.upload_file(f"{test_file_directory}/rocks.json", "test-bucket", "rocks.json")

        result = create_file_report("test-bucket")

        assert result == {
            "test-bucket": {
                "object_count": 1,
                "object_information": [{"key": "rocks.json", "file_size": 12568}],
            }
        }
```

### Test 3: **Probably breeze over this to get onto fixtures - only difference from previous code is extra objects**

- CAN JUST TALK ABOUT THIS RATHER THAN IMPLEMENT

```py
def test_returns_information_about_multiple_s3_objects(aws_credentials):
    with mock_aws():
        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="test_bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )
        test_file_directory = f"{os.getcwd()}/test/test_files"
        s3.upload_file(f"{test_file_directory}/rocks.json", "test_bucket", "rocks.json")
        s3.upload_file(f"{test_file_directory}/lakes.csv", "test_bucket", "lakes.csv")
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
```

## Fixtures Refactor:

**BEFORE THIS TALK ABOUT TESTING THE ERROR AND HOW THAT COULD BE DONE**

**Ask students to take a look at the tests we've written and see if there's anything that could maybe be improved**

If they're struggling point them towards the arranging part of the test

Repeated code:

- create s3 connection
- create bucket
- uploading files

How might we avoid this and clean up our tests a bit?

**🎉 F I X TU R E S 🎉**

**Yield keeps `mock_aws` context active for the duration of the test**

Refactor:

```py
@pytest.fixture
def s3_client(aws_credentials):
    with mock_aws():
        yield boto3.client("s3")


@pytest.fixture
def s3_with_bucket(s3_client):
    s3_client.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={
            "LocationConstraint": "eu-west-2"
            # We need to specify the location otherwise it will default to 'us-east-1'
        },
    )
    return s3_client


@pytest.fixture()
def s3_single_object(s3_with_bucket):
    test_file_directory = f"{os.getcwd()}/test/test_files"
    s3_with_bucket.upload_file(
        f"{test_file_directory}/rocks.json", "test_bucket", "rocks.json"
    )


@pytest.fixture()
def s3_multiple_object(s3_with_bucket):
    test_file_directory = f"{os.getcwd()}/test/test_files"
    s3_with_bucket.upload_file(
        f"{test_file_directory}/rocks.json", "test_bucket", "rocks.json"
    )
    s3_with_bucket.upload_file(
        f"{test_file_directory}/lakes.csv", "test_bucket", "lakes.csv"
    )
    s3_with_bucket.upload_file(
        f"{test_file_directory}/mountains.yaml",
        "test_bucket",
        "mountains.yaml",
    )



def test_returns_empty_bucket_message(s3_with_bucket):
    result = create_file_report("test_bucket")

    assert result == "No objects found in test_bucket"
```

Can then discuss how you could go on to create fixtures that do more like uploading the files etc.
