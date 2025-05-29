from config.database import Session
from models.model import Vehicle, Destination, Booking

def list_vehicles():
    session = Session()
    vehicles = session.query(Vehicle).all()
    print("\n🚗 Available Vehicles:")
    for v in vehicles:
        print(f"- {v.name} | Type: {v.type} | Seats: {v.seats} | Price: ${v.price}")
    session.close()

def list_destinations():
    session = Session()
    destinations = session.query(Destination).all()
    print("\n🌍 Available Destinations:")
    for d in destinations:
        print(f"- {d.name} | Distance: {d.distance}km | Base Price: ${d.base_price}")
    session.close()

def main():
    print("🦁 Welcome to the Safari Booking CLI App!")
    while True:
        print("\nChoose an option:")
        print("1. View Vehicles")
        print("2. View Destinations")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            list_vehicles()
        elif choice == '2':
            list_destinations()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
