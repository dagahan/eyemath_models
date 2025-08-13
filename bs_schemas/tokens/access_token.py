from ..base_schema import *


class RequestAccess(BaseModel):
    access_token: str


class ResponseAccess(BaseModel):
    valid: bool

