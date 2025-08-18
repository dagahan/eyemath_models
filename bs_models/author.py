from __future__ import annotations
from .base_model import *
from .media import Image


class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[UUIDpk]
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    avatar_image_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("images.id", ondelete="SET NULL"), nullable=True
    )
    
    product_types: Mapped[list["ProductType"]] = relationship("ProductType", back_populates='author')
    avatar_image: Mapped[Image | None] = relationship("Image")

    