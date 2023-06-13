"""
Create a python program. Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""
def descending_order(num):
    sorted_digits = sorted(str(num), reverse=True)
    result = int(''.join(sorted_digits))
    return result

# Allow the user to input numbers
while True:
    try:
        num = int(input("Enter a non-negative integer (or enter -1 to exit): "))
        if num < 0:
            break
        print("Output:", descending_order(num))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

print("Program exited.")
