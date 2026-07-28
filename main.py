from fastapi import FastAPI

from config.logger import logger
from database.db_connection import get_supabase_connection
from services.cloud_connection import get_bucket_client
from routers import users

app = FastAPI()

app.include_router(
    users.router
)

@app.get("/")
def health_check():
    return {
        "status": "API Online"
    }

# def main():
#     return

# if __name__ == "__main__":
#     main()
