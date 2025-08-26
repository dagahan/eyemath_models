from __future__ import annotations
from ..base_model import * 
from .media.media import Media 


class Gif(Media):
    __tablename__ = "gifs"

    id: Mapped[UUID] = mapped_column(
        ForeignKey("media.id", ondelete="CASCADE"), primary_key=True
    )
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    frames: Mapped[int] = mapped_column(Integer, nullable=False)
    duration_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    loop_count: Mapped[int | None] = mapped_column(Integer, nullable=True)  # None = infinite

    __mapper_args__ = {"polymorphic_identity": "gif"}

    