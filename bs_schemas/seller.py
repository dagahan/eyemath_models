from .base_model import *


class SellerDTO(TimestampMixin):
    id: UUID = Field(...)
    name: str = Field(..., min_length=1, max_length=128)
    user_id: UUID = Field(...)
    avatar_image_id: Optional[UUID] = Field(default=None)


class SellerCreateDTO(BaseDTO):
    name: str = Field(..., min_length=1, max_length=128)
    user_id: UUID = Field(...)


class SellerUpdateDTO(BaseDTO):
    name: Optional[str] = Field(default=None, min_length=1, max_length=128)
    avatar_image_id: Optional[UUID] = Field(default=None)

