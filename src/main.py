from fastapi import FastAPI
from src.core.config import Settings
from src.models.models import User

# 設定クラスのインスタンスを作成
settings = Settings()

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    return {
        "massege": "Welcome to AuthN-AuthZ-API!",
        "project_name": settings.PROJECT_NAME,
        "database_url": settings.DATABASE_URL.get_secret_value(),
    }