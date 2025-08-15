from .base_schema import *


class Session(BaseModel):  # Session:{hashed_session_uuid} {expire_time}
    sub: str  # user_id
    iat: int  # issued_at
    mtl: int  # max_time_to_live (timestamp)
    dsh: str  # device info hash (user_agent + client_id + local_system_time_zone + platform)
    ish: str  # hashed_ip (for soft identity)
