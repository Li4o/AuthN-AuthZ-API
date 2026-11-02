from pydantic import SecretStr
from pydantic_settings import BaseSettings

# 設定クラスの宣言
class Settings(BaseSettings):
    PROJECT_NAME: str = "AuthN-AuthZ-API"
    DATABASE_URL: SecretStr
    SECRET_KEY: SecretStr

    # 環境設定ファイルの設定
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }