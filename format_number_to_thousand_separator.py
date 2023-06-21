def format_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    formatted_str = ",".join(reversed_str[i:i+3] for i in range(0, len(reversed_str), 3))
    return formatted_str[::-1]

# Example usage with input validation
while True:
    try:
        number = int(input("Enter a non-negative number: "))
        if number >= 0:
            formatted_number = format_number(number)
            print("Formatted number:", formatted_number)
            break
        else:
            print("Please enter a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative number.")
