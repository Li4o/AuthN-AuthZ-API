from pydantic import Basemodel, EmailStr, SecretStr

class UserCreate(Basemodel):
    email: EmailStr
    password: SecretStr