from __future__ import annotations
from ..base_model import * 
from .media import Media 


class Video(Media):
    __tablename__ = "videos"

    id: Mapped[UUIDMediapk]
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    duration_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    fps: Mapped[float | None] = mapped_column(Float, nullable=True)
    bitrate: Mapped[int | None] = mapped_column(Integer, nullable=True)
    codec_video: Mapped[str | None] = mapped_column(String(32), nullable=True)
    codec_audio: Mapped[str | None] = mapped_column(String(32), nullable=True)

    __mapper_args__ = {"polymorphic_identity": "video"}

    