#!/usr/bin/python3

"""
To run the application, make sure you are passing the required command-line argument when executing the script.
You should run the script as follows:
        python algebra_solver.py "2*x = 10"
"""
from sympy import *
import sys

def solver(x):
	sympy_eq = sympify("Eq(" + x.replace("=", ",") + ")")
	result = solve(sympy_eq)
	return result[0]

def main(x):
	X = solver(x)
	print("X = " + str(X))

if __name__ == "__main__":
	main(sys.argv[1])