from ..base_schema import *
from typing import Optional
from pydantic import field_validator, model_validator


class LoginRequest(BaseModel):
    # Login can be proceed by phone, user_name or email. Frond-end need to define what kind of login method we using here.
    phone: Optional[str] = None
    user_name: Optional[str] = None
    email: Optional[str] = None
    password: SecretStr
    dsh: str
    
    @field_validator('phone', 'user_name', 'email', mode='before')
    @classmethod
    def validate_login_fields(cls, v):
        if v == "" or v is None:
            return None
        return v
    
    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, v):
        if not v or v == "":
            raise ValueError('Password is required')
        return v
    
    @field_validator('dsh', mode='before')
    @classmethod
    def validate_dsh(cls, v):
        if not v or v == "":
            raise ValueError('DSH is required')
        return v
    
    @model_validator(mode='after')
    def validate_at_least_one_login_field(self):
        if not any([self.phone, self.user_name, self.email]):
            raise ValueError('At least one login field (phone, user_name, or email) must be provided')
        return self


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str

