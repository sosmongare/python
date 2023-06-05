"""
Please write a program which prints all permutations of [1,2,3]

Hints: Use itertools.permutations() to get permutations of list.
"""
# import itertools
# print(list(itertools.permutations([1,2,3])))

"""
Allw user to input the numbers to generate permutations.
"""

import itertools

# Prompt the user to enter numbers separated by commas
print ("---Permutation Calculator!---")
user_input = input("Enter numbers separated by commas: ")

# Split the input string into individual numbers and convert them to integers
numbers = [int(num) for num in user_input.split(",")]

# Generate permutations using itertools.permutations()
permutations = list(itertools.permutations(numbers))

# Print the permutations
print("Permutations:", permutations)
