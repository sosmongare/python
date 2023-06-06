from random import shuffle

print("***Number Shuffler***")

# Take input from the user
numbers = input("Enter numbers to shuffle separated by commas: ")

# Split the input string into a list of numbers
numbers_list = numbers.split(",")

# Convert the input numbers from strings to integers
li = [int(num) for num in numbers_list]

# Shuffle the list
shuffle(li)

# Print the shuffled list
print(li)
