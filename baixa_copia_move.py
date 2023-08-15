import boto3
import os
import datetime
from config_bucket import aws_access_key_id, aws_secret_access_key


bucket_origem = 'teste-python-upload'   # Nome dos buckets
bucket_destino = 'teste-python-download'
diretorio_local = 'C:\\Users\\Jefferson Reis\\Documents\\Nova pasta\\bucket_download\\' # Pasta local para as cópias em PDF
s3_cliente = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)  # Criar cliente S3
lista = s3_cliente.list_objects(Bucket=bucket_origem) # Listra objetos no bucket de origem

for obj in lista.get('Contents', []):        #lista os objetos no bucekt origem
    nome_arquivo = obj['Key']

    lista = s3_cliente.get_object(Bucket=bucket_origem, Key=nome_arquivo)
    conteudo = lista['Body'].read()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # Gerar um timestamp     
    novo_nome_arquivo_pdf = f'novo_{nome_arquivo}_{timestamp}.pdf' # Nome do novo arquivo com o timestamp e extensão .pdf   
    caminho_arquivo_local = os.path.join(diretorio_local, novo_nome_arquivo_pdf)  # Caminho completo para o novo arquivo local em PDF
    
    with open(caminho_arquivo_local, 'wb') as novo_arquivo: # Criar a cópia local em PDF
        novo_arquivo.write(conteudo)

    print(f'Arquivo {nome_arquivo} lido e cópia em PDF criada em {caminho_arquivo_local}')

    with open(caminho_arquivo_local, 'rb') as arquivo_pdf:          # Fazer o upload do arquivo em PDF para o bucket de destino
        s3_cliente.upload_fileobj(arquivo_pdf, bucket_destino, novo_nome_arquivo_pdf)

    print(f'Arquivo em PDF {novo_nome_arquivo_pdf} enviado para o bucket {bucket_destino}')
