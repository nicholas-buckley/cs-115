##########################################
# Name: Nicholas Buckley
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def all_true(lst):
    # TODO: Implement
    return reduce(and_, lst)

def and_(one, two):
    return one and two

print("all_true: " + str(all_true([True,True,True])))
    

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true(lst):
    # TODO: Implement
    return reduce(or_, lst)

def or_(one, two):
    return one or two

print("one_true: " + str(one_true([False,False,True]))) 

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true(lst):
    # TODO: Implement
    new_lst = map(convert, lst)
    return reduce(add, new_lst)

def convert(a):
    if a:
        return 1
    else:
        return 0

def add(a, b):
    return a + b

print("Num of trues: " + str(count_true([True,True,False,True,True,False,False,True])))


########################################################################################
# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].
def getLongestString():
    strings = getInput()
    str_length = map(get_length, strings)
    largest = reduce(highest, str_length)

    for s in strings:
        if len(s) == largest:
            return s

def get_length(s):
    return len(s)

def highest(a, b):
    if a > b:
        return a
    else:
        return b


print("Longest String: " + str(getLongestString()))
