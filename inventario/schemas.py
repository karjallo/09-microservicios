from pydantic import BaseModel

class InventarioBase(BaseModel):
    nombre: str
    precio: int

class InventarioCreate(InventarioBase):
    pass

class InventarioUpdate(BaseModel):
    nombre: str | None = None
    precio: str | None = None

class InventarioReplace(InventarioBase):
    pass

class InventarioResponse(InventarioCreate):
    id: int

    class Config:
        from_attributes = True
