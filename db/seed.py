from config.database import Session, engine, Base
from models.model import Vehicle, Destination, Booking

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("📦 Tables created successfully.")

session = Session()

vehicle1 = Vehicle(name="Toyota Land Cruiser", price=150, image="landcruiser.jpg", seats=6, type="open-air")
vehicle2 = Vehicle(name="Toyota Hiace", price=100, image="hiace.jpg", seats=8, type="van")

destination1 = Destination(name="Maasai Mara", base_price=200, image="maasai-mara.jpg", distance=300)
destination2 = Destination(name="Ol Pejeta", base_price=150, image="ol-pejeta.jpg", distance=250)

session.add_all([vehicle1, vehicle2, destination1, destination2])
session.commit()

print("✅ Vehicles and destinations inserted into the database.")

session.close()
