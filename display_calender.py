import calendar
from datetime import datetime

# Function to validate the year input
def validate_year(year):
    while True:
        try:
            yy = int(input("Enter year: "))
            if yy >= year:
                return yy
            else:
                print("Invalid year. Please enter a year greater than or equal to", year)
        except ValueError:
            print("Invalid input. Please enter a valid year.")

# Function to validate the month input
def validate_month():
    while True:
        try:
            mm = int(input("Enter month: "))
            if 1 <= mm <= 12:
                return mm
            else:
                print("Invalid month. Please enter a month between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid month.")

# Get the current year
current_year = datetime.now().year

# Ask for year
yy = validate_year(current_year)

# Ask for month
mm = validate_month()

# Display the calendar
print(calendar.month(yy, mm))
