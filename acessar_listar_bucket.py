import boto3                    #lib para se conectar com aws
from config_bucket import aws_access_key_id, aws_secret_access_key      #import das credenciais

# Create a Boto3 client for S3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)    #variavel com as credencias 

# List all buckets
response = s3_client.list_buckets()     #lista os bucket do repositorio
bucket_name = 'teste-python-upload'

# Check if the response contains buckets
if 'Buckets' in response:
    buckets = response['Buckets']
    for bucket in buckets:
        print(bucket['Name'])
else:
    print("Bucket não localizado.")

bucket_name = 'teste-python-upload'