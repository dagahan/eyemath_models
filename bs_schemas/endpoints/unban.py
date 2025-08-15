from ..base_schema import *


class UnbanRequest(BaseModel):
    ban_user_id: str


class UnbanResponse(BaseModel):
    succsess: bool

