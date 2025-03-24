class Marks:
    def __init__(self):
        self.subject_marks = {}

    def add_marks(self, subject, marks):
        self.subject_marks[subject] = marks

    def total_marks(self):
        return sum(self.subject_marks.values())

    def average_marks(self):
        return self.total_marks() / len(self.subject_marks) if self.subject_marks else 0
