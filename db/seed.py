from config.database import Session, engine, Base
from models.models import Vehicle, Destination

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

vehicles = [
    Vehicle(name="Toyota Land Cruiser", price=150, image="landcruiser.jpg", seats=6, type="open-air"),
    Vehicle(name="Toyota Hiace", price=100, image="hiace.jpg", seats=8, type="van")
]

destinations = [
    Destination(name="Maasai Mara", base_price=200, image="maasai-mara.jpg", distance=300),
    Destination(name="Ol Pejeta", base_price=150, image="ol-pejeta.jpg", distance=250)
]

session.add_all(vehicles + destinations)
session.commit()
print("Database seeded successfully!")
