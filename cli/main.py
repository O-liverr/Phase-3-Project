from config.database import Session
from models.model import Vehicle, Destination, Booking

session = Session()

def list_vehicles():
    print("\nAvailable Safari Vehicles:")
    for vehicle in session.query(Vehicle).all():
        print(f"[{vehicle.id}] {vehicle.name} - Ksh {vehicle.price}, Seats: {vehicle.seats}, Type: {vehicle.type}")

def list_destinations():
    print("\nPopular Safari Destinations:")
    for dest in session.query(Destination).all():
        print(f"[{dest.id}] {dest.name} - Ksh {dest.base_price}, Distance: {dest.distance} km")

def make_booking():
    name = input("\nEnter your full name: ")
    list_vehicles()
    v_id = int(input("Select Vehicle ID: "))
    list_destinations()
    d_id = int(input("Select Destination ID: "))

    booking = Booking(customer_name=name, vehicle_id=v_id, destination_id=d_id)
    session.add(booking)
    session.commit()
    print(f"\nBooking successful for {name} to destination ID {d_id} using vehicle ID {v_id}.")

def view_bookings():
    print("\nAll Bookings:")
    bookings = session.query(Booking).all()
    for b in bookings:
        print(f"{b.customer_name} - Vehicle: {b.vehicle.name}, Destination: {b.destination.name}")

def main():
    while True:
        print("\n--- Safari Booking CLI ---")
        print("1. View Vehicles")
        print("2. View Destinations")
        print("3. Make Booking")
        print("4. View All Bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_vehicles()
        elif choice == '2':
            list_destinations()
        elif choice == '3':
            make_booking()
        elif choice == '4':
            view_bookings()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()