from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Auth(Base):
    __tablename__ = "auth_db"
    id       : Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre   : Mapped[str] = mapped_column(unique=True, index=True)
    password : Mapped[str] = mapped_column()
