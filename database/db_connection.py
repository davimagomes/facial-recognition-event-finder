import os

from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from config.logger_config import logger
from config import settings

def conexao_banco():
    
    try:

        safe_password = quote_plus(str(settings.password)) if settings.password is not None else ""

        DATABASE_URL = f"mysql+mysqlconnector://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}"

        logger.info("Tentando inicializar o engine do SQLAlchemy...")

        engine = create_engine(DATABASE_URL)

        with engine.connect() as conexao:
            logger.info("Conexão com o banco de dados estabelecida com sucesso.")

        return engine
    
    except SQLAlchemyError as erro:
        logger.error(f"Falha crítica na conexão com o MySQL: {erro}", exc_info=True)
        return None
    