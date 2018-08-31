import random
import matplotlib.pyplot as plt
import numpy as np
import math


N_coins = 100
# will run for some time
M_trials = 1000000
p = 1/4
Frequency = [0]*(N_coins)
# distance between two events [i = j, |i-j|=1, |i-j|≥2]
# I shortened the name to DBTE
DBTE = [0]*3

def randomDiscreet(x, pmf):
    i = 0
    tmp = pmf[i]
    while (tmp <= random.random()):
        i += 1
        tmp += pmf[i]
    return x[i]

def draw(pmf):
    plt.bar(np.arange(N_coins), pmf)
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.show()

def trial():
    array = []
    N_change = 0
    # simulate coin flips
    for i in range(N_coins):
        array.append(randomDiscreet([1,0],[p, 1-p]))
    # get number of changes
    for i in range(N_coins-1):
        if array[i] != array[i+1]:
            N_change+=1
    # check if random i and j are connected
    i = random.randint(0, N_coins-2)
    j = random.randint(0, N_coins-2)
    if (array[i] != array[i+1] and array[j] != array[j+1]):
        # case 1 when i = j
        if i == j: 
            DBTE[0] += 1/M_trials
        elif math.fabs(i-j) == 1: 
            DBTE[1] += 1/M_trials
        else: 
            DBTE[2] += 1/M_trials
    return N_change

for i in range(M_trials):
    Frequency[trial()] += 1/M_trials


def expectedValue(n, p):
    distance0 = 1/(n-1)*(2*p*(1-p))
    distance1 = (2*n-4)/(n-1)**2*(p*(1-p))
    distance_more_than_1 = (n**2-5*n+6)/(n-1)**2*(4*p**2*(1-p)**2)
    print(distance0 + distance1 + distance_more_than_1)

print(DBTE)
print(sum(DBTE))
expectedValue(N_coins, p)
# draw(Frequency)



