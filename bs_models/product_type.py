from .base_model import *
from .media.image import Image
from .media.video import Video
from __future__ import annotations


product_type_images = Table(
    "product_type_images",
    Base.metadata,
    Column("product_type_id", UUID(as_uuid=True), ForeignKey("product_types.id", ondelete="CASCADE"), primary_key=True),
    Column("image_id", UUID(as_uuid=True), ForeignKey("images.id", ondelete="CASCADE"), primary_key=True),
    Column("position", Integer, nullable=False, default=0),
    UniqueConstraint("product_type_id", "image_id", name="uq_product_type_image_once"),
)

product_type_videos = Table(
    "product_type_videos",
    Base.metadata,
    Column("product_type_id", UUID(as_uuid=True), ForeignKey("product_types.id", ondelete="CASCADE"), primary_key=True),
    Column("video_id", UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"), primary_key=True),
    Column("position", Integer, nullable=False, default=0),
    UniqueConstraint("product_type_id", "video_id", name="uq_product_type_video_once"),
)


class ProductType(Base):
    __tablename__ = "product_types"
    
    id: Mapped[UUIDpk]
    name: Mapped[str] = mapped_column(String(128), nullable=True)
    seller_id: Mapped[UUID] = mapped_column(ForeignKey('sellers.id'), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False)
    cost: Mapped[money]
    sale: Mapped[float] = mapped_column(Float, nullable=True)
    author_id: Mapped[UUID] = mapped_column(ForeignKey('authors.id'), nullable=False)
    date_publication: Mapped[BigInteger] = mapped_column(BigInteger, nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    seller: Mapped["Seller"] = relationship("Seller", back_populates='product_types')
    author: Mapped["Author"] = relationship("Author", back_populates='product_types')
    products: Mapped[list["Product"]] = relationship("Product", back_populates='product_type')
    purchase_items: Mapped[list["PurchaseItem"]] = relationship("PurchaseItem", back_populates='product_type')
    images: Mapped[list[Image]] = relationship(
        "Image", secondary="product_type_images", back_populates="product_types", order_by="product_type_images.c.position"
    )
    videos: Mapped[list[Video]] = relationship(
        "Video", secondary="product_type_videos", back_populates="product_types", order_by="product_type_videos.c.position"
    )

