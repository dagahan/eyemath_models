from ..base_schema import *


class BanRequest(BaseModel):
    ban_user_id: str


class BanResponse(BaseModel):
    succsess: bool

