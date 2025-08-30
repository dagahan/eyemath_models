from enum import Enum
from typing import List, Optional, Annotated, Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, SecretStr


UnixTs = Annotated[int, Field(...,
description="Unix time, seconds since 1970-01-01T00:00:00Z, may be negative before 1970")]


class UserRole(str, Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"
    god = "god"


class PaymentMethodDTO(str, Enum):
    cash = 'cash'
    card = 'card'


class BaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class TimestampMixin(BaseDTO):
    created_at: UnixTs
    updated_at: UnixTs
