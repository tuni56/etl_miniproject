# etl_miniproject con python y AWS S3

## 🎯 Objetivo
Crear un pipeline ETL (Extract, Transform, Load) en AWS que:

Extraiga datos desde un archivo CSV en un bucket de S3.
Transforme los datos con Pandas en Python (limpieza, normalización, agregaciones).
Cargue los datos procesados en otro bucket de S3 o en una base de datos como Amazon RDS.

## 🛠 Tecnologías
✅ Python (Pandas, Boto3)
✅ AWS S3 (para almacenamiento de datos)
✅ AWS IAM (gestión de permisos)
✅ Docker (opcional, para ejecutar en un contenedor)
✅ Jupyter Notebook o Script Python (para desarrollo y pruebas)

## 📌 Pasos del Proyecto
### 🔹 1. Configuración de AWS S3 e IAM
Crear un bucket de S3 llamado etl-source-data para almacenar los datos sin procesar.
Crear otro bucket etl-processed-data para los datos transformados.
Crear un usuario IAM con permisos para S3 (s3:PutObject, s3:GetObject, etc.).
Configurar credenciales en ~/.aws/credentials o usar variables de entorno.
### 🔹 2. Subir un Dataset a S3
Descargar un dataset público (por ejemplo, sobre ventas, clima, etc.).
Subirlo manualmente a etl-source-data o usar un script Python con Boto3.
### 🔹 3. Desarrollo del Script ETL con Python
El script debe:

Extraer el archivo CSV desde S3.
Transformar los datos (limpieza, conversión de tipos, agregaciones).
Cargar los datos procesados en otro bucket o en RDS.
### 🔹 4. Automatización con AWS Lambda (Opcional)
Subir el script a AWS Lambda.
Configurar un trigger para ejecutarlo cada vez que se suba un nuevo archivo a S3.
