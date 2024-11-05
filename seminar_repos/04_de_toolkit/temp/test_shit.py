from shit import listin
from moto import mock_aws

import boto3
import pytest
import os


@mock_aws
def test_stuff():
    # dependancy inject and imports don't matter
    
    assert listin() == ['yeet']
