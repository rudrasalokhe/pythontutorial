# main.py
from student import Student
from marks import Marks
from grading import Grading
from report import Report

if __name__ == "__main__":
    # Create a student
    student1 = Student("Alice", "101")

    # Add marks
    marks1 = Marks()
    marks1.add_marks("Math", 85)
    marks1.add_marks("Science", 78)
    marks1.add_marks("English", 92)

    # Generate Report
    Report.generate_report(student1, marks1)
