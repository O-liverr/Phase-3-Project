from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    seats = Column(Integer)
    type = Column(String)

    bookings = relationship("Booking", back_populates="vehicle")

class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_price = Column(Float)
    image = Column(String)
    distance = Column(Integer)

    bookings = relationship("Booking", back_populates="destination")

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    vehicle = relationship("Vehicle", back_populates="bookings")
    destination = relationship("Destination", back_populates="bookings")