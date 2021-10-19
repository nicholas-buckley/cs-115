############################################################
# CS115 Lab 4
# Name: Nicholas Buckley
# Pledge: I pledge my honor that I have abided by the Stevens Honor System 
############################################################

from functools import reduce

# Task 1: Use reduce to add up all elements in a list
"""
Input: A list of numbers
Output A number representing the sum
Example: add_all([1, 2, 3]) = 6
"""
def add_all(lst):
    result = reduce(lambda x1,x2: x1+x2,lst)
    return result

print(add_all([1,2,3]))

# Task 2: Use map to evaluate a given polynomial at a specific x-value
"""
Input:
  p: A list of coefficients for increasing powers of x
  x: The value of x to evaluate
Output: Number representing the value of the evaluated polynomial
Example: poly_eval([1, 2, 3], 2) = 1(2)^0 + 2(2)^1 + 3(2)^2 = 17
"""
def poly_eval(p, x):
    def add(a,b):
        return a + b
    def mult(a,b):
        return a * b         
    def x_powers(i):
        return x ** i

    powers = map(x_powers, range(0,len(p)))
    multiply = map(mult, powers, p)
    return reduce(add, multiply)

print(poly_eval([1,2,3], 2))
