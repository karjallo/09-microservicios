from pydantic import BaseModel

class OrderBase(BaseModel):
    nombre: str
    precio: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    nombre: str | None = None
    precio: str | None = None

class OrderReplace(OrderBase):
    pass

class OrderResponse(OrderCreate):
    id: int

    class Config:
        from_attributes = True
