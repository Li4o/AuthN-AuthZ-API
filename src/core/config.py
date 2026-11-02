from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    PROJECT_NAME: str = "AuthN-AuthZ-API"
    DATABASE_URL: SecretStr
    SECRET_KET: SecretStr

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }