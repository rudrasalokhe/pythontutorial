# reports.py
class Reports:
    @staticmethod
    def issued_books(transactions):
        for transaction in transactions:
            if not transaction.return_date:
                print(f"{transaction.book.title} is issued to {transaction.member.name}")

    @staticmethod
    def fines_due(transactions):
        for transaction in transactions:
            if transaction.return_date and transaction.return_date > transaction.due_date:
                print(f"{transaction.member.name} has a fine due for {transaction.book.title}")
