import boto3
from config_bucket import aws_access_key_id, aws_secret_access_key

# Replace with the name of your S3 bucket
bucket_name = 'teste-python-upload'

# Replace with the object key (name) you want to download from S3
s3_object_key = 'upload_arquivo_teste.txt'

# Replace with the local file path where you want to save the downloaded file
local_file_path = r'C:\Users\Jefferson Reis\OneDrive - PROVU SERV. DE ADM. E CORRESPONDENTE BANCARIO SA\Documentos\Desenvolvimento\meu_bucket\donwload_bucket\upload_arquivo_teste.txt'

# Create a Boto3 client for S3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Perform the file download
try:
    response = s3_client.download_file(bucket_name, s3_object_key, local_file_path)
    print(f"File downloaded successfully from S3 with key: {s3_object_key}")
except Exception as e:
    print(f"Error downloading the file: {e}")
