import os
import logging

from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

import logger_config

logger = logging.getLogger(__name__)
load_dotenv()

def conexao_banco():
    
    try:
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_DATABASE")
        port = int(os.getenv("DB_PORT", 3306))

        safe_password = quote_plus(str(password)) if password is not None else ""

        DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

        logger.debug("Tentando inicializar o engine do SQLAlchemy...")

        engine = create_engine(DATABASE_URL)

        with engine.connect() as conexao:
            logger.info("Conexão com o banco de dados estabelecida com sucesso.")

        return engine
    
    except SQLAlchemyError as erro:
        logger.error(f"Falha crítica na conexão com o MySQL: {erro}", exc_info=True)
        return None
    