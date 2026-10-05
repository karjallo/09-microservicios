from pydantic import BaseModel
from datetime import datetime

class PedidosBase(BaseModel):
    id_producto : str
    cantidad    : int
    precio      : int
    total       : int

class PedidosCreate(PedidosBase):
    pass

class PedidosUpdate(BaseModel):
    id          : int
    id_producto : int | None = None
    cantidad    : int | None = None
    precio      : int | None = None
    total       : int | None = None

class PedidosReplace(PedidosBase):
    pass

class PedidosResponse(PedidosBase):
    id          : int
    created_at  : datetime

    class Config:
        from_attributes = True
