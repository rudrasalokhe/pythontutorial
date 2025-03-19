  marks= []subjects = 5
    for i in range(1, subjects+1):
        mark = float(input(f'Enter the subject for {i}'))
        marks.append(mark)

    total_marks = sum(marks)
    percentage = (total_marks/subjects)*100
    print(percentage)
    if percentage >= 75:
        division = "First class with Distinction"
    elif percentage >= 60:
        division = "First Class"
    elif percentage >= 45:
        division = "Second Class"
    elif percentage >= 40:
        division = "Pass"
    else:
        print("Fail.")