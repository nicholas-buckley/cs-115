from math import factorial


def choose(n,k):
    result = 0
    #0 <= k <= n
    #if k is 0, there is only one way
    #if k == n, there is only one way
    if k == 0 or k == n:
        result = 1
    else:
        # 0 < k < n
        #focus on the first of the n items
        #Q: should we keep it or not (use-it or lose-it)
        
        #use_it: count of k-choices that include
        # the first item
        use_it = choose(n-1,k-1)
        #lose_it: count of k-choices that do
        # not include the first(so all k comes from the rest)
        lose_it = choose(n-1,k)

        result = use_it + lose_it

        return result
#pick 2 out of 4
#[a,b,c,d]
#[[a,b],[a,c],[a,d],[b,c],[b,d],[c,d]



def choose_factorial(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))    

    
#powerset
#[1,2,3] -> [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]

#1+3+3+1
#choose(3,0) + choose(3,1) + choose(3,2) + choose(3,3)
#(1 + 1)**n = \sum_{k=0..n} \choose(n,k) 1**(n-k) 1**k
#2**n
#1 2 3 ... (n-1) n
#Y N Y      Y    N --> [1,3,...,(n-1)]
#2*2*2 ...  2 *  2 = 2**n

def powerset(L):
    ''' build a list of lists, where eah inner list
        corresponds to a subset of the original list
        E.G. if the input is [1,2,3] then the output could be
        [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]'''
    
    result = []
    lose_it = []
    use_it = []

    #base case: L is empty, then powerset([]) = [[]]
    if not L:
        result = [[]]
    else:
        head, tail = L[0], L[1:]
        #use-it-or-lose-it w.r.t head
        
        #use-it: all subset that include head
        # one way of doing this is to pre-pend head to all
        # items in lose-it
        #append the head to all the results of the tail
        
        #lose-it: all sebsets that do not include head
        lose_it = powerset(tail)
        use_it = list(map(lambda lst: [head]+lst, lose_it))

        result = use_it + lose_it

    return result

def prepend_item(item, L):
    return [item] + L

def powerset_better(L):
    result, use_it, lose_it = [],[],[]
    
    if not L:
        result = [[]]

    else:
        head, tail = L[0], L[1:]
        lose_it = powerset(tail)
        use_it = list(map(lambda lst: prepend_item(head, lst), lose_it))

        result = use_it + lose_it

    return result

def combinations(L, k):
    return list(filter(lambda s: len(s) == k, powerset(L)))

def combination_rec(L, k):
    result, use_it, lose_it = [],[],[]
    #base cases:
    if k == 0:
        result = [[]]
    elif not L: #can't pick k>0 items from []
        result = []
    else:
        #use-it or lose-it
        head, tail = L[0], L[1:]
        lose_it = combination_rec(tail, k-1)
        use_it_helper = combination_rec(tail, k-1)
        use_it = list(map(lambda lst: prepend_item(head, lst), use_it_helper))

        result = use_it + lose_it

    return result
