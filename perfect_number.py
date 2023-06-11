"""
This is a Python Program to check if a number is a Perfect number.

Problem Description
The program takes a number and checks if it is a Perfect number.

Problem Solution
1. Take in an integer and store it in a variable.
2. Initialize a variable to count the sum of the proper divisors to 0.
3. Use a for loop and an if statement to add the proper divisors of the integer to the sum variable.
4. Check if the sum of the proper divisors of the number is equal to the variable.
5. Print the final result.
6. Exit.

Program/Source Code
Here is source code of the Python Program to check if a number is a Perfect number. The program output is also shown below.

 
"""
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")