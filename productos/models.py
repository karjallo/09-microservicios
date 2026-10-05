from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Productos(Base):
    __tablename__ = "catalog_db"
    id          : Mapped[int]  = mapped_column(primary_key=True, index=True)
    producto_id : Mapped[int]  = mapped_column(index=True)
    cantidad    : Mapped[int]  = mapped_column()
    confirmado  : Mapped[bool] = mapped_column()
