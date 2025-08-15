import datetime
import enum
from typing import Annotated
from uuid import uuid4
import bcrypt
from loguru import logger

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    func,
    TypeDecorator,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

UUIDpk = Annotated[UUID, mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now(), nullable=False)]
updated_at = Annotated[datetime.datetime, mapped_column
                       (
                            server_default=func.now(),
                            onupdate=func.now(),
                            nullable=False
                        )]
money = Annotated[Numeric, mapped_column(Numeric(10, 2), nullable=False)]


class Password(TypeDecorator):
    impl = String(256) # length of the bcrypt hash
    cache_ok = True


    def process_bind_param(self, value: str, dialect) -> str:
        if value:
            return self.hash_password(value)
        return value


    def process_result_value(self, value: str, dialect) -> str:
        return value


class Base(DeclarativeBase):
    # this is base class for all of declaratively using models of tables.
    # e.g. we use this for create or drop all of tables in db.
    pass


class UserRole(str, Enum):
    user = "user"
    admin = "admin"
    seller = "seller"


class PaymentMethodEnum(str, enum.Enum):
    cash = 'cash'
    card = 'card'


class DeliveryStatusEnum(str, enum.Enum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'


class DeliveryGroupStatusEnum(str, enum.Enum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'

    