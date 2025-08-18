from ..base_schema import *


class MediaDTO(TimestampMixin):
    id: UUID = Field(...)
    media_type: str = Field(..., min_length=3, max_length=16)
    bucket: str = Field(..., max_length=63)
    key: str = Field(..., max_length=512)
    mime: str = Field(..., max_length=64)
    size: int = Field(..., ge=0)
    checksum_sha256: str = Field(..., min_length=64, max_length=64)

    