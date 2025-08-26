from ..base_schema import *


# class UploadAvatarRequest(BaseModel):
#     avatar: Any
# we don't use this because form-data (from fastapi)
# isn't use json fields, which is required by pydantic.


class UploadAvatarResponse(BaseModel):
    succsess: bool

