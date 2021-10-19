####################################################################################
# Name: Nicholas Buckley
# Pledge: I pledge my honor that I have abided by the Stevens Honor Code
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
    result = []

    if x == 0:
        result = []
    else:
        after = decimalToBinary(x // 2)
        result = [x % 2] + after

    return result
    

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
    result = 0

    if len(num) == 0 or (len(num) == 1 and num[0] == 0):
        result = 0
    else:
        after = binaryToDecimal(num[:-1])
        result = num[-1] * 2**(len(num)-1) + after

    return result

# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
    result = []

    if len(num) == 0:
        result = []
    else:
        num[0] += 1
        if num[0] > 1:
            num[0] -= 2
            if(len(num) > 1):
                tail = incrementBinary(num[1:])
            else:
                tail = [1]
            result = [num[0]] + tail
        else:
            result = num

    return result

    

    

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
def addBinary(num1, num2):
    result = []

    shorter = []
    longer = []

    if len(num1) == 0 and len(num2) == 0:
        result = []
    elif len(num1) == 0:
       result = incrementBinary([num2[0]-1] + num2[1:])
    elif len(num2) == 0:
        result = incrementBinary([num1[0]-1] + num1[1:])       
    else:
        if(len(num1) < len(num2)):
            longer = num2
            shorter = num1
        else:
            longer = num1
            shorter = num2
        
        longer[0] = num1[0] + num2[0]

        if longer[0] > 1:
            longer[0] -= 2
            if(len(longer) > 1):      
                longer[1] += 1
            else:
                longer += [1]
        
        tail = addBinary(longer[1:], shorter[1:])

        result = [longer[0]] + tail

    return result
        

   
