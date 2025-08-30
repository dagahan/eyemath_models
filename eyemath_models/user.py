from __future__ import annotations
from .base_model import *
from .media.image import Image


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[UUIDpk]
    user_name: Mapped[str] = mapped_column(String(32), nullable=False) 
    hashed_password: Mapped[str] = mapped_column(Password, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(32), nullable=False)
    last_name: Mapped[str] = mapped_column(String(32), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[str] = mapped_column(String(64), nullable=True)
    phone: Mapped[str] = mapped_column(String(16), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole.user, UserRole.moderator, UserRole.admin, UserRole.god, name="role"),
        default=UserRole.user,
        nullable=False,
    )
    profile_image_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("images.id", ondelete="SET NULL"), nullable=True
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    profile_image: Mapped[Image | None] = relationship("Image")

    def verify_password(self, plain_password: str) -> bool:
        try:
            return bcrypt.checkpw(
                plain_password.encode('utf-8'),
                self.hashed_password.encode('utf-8')
            )
        except Exception as e:
            logger.error(f"Password verification error: {e}")
            return False