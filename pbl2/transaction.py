from datetime import datetime, timedelta

class Transaction:
    FINE_PER_DAY = 5  # Fine amount per overdue day
    
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=14)
        self.return_date = None
    
    def return_book(self):
        self.return_date = datetime.now()
        overdue_days = (self.return_date - self.due_date).days
        fine = max(0, overdue_days * Transaction.FINE_PER_DAY)
        self.book.available = True
        self.member.borrowed_books.remove(self.book)
        return fine
    
    def __str__(self):
        return f"Book: {self.book.title}, Issued to: {self.member.name}, Due: {self.due_date.strftime('%Y-%m-%d')}"
