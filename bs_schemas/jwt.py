from .base_schema import *


class AccessPayload(BaseModel):
    sub: int  # user_id
    sid: str  # session_id
    exp: int  # expiry timestamp


class RefreshPayload(BaseModel):
    sub: int
    sid: str
    exp: int
    ref: bool # refresh token 
