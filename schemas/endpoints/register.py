from .base_schema import *
from ..user import *


class RegisterRequest:
    data: UserCreateDTO


class RegisterResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

