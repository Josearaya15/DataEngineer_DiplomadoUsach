import boto3

s3 = boto3.client('s3')

localpath = 'Carga de archivos a bucket3\Tarea_1_ModuloCloud.docx'
bucket = 'data-engineer-diplomadousach-2024'
nombre_en_s3 = 'Tarea_1_ModuloCloud.docx'

try:
    s3.upload_file(localpath, bucket, nombre_en_s3)

except:
    raise