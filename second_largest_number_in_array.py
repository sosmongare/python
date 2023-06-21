def find_second_largest(arr):
    sorted_numbers = sorted(arr, reverse=True)
    
    if len(sorted_numbers) >= 2:
        second_largest = sorted_numbers[1]
        return second_largest
    else:
        return None

# Example usage:
numbers = [5, 2, 9, 1, 8, 7]
second_largest_num = find_second_largest(numbers)

if second_largest_num is not None:
    print("Second largest number:", second_largest_num)
else:
    print("There is no second largest number in the array.")


"""
Other solution:


numbers = [5, 2, 9, 1, 7]

# Sort the array in descending order
sorted_numbers = sorted(numbers, reverse=True)

# Access the element at index 1 (second largest)
second_largest = sorted_numbers[1]

# Print the second largest number
print("Second largest number:", second_largest)

"""

