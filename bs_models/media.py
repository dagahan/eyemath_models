from .base_model import *


class Media(Base):
    __tablename__ = "media"

    id: Mapped[UUIDpk]
    media_type: Mapped[str] = mapped_column(String(16), nullable=False)   # 'image' | 'video' | 'gif'
    bucket: Mapped[str] = mapped_column(String(63), nullable=False)
    key: Mapped[str] = mapped_column(String(512), unique=True, nullable=False)
    mime: Mapped[str] = mapped_column(String(64), nullable=False)
    size: Mapped[int] = mapped_column(Integer, nullable=False)            # байты
    checksum_sha256: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    __mapper_args__ = {
        "polymorphic_on": media_type,
        "polymorphic_identity": "media",
    }

