from typing import Optional

from supabase import Client, create_client

from config import (
    logger,
    SUPABASE_URL,
    SUPABASE_KEY,
)

_supabase_client: Optional[Client] = None

def get_supabase_connection() -> Optional[Client]:

    global _supabase_client
    
    try:
        if _supabase_client is None:
            _supabase_client = create_client(
                SUPABASE_URL,
                SUPABASE_KEY
                )
            logger.info("Connection created successfully")

        return _supabase_client

    except Exception as error:
        logger.error(f"Failed to connect to database {error}", exc_info=True)

        return None