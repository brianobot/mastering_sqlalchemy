from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # a typing hint (generic) that tells SQLAlchemy and IDEs that this attribute is mapped to a database column.
    name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)