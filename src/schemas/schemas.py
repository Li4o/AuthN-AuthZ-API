from pydantic import BaseModel, EmailStr, SecretStr

# ユーザー登録クラスの宣言
class UserCreate(BaseModel):
    email: EmailStr
    password: SecretStr