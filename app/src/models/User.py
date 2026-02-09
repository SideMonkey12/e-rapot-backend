import enum
from app.db.db import Base
from sqlalchemy import Integer, String, TIMESTAMP, Boolean, func, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

class RoleUser(enum.Enum):
    ADMIN = 'admin'
    SISWA = 'siswa'
    GURU = 'guru'

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Enum] = mapped_column(Enum(RoleUser), name='role', default=RoleUser.SISWA)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now(), onupdate=func.now())