from config.database import Session, engine, Base
from models.model import Vehicle, Destination, Booking

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = Session()

vehicle1 = Vehicle(name="Toyota Land Cruiser", price=150, image="landcruiser.jpg", seats=6, type="open-air")