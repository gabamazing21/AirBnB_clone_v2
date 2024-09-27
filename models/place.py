from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review

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

    @property
    def get_reviews(self):
        """Returns a list of Review instances with place_id equals to the current Place.id"""
        from models import storage
        return [review for review in storage.all(Review).values() if review.place_id == self.id]