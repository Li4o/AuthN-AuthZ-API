from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AuthN-AuthZ-API"
    DATABASE_URL: SecretStr
    SECRET_KEY: SecretStr

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }