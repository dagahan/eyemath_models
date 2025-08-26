from .base_schema import *


class AccessPayload(BaseModel):
    sub: str  # user_id
    sid: str  # session_id
    exp: int  # expiry timestamp


class RefreshPayload(BaseModel):
    sub: str
    sid: str
    exp: int
    dsh: str  # device info hash (user_agent + client_id + local_system_time_zone + platform)
    ish: str  # hashed ip (for soft identity)