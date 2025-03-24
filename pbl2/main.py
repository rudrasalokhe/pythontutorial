from book import Book
from member import Member
from transaction import Transaction
from reports import Reports

if __name__ == "__main__":
    b1 = Book("Python Programming", "John Doe", "12345")
    b2 = Book("Machine Learning", "Jane Smith", "67890")
    
    m1 = Member("Alice", "M001")
    
    if m1.can_borrow():
        transaction1 = Transaction(b1, m1)
        m1.borrowed_books.append(b1)
        b1.available = False
    
    print("Issued Books:")
    Reports.issued_books([transaction1])
    