# billing.py
class Billing:
    @staticmethod
    def calculate_total(booking):
        if booking.is_active:
            return booking.total_days * booking.room.price_per_night
        return 0

    @staticmethod
    def generate_bill(booking):
        amount = Billing.calculate_total(booking)
        return f"Bill for {booking.customer.name}: ${amount} (Room {booking.room.room_number})"
