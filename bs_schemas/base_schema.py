from enum import Enum
from typing import List, Optional
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


class DeliveryStatusDTO(str, Enum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'


class DeliveryGroupStatusDTO(str, Enum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'


class BaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class TimestampMixin(BaseDTO):
    created_at: UnixTs
    updated_at: UnixTs
