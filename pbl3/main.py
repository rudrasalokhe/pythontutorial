# main.py
from rooms import Room
from customer import Customer
from booking import Booking
from billing import Billing
from datetime import datetime

if __name__ == "__main__":
    # Create rooms
    room1 = Room(101, "Deluxe", 1500)
    room2 = Room(102, "Suite", 2500)

    # Register customer
    customer1 = Customer("Alice", "9876543210", "alice@example.com")

    # Check-in and check-out dates
    check_in_date = datetime(2025, 3, 25)
    check_out_date = datetime(2025, 3, 28)

    # Book a room
    if room1.book_room():
        booking1 = Booking(customer1, room1, check_in_date, check_out_date)
        print("Booking Successful!")
        print(booking1)

    # Generate Bill
    print(Billing.generate_bill(booking1))

    # Cancel Booking
    booking1.cancel_booking()
    print("Booking Canceled.")
    print(room1)
