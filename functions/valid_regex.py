"""
Q: User
Write a code in Python to find out whether a given string S is a valid regex or not.


To determine whether a given string S is a valid regular expression (regex) in Python, you can use the re module, which provides support for regular expressions.

In this code, the is_valid_regex function attempts to compile the input pattern using re.compile. If the compilation is successful, the function returns True, indicating that the input is a valid regex. If a re.error exception is raised during the compilation, it means the input is not a valid regex, and the function returns False.

You can input your desired regex pattern, and the program will display whether it is valid or not.
"""
import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

# Test the function
regex_string = input("Enter a regex pattern: ")
if is_valid_regex(regex_string):
    print("Valid regex!")
else:
    print("Invalid regex!")
