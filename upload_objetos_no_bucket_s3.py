import boto3
from config_bucket import aws_access_key_id, aws_secret_access_key

# Replace with the name of your S3 bucket
bucket_name = 'teste-python-upload'

# Replace with the local file path you want to upload
local_file_path = r'C:\Users\Jefferson Reis\Documents\desenvolvimento\bucket_aws\upload_bucket\upload_arquivo_teste.txt'

# Replace with the desired key (object name) under which you want to store the file in S3
s3_object_key = 'upload_arquivo_teste.txt'

# Create a Boto3 client for S3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Perform the file upload
try:
    response = s3_client.upload_file(local_file_path, bucket_name, s3_object_key)
    print(f"File uploaded successfully to S3 with key: {s3_object_key}")
except Exception as e:
    print(f"Error uploading the file: {e}")
