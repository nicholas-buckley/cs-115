#recursion
#factorial

from math import factorial
# n! = 1 * 2 * 3 * 4 * ... * n
print(factorial(10))

#cases:
#0! = 1
#1! = 1
#n! = (n-1)! * n

#n! := (n-1)! * n (for n >= 2)

def rec_factorial(n):
    result = 1
    #simple recursive definition of factorial
    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        prev_result = rec_factorial(n-1)
        result = prev_result * n

    return result

def rec_factorial_short(n):
    result = 1

    if n > 1:
        result = rec_factorial_short(n-1) * n

    return result
