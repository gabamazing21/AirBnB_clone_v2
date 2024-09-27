#!/usr/bin/python3
"""
State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """Getter method for cities if storage engine is not DBStorage"""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            from models import storage
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        else:
            cities = relationship("City", backref="state", cascade="all, delete-orphan")