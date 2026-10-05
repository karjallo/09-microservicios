from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Inventory(Base):
    __tablename__ = "inventory_db"
    id       : Mapped[int] = mapped_column(primary_key=True, index=True)
    cantidad : Mapped[int] = mapped_column()
