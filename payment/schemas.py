from pydantic import BaseModel

class DummySchema(BaseModel):
    nombre: str

    class Config:
        from_attributes = True