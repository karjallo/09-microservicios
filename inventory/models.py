from sqlalchemy import Column, Integer, String
from database import Base

class Inventory(Base):
    __tablename__ = "inventory_db"
    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer)
