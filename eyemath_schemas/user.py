from .base_schema import *


class UserDTO(TimestampMixin):
    id: UUID = Field(...)
    user_name: str = Field(..., min_length=5, max_length=32)
    hashed_password: SecretStr = Field(...)
    is_active: bool = Field(default=True)
    first_name: str = Field(..., min_length=3, max_length=32)
    last_name: str = Field(..., min_length=3, max_length=32)
    middle_name: str = Field(..., min_length=3, max_length=32)
    email: Optional[str] = Field(default=None, max_length=64)
    phone: str = Field(..., min_length=11, max_length=16)
    role: UserRole = Field(...)
    profile_image_id: Optional[UUID] = Field(default=None)

    @field_validator('first_name', 'last_name', 'middle_name', mode='before')
    def capitalize_name(cls, v: str) -> str:
        return v.strip().capitalize()


class UserCreateDTO(BaseDTO):
    user_name: str = Field(..., min_length=5, max_length=32)
    password: SecretStr = Field(..., min_length=8, max_length=32)
    dsh: str = Field(...)
    first_name: str = Field(..., min_length=3, max_length=32)
    last_name: str = Field(..., min_length=3, max_length=32)
    middle_name: str = Field(..., min_length=3, max_length=32)
    email: Optional[str] = Field(default=None, max_length=64)
    phone: str = Field(..., min_length=11, max_length=16)
    role: UserRole = Field(default=UserRole.user)

    @field_validator('first_name', 'last_name', 'middle_name', mode='before')
    def capitalize_name(cls, v: str) -> str:
        return v.strip().capitalize()


class UserUpdateDTO(BaseDTO):
    user_name: str = Field(default=None, min_length=5, max_length=32)
    password: SecretStr = Field(default=None, min_length=8, max_length=32)
    is_active: bool = Field(default=None)
    first_name: str = Field(default=None, min_length=3, max_length=32)
    last_name: str = Field(default=None, min_length=3, max_length=32)
    middle_name: str = Field(default=None, min_length=3, max_length=32)
    email: str = Field(default=None, max_length=64)
    phone: str = Field(default=None, min_length=11, max_length=16)
    role: UserRole = Field(default=None)
    profile_image_id: Optional[UUID] = Field(default=None)

    @field_validator('first_name', 'last_name', 'middle_name', mode='before')
    def capitalize_name(cls, v: str) -> str:
        return v.strip().capitalize()
    