from src.example import create_file_report

import pytest


def test_returns_empty_bucket_message():
    """
    Function should return "No objects found in BUCKET_NAME" when
    given bucket is empty.
    """


@pytest.mark.skip
def test_returns_information_about_single_s3_object():
    """
    Function should return a file report for a bucket containing
    a single object.
    """


@pytest.mark.skip
def test_returns_information_about_multiple_s3_objects():
    """
    Function should return a file report for a bucket containing
    a single object.
    """
