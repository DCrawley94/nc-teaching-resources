import boto3
from botocore.exceptions import ClientError

"""
    Creates an easily digestible report about the contents of a given s3 bucket

    Should create a report that looks like this:

    {
        "example-bucket": {
            "object_count": 3,
            "object_information": [
                {"key": "lakes.csv", "file_size": 5159},
                {"key": "mountains.yaml", "file_size": 13773},
                {"key": "rocks.json", "file_size": 12568},
            ],
        }
    }

    Arguments:
        bucket_name: name of the bucket to create a report for
"""


def create_file_report(bucket_name):
    try:
        s3 = boto3.client("s3")
        bucket_data = s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in bucket_data:
            # Create and return file report
            response = {
                bucket_name: {
                    "object_count": bucket_data["KeyCount"],
                    "object_information": [
                        {"key": obj["Key"], "file_size": obj["Size"]}
                        for obj in bucket_data["Contents"]
                    ],
                }
            }

            return response

        # Return message if no contents found
        return f"No objects found in {bucket_name}"
    except ClientError as c:
        return f"ClientError occurred: {c}"
