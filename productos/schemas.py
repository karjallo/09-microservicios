from pydantic import BaseModel

class ProductosBase(BaseModel):
    nombre: str
    precio: int

class ProductosCreate(ProductosBase):
    pass

class ProductosUpdate(BaseModel):
    nombre: str | None = None
    precio: int | None = None

class ProductosReplace(ProductosBase):
    pass

class ProductosResponse(ProductosCreate):
    id: int

    class Config:
        from_attributes = True
