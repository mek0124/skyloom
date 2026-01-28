from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from ..database.db import get_base

Base = get_base()

class Settings(Base):
    __tablename__ = 'settings'
    
    id = Column(UUID, index=True, primary_key=True, default=lambda: uuid4())
    f_c = Column(String, index=True, default="f")
    mph_kph = Column(String, index=True, default="mph")
    km_mi = Column(String, index=True, default="mi")
    mb_in = Column(String, index=True, default="in")
    user_id = Column(UUID, ForeignKey('users.id'), unique=True)
    
    user = relationship("User", back_populates="settings")