from sqlalchemy import Column, Integer, String
from database import Base

class DummyModel(Base):
    __tablename__ = "dummy_table"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)