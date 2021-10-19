from functools import reduce

print(max([0,1,2,3,4,5,6]))

L = [1,2,3,4,5,6,7,8]
print(max(L))

def my_max(x,y):
    if x > y:
        return x
    else:
        return y

print(my_max(10,14))
print(reduce(my_max,L))

def my_max_shorter(x,y):
    return x if x > y else y

print(my_max_shorter(11,12))

#One Line Max
print(reduce(lambda x,y: x if x>y else y, L))

#One Line Min
print(reduce(lambda x,y: x if x<y else y, L))

#One Line Average
print(reduce(lambda x,y: x+y, L)/len(L))

#One Line Thing
print(reduce(lambda x,y: x*y, L)**(1/len(L)))


#Filter
def evens(bound):  
    return list(range(0,bound+1,2))


print(evens(10))

def three_multiples(bound):
    def is_three_mult(x):
        return x%3 == 0

    ints = range(bound)

    return list(filter(is_three_mult,ints))

print(three_multiples(10))

print(list(filter(lambda x: x%3 == 0, range(0,10))))

L = [1,103,1]
print(L[1])
print(L[-2])

