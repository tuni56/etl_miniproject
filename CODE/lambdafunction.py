import boto3
import pandas as pd
from io import StringIO

# Configuración de S3
S3_BUCKET_INPUT = "etl-source-data"
S3_BUCKET_OUTPUT = "etl-processed-data"

def lambda_handler(event, context):
    """Función que se ejecuta cuando se sube un archivo a S3"""
    s3_client = boto3.client("s3")

    # Obtener el nombre del archivo subido desde el evento de S3
    file_name = event['Records'][0]['s3']['object']['key']
    print(f"📂 Procesando archivo: {file_name}")

    try:
        # Descargar archivo desde S3
        response = s3_client.get_object(Bucket=S3_BUCKET_INPUT, Key=file_name)
        data = response['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(data))
        print("✅ Archivo cargado correctamente")

        # Transformar datos
        df.dropna(inplace=True)
        df.columns = df.columns.str.lower()
        df["total"] = df["cantidad"] * df["precio"]
        print("✅ Transformación completada")

        # Guardar archivo procesado en S3
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        s3_client.put_object(Bucket=S3_BUCKET_OUTPUT, Key=f"processed_{file_name}", Body=csv_buffer.getvalue())

        print(f"✅ Datos cargados en s3://{S3_BUCKET_OUTPUT}/processed_{file_name}")

    except Exception as e:
        print(f"❌ Error en el proceso ETL: {e}")
