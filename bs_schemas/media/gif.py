from ..base_schema import *
from .media import MediaDTO


class GifDTO(MediaDTO):
    media_type: str = Field(default="gif")
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    frames: int = Field(..., ge=1)
    duration_ms: int = Field(..., ge=0)
    loop_count: Optional[int] = Field(default=None, ge=0)  # None = infinite


class GifCreateDTO(BaseDTO):
    bucket: str = Field(..., max_length=63)
    key: str = Field(..., max_length=512)
    mime: str = Field(..., max_length=64)
    size: int = Field(..., ge=0)
    checksum_sha256: str = Field(..., min_length=64, max_length=64)
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    frames: int = Field(..., ge=1)
    duration_ms: int = Field(..., ge=0)
    loop_count: Optional[int] = Field(default=None, ge=0)


class GifUpdateDTO(BaseDTO):
    bucket: Optional[str] = Field(default=None, max_length=63)
    key: Optional[str] = Field(default=None, max_length=512)
    mime: Optional[str] = Field(default=None, max_length=64)
    size: Optional[int] = Field(default=None, ge=0)
    checksum_sha256: Optional[str] = Field(default=None, min_length=64, max_length=64)
    width: Optional[int] = Field(default=None, ge=1)
    height: Optional[int] = Field(default=None, ge=1)
    frames: Optional[int] = Field(default=None, ge=1)
    duration_ms: Optional[int] = Field(default=None, ge=0)
    loop_count: Optional[int] = Field(default=None, ge=0)

