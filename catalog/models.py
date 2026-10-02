from sqlalchemy import Column, Integer, String
from database import Base

class Catalog(Base):
    __tablename__ = "catalog_db"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    precio = Column(Integer)

