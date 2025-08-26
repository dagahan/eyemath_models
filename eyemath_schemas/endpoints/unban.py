from ..base_schema import *


class UnbanRequest(BaseModel):
    unban_user_id: str


class UnbanResponse(BaseModel):
    succsess: bool

