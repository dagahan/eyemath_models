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


class ProductTypeCategory(str, Enum):
    FICTION = "fiction"
    NONFICTION = "nonfiction"
    BUSINESS = "business_economics"
    SCIENCE = "science_technology"
    SELF_HELP = "self_help"
    PSYCHOLOGY = "psychology"
    HISTORY = "history"
    BIOGRAPHY = "biography_memoir"
    CHILDREN = "children"
    YOUNG_ADULT = "young_adult"
    FANTASY = "fantasy"
    SCIENCE_FICTION = "science_fiction"
    MYSTERY_THRILLER = "mystery_thriller"
    ROMANCE = "romance"
    COMICS_MANGA = "comics_manga"
    ART_PHOTOGRAPHY = "art_photography"
    COOKBOOKS_FOOD = "cookbooks_food"
    HEALTH_FITNESS = "health_fitness"
    EDUCATION_TEACHING = "education_teaching"
    TRAVEL = "travel"


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
