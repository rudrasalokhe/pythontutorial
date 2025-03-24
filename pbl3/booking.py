# booking.py
from datetime import datetime

class Booking:
    def __init__(self, customer, room, check_in, check_out):
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.total_days = (check_out - check_in).days
        self.is_active = True

    def cancel_booking(self):
        self.is_active = False
        self.room.cancel_booking()

    def __str__(self):
        return f"Booking for {self.customer.name}: Room {self.room.room_number}, Check-in: {self.check_in}, Check-out: {self.check_out}"
