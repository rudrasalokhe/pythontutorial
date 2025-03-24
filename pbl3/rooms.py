    # rooms.py
class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def cancel_booking(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.room_number} ({self.room_type}) - {status}"
