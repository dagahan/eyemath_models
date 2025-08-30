from ..base_schema import *


class NormalizeLatexRequest(BaseModel):
    expression: str


class NormalizeLatexResponse(BaseModel):
    normalized: str


