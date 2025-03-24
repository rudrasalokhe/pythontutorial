# report.py
from grading import Grading  # Import the Grading module

class Report:
    @staticmethod
    def generate_report(student, marks):
        total = marks.total_marks()
        average = marks.average_marks()
        grade = Grading.assign_grade(average)  # Now it will work

        print("\n--- Report Card ---")
        print(student)
        print("Subjects & Marks:", marks.subject_marks)
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
