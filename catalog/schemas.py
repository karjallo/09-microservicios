from pydantic import BaseModel

class CatalogBase(BaseModel):
    nombre: str
    precio: int

class CatalogCreate(CatalogBase):
    pass

class CatalogUpdate(BaseModel):
    nombre: str | None = None
    precio: int | None = None

class CatalogReplace(CatalogBase):
    pass

class CatalogResponse(CatalogCreate):
    id: int

    class Config:
        from_attributes = True
