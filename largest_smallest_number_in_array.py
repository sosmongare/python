def find_largest_smallest(arr):
    largest = max(arr)
    smallest = min(arr)
    return largest, smallest

# Example usage:
numbers = [5, 2, 9, 1, 7]
largest_num, smallest_num = find_largest_smallest(numbers)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
