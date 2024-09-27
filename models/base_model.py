#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()



class BaseModel:
    """A base class for all hbnb models"""
    # Common attributes for all models using SQLAlchemy
    id = Column(String(60), primary_key=True, nullable=False, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance, excluding _sa_instance_state"""
        obj_dict = self.__dict__.copy()

        # Remove the SQLAlchemy internal attribute if it exists
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']

        # Format dates to ISO format
        if 'created_at' in obj_dict:
            obj_dict['created_at'] = self.created_at.isoformat()
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = self.updated_at.isoformat()

        # Add the class name to the dictionary
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict
    
    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
