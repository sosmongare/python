"""
In this example, we use the [::-1] slicing technique on the numbers array to create a reversed version of the array called reversed_numbers. When the [::-1] slice is applied, it returns a new list with elements in reverse order. Finally, we print the reversed_numbers list, which represents the original array in reverse order.
"""
numbers = [5, 2, 9, 1, 7]

# Print the array in reverse order
reversed_numbers = numbers[::-1]
print(reversed_numbers)
