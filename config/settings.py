import os

import dotenv
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
port = int(os.getenv("DB_PORT", 3306))

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
