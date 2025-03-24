import calendar
def display_calculator(year, month):
    print(calendar.month(year, month))


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
display_calculator(year, month)   