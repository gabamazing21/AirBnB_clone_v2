#!/usr/bin/python3
"""DBStorage class for AirBnB clone"""
from models.city import City
from models.state import State
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """Database storage engine for MySQL"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine and session"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name (cls).
        If cls=None, query all types of objects."""
        if cls:
            return {f"{cls.__name__}.{obj.id}": obj for obj in self.__session.query(cls).all()}
        else:
            obj_dict = {}
            for model in [State, City]:  # Add other models as needed
                obj_dict.update({f"{model.__name__}.{obj.id}": obj for obj in self.__session.query(model).all()})
            return obj_dict


    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables in the database"""
        # Ensure all models are imported before creating tables
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
