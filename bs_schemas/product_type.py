from .base_schema import *


class ProductTypeDTO(TimestampMixin):
    id: UUID = Field(...)
    name: str = Field(..., min_length=3, max_length=128)
    available: bool = Field(default=True)
    cost: float = Field(..., ge=0)
    sale: Optional[float] = Field(default=None, ge=0, le=1)
    date_publication: UnixTs = Field(...)
    seller_id: UUID = Field(...)
    author_id: UUID = Field(...)
    image_ids: List[UUID] = Field(default_factory=list)
    video_ids: List[UUID] = Field(default_factory=list)
    
    @field_validator('cost', mode='before')
    def convert_decimal(cls, v):
        return float(v)


class ProductTypeCreateDTO(BaseDTO):
    name: str = Field(..., min_length=3, max_length=128)
    available: bool = Field(default=True)
    cost: float = Field(..., ge=0)
    sale: Optional[float] = Field(default=None, ge=0, le=1)
    date_publication: UnixTs = Field(...)
    seller_id: UUID = Field(...)
    author_id: UUID = Field(...)
    image_ids: List[UUID] = Field(default_factory=list)
    video_ids: List[UUID] = Field(default_factory=list)
    
    @field_validator('cost', mode='before')
    def convert_decimal(cls, v):
        return float(v)


class ProductTypeUpdateDTO(BaseDTO):
    name: Optional[str] = Field(default=None, min_length=3, max_length=128)
    available: Optional[bool] = Field(default=None)
    cost: Optional[float] = Field(default=None, ge=0)
    sale: Optional[float] = Field(default=None, ge=0, le=1)
    date_publication: Optional[UnixTs] = Field(default=None)
    seller_id: Optional[UUID] = Field(default=None)
    author_id: Optional[UUID] = Field(default=None)
    image_ids: Optional[List[UUID]] = Field(default=None)
    video_ids: Optional[List[UUID]] = Field(default=None)
    
    @field_validator('cost', mode='before')
    def convert_decimal(cls, v):
        if v is not None:
            return float(v)
        return v
