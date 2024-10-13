import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event=None,context=None):
    # Inicializa el cliente de S3
    s3 = boto3.client('s3')
    bucket = 'data-engineer-diplomadousach-2024' 
    prefijo = 'apihuachitos/huachitos_'
    key = event["Records"][0]["s3"]["object"]["key"]


    if key.startswith(prefijo):
        try:
            response = s3.get_object(Bucket=bucket, Key=key)
            csv_content = response['Body'].read().decode('utf-8') #leemos contenido de s3
            df = pd.read_csv(StringIO(csv_content)) #pasamos contenido a un df
            print('df leido con exito desde s3')

            #Modificamos df
            df['desc_fisica'] = df['desc_fisica'].str.replace('<p>','').str.replace('</p>','')
            df['desc_personalidad'] = df['desc_personalidad'].str.replace('<p>','').str.replace('</p>','')
            df['desc_adicional'] = df['desc_adicional'].str.replace('<p>','').str.replace('</p>','')

        except Exception as e:
            print('Error al leer archivo en bucket s3')
            print(e)

lambda_handler(event=None,context=None)