from typing import Annotated
from uuid import uuid4
import bcrypt
from loguru import logger

from sqlalchemy import (
    TIMESTAMP, # Unix time, seconds since 1970-01-01T00:00:00Z, may be negative before 1970
    BigInteger,
    Boolean,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    func,
    TypeDecorator,
    text,
    Table,
    Column,
    UniqueConstraint,
)

from enum import Enum as PyEnum

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


UUIDpk = Annotated[UUID,
        mapped_column(UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )]

UUIDMediapk = Annotated[UUID, mapped_column(
        UUID(as_uuid=True),
        ForeignKey("media.id", ondelete="CASCADE"),
        primary_key=True,
        default=uuid4
    )]
    
created_at = Annotated[int, mapped_column(
    BigInteger,
    server_default=text("(EXTRACT(EPOCH FROM NOW()))::bigint"),
    nullable=False)
]

updated_at = Annotated[int, mapped_column(
    BigInteger,
    server_default=text("(EXTRACT(EPOCH FROM NOW()))::bigint"),
    onupdate=text("(EXTRACT(EPOCH FROM NOW()))::bigint"),
    nullable=False)
]

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

    
    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


class Base(DeclarativeBase):
    # this is base class for all of declaratively using models of tables.
    # e.g. we use this for create or drop all of tables in db.
    pass


class UserRole(str, PyEnum):
    user = "user"
    moderator = "moderator"
    admin = "admin"
    god = "god"


class PaymentMethodEnum(str, PyEnum):
    cash = 'cash'
    card = 'card'


class DeliveryStatusEnum(str, PyEnum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'


class DeliveryGroupStatusEnum(str, PyEnum):
    on_delivery = 'on_delivery'
    wait_for_delivery = 'wait_for_delivery'
    done = 'done'
    failed = 'failed'

    