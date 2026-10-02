from pydantic import BaseModel

class InventoryBase(BaseModel):
    nombre: str
    precio: int

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    nombre: str | None = None
    precio: str | None = None

class InventoryReplace(InventoryBase):
    pass

class InventoryResponse(InventoryCreate):
    id: int

    class Config:
        from_attributes = True
