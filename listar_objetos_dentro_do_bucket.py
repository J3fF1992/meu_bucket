import boto3
from config_bucket import aws_access_key_id, aws_secret_access_key

# Replace with the name of your S3 bucket
bucket_name = 'teste-python-upload'

# Create a Boto3 client for S3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Replace with the prefix of the objects you want to list
# List all objects with the specified prefix
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if the response contains objects
if 'Contents' in response:
    objects = response['Contents']
    for obj in objects:
        print(obj['Key'])
else:
    print("The folder is empty or you don't have access to it.")
