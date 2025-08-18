from ..base_schema import *


class ImageDTO(MediaDTO):
    media_type: str = Field(default="image")
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    exif_stripped: bool = Field(default=True)
    colorspace: Optional[str] = Field(default=None, max_length=16)


class ImageCreateDTO(BaseDTO):
    bucket: str = Field(..., max_length=63)
    key: str = Field(..., max_length=512)
    mime: str = Field(..., max_length=64)
    size: int = Field(..., ge=0)
    checksum_sha256: str = Field(..., min_length=64, max_length=64)
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    exif_stripped: bool = Field(default=True)
    colorspace: Optional[str] = Field(default=None, max_length=16)


class ImageUpdateDTO(BaseDTO):
    bucket: Optional[str] = Field(default=None, max_length=63)
    key: Optional[str] = Field(default=None, max_length=512)
    mime: Optional[str] = Field(default=None, max_length=64)
    size: Optional[int] = Field(default=None, ge=0)
    checksum_sha256: Optional[str] = Field(default=None, min_length=64, max_length=64)
    width: Optional[int] = Field(default=None, ge=1)
    height: Optional[int] = Field(default=None, ge=1)
    exif_stripped: Optional[bool] = Field(default=None)
    colorspace: Optional[str] = Field(default=None, max_length=16)

    