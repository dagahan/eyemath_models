from .base_schema import *


class AccessPayload(BaseModel):
    sub: str  # user_id
    sid: str  # session_id
    exp: int  # expiry timestamp


class RefreshPayload(BaseModel):
    sub: str
    sid: str
    exp: int
    ref: bool # refresh token 
