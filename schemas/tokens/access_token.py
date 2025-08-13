from .base_schema import *


class RequestAccess(BaseModel):
    access_token: str
    token_type: str


class ResponseAccess(BaseModel):
    valid: bool

