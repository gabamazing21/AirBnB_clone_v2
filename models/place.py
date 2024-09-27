from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

class Place(BaseModel, Base):
    """Place class to represent a place"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    _amenities = relationship("Amenity", secondary="place_amenity", viewonly=False, backref="places")

    @property
    def get_reviews(self):
        from models import storage
        """Returns a list of Review instances with place_id equals to the current Place.id"""
        return [review for review in storage.all(Review).values() if review.place_id == self.id]
    
    @property
    def amenities_list(self):
        """ returns the list of Amenity instances based on 
        the attribute amenity_ids that contains all Amenity.id linked to the Place """
        return self._amenities

    @amenities_list.setter
    def amenities_list(self, obj):
        """ 
        Setter attribute amenities that handles 
        append method for adding an Amenity.id

        """
        if isinstance(obj, Amenity):
            self._amenities.append(obj)




# Define the many-to-many association table
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id', ondelete='CASCADE'), primary_key=True, nullable=False)
)