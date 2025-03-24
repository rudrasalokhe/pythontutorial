# customer.py
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Customer: {self.name}, Phone: {self.phone}, Email: {self.email}"
