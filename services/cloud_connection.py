import logging

import boto3
from botocore.exceptions import ClientError, BotoCoreError

import config.logger_config as logger
from config import settings

def conexao_nuvem():

    try:

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
            endpoint_url=settings.ENDPOINT_URL,
        )

        #Teste 1
        foto_teste = "unknown_face.jpg"
        foto_bucket = "kate_bush.jpg"

        logging.info("🔄 Conectando ao Backblaze B2 via API S3...")

        s3_client.upload_file(
        Filename=foto_teste,  
        Bucket=settings.BUCKET_NAME,           
        Key=foto_bucket      
        )

        logging.info("✅ Upload da foto realizado com sucesso!")

        # TESTE 2 - Listar arquivos no bucket

        logging.info(f"\n📂 Listando arquivos dentro de '{settings.BUCKET_NAME}':")
        resposta = s3_client.list_objects_v2(Bucket=settings.BUCKET_NAME)

        if "Contents" in resposta:
            for obj in resposta["Contents"]:
                tamanho_kb = obj['Size'] / 1024
                logging.info(f"   🖼️ {obj['Key']} ({tamanho_kb:.2f} KB)")
        else:
            logging.info("   ⚠️ O bucket está vazio.")

    
    except ClientError as e:
        logger.error(f"\n❌ Erro de permissão ou chave (AWS/S3 Error): {e}", exc_info=True)
        return None
    
    except BotoCoreError as e:
        logger.error(f"\n❌ Erro de conexão/rede: {e}", exc_info=True)
        return None
    
    except Exception as e:
        logger.error(f"\n❌ Erro inesperado: {e}", exc_info=True)
        return None