import numpy as np
from sqlalchemy import text

from database.db_connection import conexao_banco
from tests.facial_detector_test import face_scan
from services.cloud_connection import conexao_nuvem
from config.logger_config import logger

def main():
    logger.info("Iniciando a aplicação de Reconhecimento Facial...")

    engine = conexao_banco()

    if engine is not None:
        try:
            with engine.connect() as conexao:
                logger.info("Conexão aberta pelo Engine. Executando teste...")
                resultado = conexao.execute(text("SELECT 1"))
                logger.info(f"Resultado do teste de banco: {resultado.scalar()}")
            
            logger.info("Pronto para iniciar o processamento de imagens/vídeo.")
            
        except Exception as e:
            logger.error(f"Erro ao executar comandos no banco de dados: {e}")
    else:
        logger.critical("Não foi possível conectar ao banco. Encerrando aplicação.")

    face_scan()

    conexao_nuvem()


if __name__ == "__main__":
    main()
