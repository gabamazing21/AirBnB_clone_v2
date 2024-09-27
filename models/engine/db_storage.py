#!/usr/bin/python3
"""
Module for DBStorage class
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        result = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                result[key] = obj
        else:
            for cls in [State, City, User, Place, Review, Amenity]:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    result[key] = obj
        return result

    def new(self, obj):
        """Adds new object to storage session"""
        self.__session.add(obj)

    def save(self):
        """Commits the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads storage session from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        Session = scoped_session(session_factory)
        Session.remove()
        self.__session = Session()
