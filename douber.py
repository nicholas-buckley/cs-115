def doubler(x):
    i = x * 2
    return i


ls = [1,2,3,4]
double = map(doubler, ls)

print(list(double))
