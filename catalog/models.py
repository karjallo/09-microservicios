from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Catalog(Base):
    __tablename__ = "catalog_db"
    id     : Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre : Mapped[str] = mapped_column(unique=True, index=True)
    precio : Mapped[int] = mapped_column()

