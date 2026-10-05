from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    id_producto : str
    cantidad    : int
    precio      : int
    total       : int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    id          : int
    id_producto : int | None = None
    cantidad    : int | None = None
    precio      : int | None = None
    total       : int | None = None

class OrderReplace(OrderBase):
    pass

class OrderResponse(OrderBase):
    id          : int
    created_at  : datetime

    class Config:
        from_attributes = True
