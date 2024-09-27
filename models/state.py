from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """State class to represent a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Define relationship with City
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
