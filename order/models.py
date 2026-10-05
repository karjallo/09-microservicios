from sqlalchemy import TIMESTAMP, func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Order(Base):
    __tablename__ = "inventory_db"
    id              : Mapped[int] = mapped_column(primary_key=True, index=True)
    id_producto     : Mapped[int] = mapped_column()
    cantidad        : Mapped[int] = mapped_column()
    precio_unitario : Mapped[int] = mapped_column()
    total           : Mapped[int] = mapped_column()
    created_at      : Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
