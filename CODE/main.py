import boto3
import pandas as pd
from io import StringIO

# Configuración de AWS
AWS_REGION = "us-east-1"  # Cambiar si es necesario
S3_BUCKET_INPUT = "etl-source-data"
S3_BUCKET_OUTPUT = "etl-processed-data"
FILE_NAME = "data.csv"

# Inicializar cliente de S3
s3_client = boto3.client("s3", region_name=AWS_REGION)

def extract():
    """Descarga el archivo CSV desde S3 y lo convierte en un DataFrame."""
    response = s3_client.get_object(Bucket=S3_BUCKET_INPUT, Key=FILE_NAME)
    df = pd.read_csv(response['Body'])
    return df

def transform(df):
    """Limpieza y transformación de datos."""
    df.dropna(inplace=True)  # Eliminar filas con valores nulos
    df.columns = df.columns.str.lower().str.replace(" ", "_")  # Normalizar nombres de columnas
    df["total"] = df["cantidad"] * df["precio"]  # Nueva columna total
    return df

def load(df):
    """Guarda el DataFrame transformado en un nuevo archivo CSV en S3."""
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=S3_BUCKET_OUTPUT, Key=f"processed_{FILE_NAME}", Body=csv_buffer.getvalue())
    print("Archivo transformado subido a S3")

def main():
    df = extract()
    df_transformed = transform(df)
    load(df_transformed)

if __name__ == "__main__":
    main()

