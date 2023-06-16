"""
we use a while loop to repeatedly ask the user for input until they provide a valid year of birth. The try-except block is used to catch any exceptions that may occur when converting the input to an integer. If the year of birth is greater than the current year, an error message is displayed.

This validation ensures that the user enters a valid year of birth and prevents any invalid input that may cause errors in the calculation.
"""
import datetime

def calculate_age(year_of_birth):
    current_date = datetime.date.today()
    age = current_date.year - year_of_birth
    birth_date = datetime.date(year_of_birth, current_date.month, current_date.day)

    if birth_date > current_date:
        age -= 1
        birth_date = datetime.date(year_of_birth - 1, current_date.month, current_date.day)

    # Calculate the number of months and days
    if birth_date.month > current_date.month:
        age -= 1
        months = (12 - birth_date.month) + current_date.month
    else:
        months = current_date.month - birth_date.month

    if birth_date.day > current_date.day:
        months -= 1
        days = (birth_date.day - current_date.day) % 30
    else:
        days = current_date.day - birth_date.day

    return age, months, days

# Get the year of birth from the user with validation
while True:
    try:
        year_of_birth = int(input("Enter your year of birth: "))
        current_year = datetime.date.today().year
        if year_of_birth <= current_year:
            break
        else:
            print("Invalid year. Please enter a year in the past.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Calculate the age
age, months, days = calculate_age(year_of_birth)

# Print the result
print("Your age is {} years, {} months, and {} days.".format(age, months, days))
