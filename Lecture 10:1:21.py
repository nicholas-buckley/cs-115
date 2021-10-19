# basic recursion on list
# if L is a (non-empty) list, then we can break it down as
# first / rest (aka head / tail)

L = [3, 'a', [4, []]]
head = L[0]
tail = L[1:]
    
def length_recursive(L):
    base_val = 0

    def recursive_step(h, l):
        return 1 + length_recursive(l)
    
    if L == []: # not L
        result = base_val

    else:
        head, tail = L[0],L[1:]
        result = recursive_step(head, tail)

    return result


def map_recursive(f, L):
    base_val = []

    def recursive_step(h, t):
        first = f(h)
        rest = map_recursive(f, t)
        return [first] + rest

    
    if L == []: # not L
        result = base_val

    else:
        head, tail = L[0],L[1:]
        result = recursive_step(head, tail)

    return result


# branch recursion
# aka use it or lose it
# counting combinations
# k choose n
# binomial coefficient
# (a+b)**n = \sum_{i=0..n} (n choose i) a**i b**(n-1)


def choose_rec(n, k):
    '''Count the number of ways in which k items might be taken from 
        a group of n'''
    # 0 <= k <= n
    # choose(n, k) = n! / (k!*(n-k)!)
    ## n == 0: only one way
    ## k == 0: only 1
    ## k == n only 1 way (must pick all)
    ## otherwise, 0 < k < n
    ## focus on say the first item in the group of n
    ## Choice: use-it or lose-it
    ## USE-IT: choose(k-1, n-1)
    ## LOSE-IT: choose(k, n-1)

    if k == 0 or k == n:
        result = 1
    else:
        use_it = choose_rec(k-1,n-1)
        lose_it = choose_rec(k,n-1)
        result = use_it + lose_it

    return result
