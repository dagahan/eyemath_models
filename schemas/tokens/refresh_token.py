from ..base_schema import *


class RequestRefresh(BaseModel):
    refresh_token: str


class ResponseRefresh(BaseModel):
    access_token: str

