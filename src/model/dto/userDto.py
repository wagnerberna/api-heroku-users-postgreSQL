from pydantic import BaseModel, validator, EmailStr
from typing import Optional, List


class UserDtoAdd(BaseModel):
    name: str
    age: Optional[int] = 18
    email: EmailStr
    city: Optional[str] = ""
    login: str
    password: str
    description: Optional[str] = ""
    activated: Optional[bool] = False

    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError("Campo não pode estar vazio")
        return field

    @validator("password")
    def password_lenght(cls, value):
        if len(value) < 6:
            raise ValueError("Senha menor que 6")
        return value

    @validator("age")
    def age_check(cls, value):
        if value < 18:
            raise ValueError("Idade mínima 18")
        return value


class UserDtoUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]
    city: Optional[str]
    description: Optional[str]
    activated: Optional[bool] = False


class UserDtoGetById(BaseModel):
    user_id: int
    name: str
    age: int
    email: EmailStr
    city: str
    login: str
    password: str
    description: str
    activated: bool
