from config.database import Session
from models.model import Vehicle, Destination, Booking

def main():
    session = Session()
    print("\nWelcome to SafariExpress CLI Booking\n")

    while True:
        print("\nOptions:")
        print("1. View Vehicles")
        print("2. View Destinations")
        print("3. Make Booking")
        print("4. View All Bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vehicles = session.query(Vehicle).all()
            for v in vehicles:
                print(f"{v.id}. {v.name} - ${v.price} - Seats: {v.seats} - Type: {v.type}")

        elif choice == "2":
            destinations = session.query(Destination).all()
            for d in destinations:
                print(f"{d.id}. {d.name} - ${d.base_price} - Distance: {d.distance}km")

        elif choice == "3":
            name = input("Enter your name: ")
            vehicle_id = int(input("Enter vehicle ID: "))
            destination_id = int(input("Enter destination ID: "))

            booking = Booking(customer_name=name, vehicle_id=vehicle_id, destination_id=destination_id)
            session.add(booking)
            session.commit()
            print("Booking successful!")

        elif choice == "4":
            bookings = session.query(Booking).all()
            for b in bookings:
                print(f"{b.customer_name} booked {b.vehicle.name} to {b.destination.name}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
