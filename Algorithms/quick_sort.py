#%% sort in place
from random import randint

def ascending(lis, lo_pt, hi_pt):
    """
    lo_pt = index of first element
    hi_pt = index of last element 
    no return value, ascending sort in place
    """
    # base case
    if lo_pt >= hi_pt:
        return

    # select pivot and swap it to the end of the list
    pivot = randint(lo_pt, hi_pt)
    lis[pivot], lis[hi_pt] = lis[hi_pt], lis[pivot]
    pivot = hi_pt

    # sort
    done = lo_pt
    for i in range(lo_pt, hi_pt):
        if lis[i] < lis[pivot]:
            lis[i], lis[done] = lis[done], lis[i]
            done += 1

    # put pivot to the point seperation
    lis[pivot], lis[done] = lis[done], lis[pivot]
    pivot, done = done, pivot

    ascending(lis, lo_pt, pivot-1)
    ascending(lis, pivot+1, hi_pt)


#%% example
a = [4, 3, 5, 7]
ascending(a, 0, len(a)-1)
print(a)

#%% test
for i in range(100):
    test = []
    for j in range(10):
        test.append(randint(0, 100))
    print(i, test)
    ascending(test, 0, len(test)-1)
    if sorted(test) != test:
        print("error")
        print(sorted(test))
        print(test)
        break
