from sqlalchemy import Column, String, Integer, UUID, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from ..database.db import get_base

Base = get_base()

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(UUID, index=True, primary_key=True, default=lambda: uuid4())
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip = Column(Integer, index=True)
    user_id = Column(UUID, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="addresses")