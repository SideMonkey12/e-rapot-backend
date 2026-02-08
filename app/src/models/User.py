from app.core.database import Base
from enum import Enum
from sqlalchemy import Integer, String, TIMESTAMP, Boolean, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

class RoleUser(Enum):
    ADMIN = 'admin'
    SISWA = 'siswa'
    GURU = 'guru'

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[RoleUser] = mapped_column(Enum(RoleUser), name='user_role', default=RoleUser.SISWA)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now(), onupdate=func.now())