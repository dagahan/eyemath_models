from __future__ import annotations
from .base_model import * 
from .media.media import Media 


class Image(Media):
    __tablename__ = "images"

    id: Mapped[UUIDMediapk]
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    exif_stripped: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    colorspace: Mapped[str | None] = mapped_column(String(16), nullable=True)

    product_types: Mapped[list["ProductType"]] = relationship(
        "ProductType", secondary="product_type_images", back_populates="images"
    )

    __mapper_args__ = {"polymorphic_identity": "image"}

    