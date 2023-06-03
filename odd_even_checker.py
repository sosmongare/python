"""
In this code, the input() function is used to prompt the user to enter a number. The int() function is then used to convert the input string into an integer. The number is stored in the variable n, and the code checks if n is divisible by 2 using the modulo operator %. If the remainder is 0, it means the number is even, and the corresponding message is printed. Otherwise, it's an odd number, and the appropriate message is printed.
"""

def checkValue():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

checkValue()

"""
In this code, the while True loop creates an infinite loop that continues until a specific condition is met. Inside the loop, the user is prompted to enter a number or enter 'exit' to quit. If the user enters 'exit', the loop is terminated using the break statement.

If the user enters a number, it is stored as a string in the variable n. The code then checks if n is equal to 'exit'. If it is, the loop is broken and the program ends. Otherwise, n is converted to an integer using int(n), and the code proceeds to check if it's odd or even and prints the appropriate message. The loop then continues, prompting the user for another number.
"""

def checkValue():
    while True:
        n = input("Enter a number (or 'exit' to quit): ")
        if n.lower() == 'exit':
            break

        n = int(n)
        if n % 2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")

checkValue()
