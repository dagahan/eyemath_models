from ..base_schema import *


class LoginRequest(BaseModel):
    # Login can be proceed by phone, user_name or email. Frond-end need to define what kind of login method we using here.
    phone: Optional[str]
    user_name: Optional[str]
    email: Optional[str]
    password: SecretStr


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str

