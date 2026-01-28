from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4
from ..database.db import get_base


Base = get_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID,
        index = True,
        primary_key = True,
        default = lambda: uuid4()
    )

    username = Column(
        String,
        unique = True,
        index = True
    )

    created_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now()
    )

    updated_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now(),
        onupdate = lambda: datetime.now()
    )

    addresses = relationship("Address", back_populates="user")
    settings = relationship("Settings", back_populates="user", uselist=False)