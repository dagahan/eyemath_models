from ..base_schema import *


# class RecognizeImageRequest(BaseModel):
#     image: Any
# we don't use this because form-data (from fastapi)
# isn't use json fields, which is required by pydantic.


class RecognizeImageResponse(BaseModel):
    latex: str


