from typing import Optional

import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from config.logger import logger
from config import settings

_bucket_client: Optional[BaseClient] = None

def get_bucket_client():

    global _bucket_client

    try:

        if _bucket_client is None:
            _bucket_client = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY,
                aws_secret_access_key=settings.AWS_SECRET_KEY,
                endpoint_url=settings.ENDPOINT_URL,
            )

            logger.info("Connection created successfully")

        return _bucket_client

        
    
    except ClientError as error:
        logger.error(f"Cloud API failure: {error}", exc_info=True)
        return None
    
    except Exception as error:
        logger.error(f"Cloud connection failed: {error}", exc_info=True)
        return None