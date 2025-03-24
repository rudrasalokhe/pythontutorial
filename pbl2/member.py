class Member:
    def __init__(self, name, member_id, max_books=3):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = max_books
    
    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books
    
    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - Books Borrowed: {len(self.borrowed_books)}/{self.max_books}"
