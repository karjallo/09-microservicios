from pydantic import BaseModel

class AuthBase(BaseModel):
    nombre: str

class AuthCreate(AuthBase):
    password: str

class AuthLogin(AuthCreate):
    pass

    class Config:
        from_attributes = True
