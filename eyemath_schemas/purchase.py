from .base_schema import *


class PurchaseDTO(TimestampMixin):
    id: UUID = Field(...)
    timestamp: UnixTs = Field(...)
    payment_method: PaymentMethodDTO = Field(...)
    delivery_group_id: UUID = Field(...)
    buyer_id: UUID = Field(...)
    seller_id: UUID = Field(...)


class PurchaseCreateDTO(BaseDTO):
    timestamp: UnixTs = Field(...)
    payment_method: PaymentMethodDTO = Field(...)
    delivery_group_id: UUID = Field(...)
    buyer_id: UUID = Field(...)
    seller_id: UUID = Field(...)


class PurchaseUpdateDTO(BaseDTO):
    timestamp: Optional[UnixTs] = Field(...)
    payment_method: Optional[PaymentMethodDTO] = Field(default=None)
    delivery_group_id: Optional[UUID] = Field(default=None)
    buyer_id: Optional[UUID] = Field(default=None)
    seller_id: Optional[UUID] = Field(default=None)
