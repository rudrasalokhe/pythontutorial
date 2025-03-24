class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __str__(self):
        return f"Student: {self.name}, Roll No: {self.roll_number}"
