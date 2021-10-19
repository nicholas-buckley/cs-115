###################################################################
# CS115 Lab 5
# Name: Nicholas Buckley
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
###################################################################

#My Length Fuction
def length(x):
    result = 0
    if x == []:
        result = 0
    else:
        prevResult =  1 + length(x[1:])
        result = prevResult
    return result
###################################################################
    
#1 Dot Product
def dotProduct(L, K):
    result = 0

    if length(L) == 1:
        result = L[0] * K[0]
    
    if length(L) > 1:
        result = L[0] * K[0]
        prevResult = dotProduct(L[1:],K[1:])
        result += prevResult

    return result

###################################################################

#2 removeAll
def removeAll(e, L):
    result = []
    
    if length(L) > 0:
        if e != L[0]:
            result = [L[0]]
        prevResult = removeAll(e, L[1:])
        result += prevResult
        

    return result

###################################################################

#Geometric Sequence
def geometricSeq(n,f,b):
    result = 0
    
    if n == 1:
        result = b
    elif n > 1:
        result = geometricSeq(n-1,f,f*b)

    return result

###################################################################

#Deep Reverse
def deepReverse(L):
    result = []

    if length(L) > 0:
        if(isinstance(L[0], list)):
            result += deepReverse(L[1:]) + [deepReverse(L[0])]

        else:
            prevResult = deepReverse(L[1:])
            result = prevResult + [L[0]]

    return result

    
