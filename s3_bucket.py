import boto3
from flask import Response

S3 = "s3"


def file_upload(filename: str, bucket: str) -> Response:
    """
    The function uploads a file to an S3 bucket.
    """
    object_name = filename
    s3 = boto3.client(S3)
    response = s3.upload_file(filename, bucket, object_name)

    return response


def file_download(filename: str, bucket: str) -> str:
    """
    The function downloads a file from an S3 bucket.
    """
    s3 = boto3.resource(S3)
    output = f"downloads/{filename}"
    s3.Bucket(bucket).download_file(filename, output)

    return output


def list_of_files(bucket: str) -> list:
    """
    The function returns a list of existing files.
    """
    contents = []
    s3 = boto3.client(S3)

    try:
        for value in s3.list_objects(Bucket=bucket)["Contents"]:
            contents.append(value)
    except Exception as e:
        print(e)

    return contents
