from pydantic import BaseModel
from typing import Optional, List


class LoginDto(BaseModel):
    login: str
    password: str
