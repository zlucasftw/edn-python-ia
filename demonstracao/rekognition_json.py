from dotenv import load_dotenv
import os

import boto3
import json


load_dotenv()

# Início da sessão com perfil específico
session = boto3.Session(profile_name=os.getenv("SESSION_PROFILE_NAME"))
rekognition = session.client('rekognition', os.getenv("REGION_NAME"))
s3 = session.client('s3', region_name=os.getenv("REGION_NAME"))

# Definição de parâmetros
bucket = os.getenv("S3_BUCKET")
imagem = "s3-service.png"
resultado_json = "resultado-imagem.json"

# Detectar os rótulos (labels) da imagem
response = rekognition.detect.labels(
    Image= {
        "Image": {
            "S3Object": {
                "Bucket": bucket,
                "Name": imagem
            }
        }
    },
    MaxLabels=10,
    MinConfidence=80
)

# Extraindo os rótulos
labels = response["Labels"]

# Salvando o resultado em um json no bucket
s3.put_object(
    Bucket=bucket,
    Key=resultado_json,
    Body=json.dumps(labels, indent=2),
    ContentType='application/json'
)

print(f"O resultado foi salvo com sucesso no bucket {bucket} como {resultado_json}")
