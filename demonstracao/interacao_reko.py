from dotenv import load_dotenv

# Importar o SDK da AWS para Python
import os

import boto3

load_dotenv()

# Fazendo com que o script
session = boto3.Session(profile_name=os.getenv("SESSION_PROFILE_NAME"))

# Criando um cliente com o serviço do Rekognition numa região
client = session.client('rekognition', region_name=os.getenv("REGION_NAME"))

response = client.detect.labels(
    Image= {
        "Image": {
            "S3Object": {
                "Bucket": os.getenv("S3_BUCKET"),
                "Name": os.getenv("S3_BUCKET_NAME")
            }
        }
    },
    MaxLabels=10,
    # MinConfidence=80
)

# Exibir o resultado da detecção
for label in response["Labels"]:
    print(f"Objeto: {label['Name']}, Confiança: {label['Confidence:.2f']}")
