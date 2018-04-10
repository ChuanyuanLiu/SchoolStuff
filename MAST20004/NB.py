from math import factorial
import matplotlib.pyplot as plt
import numpy as np

p = 1/4.0
r = 2.0
# to N th term do you want to end?
N = 21

pmf = []

# choose function
# returns a float


def choose(n, k):
    return factorial(n)/factorial(k)/factorial(n-k)

# use matplotlib.pyplot to print out a bar graph


def draw(pmf):
    plt.bar(np.arange(N), pmf)
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.title('Negative Binomial distribution NB({},{})'.format(r, p))
    plt.show()


def printMD(pmf):
    odd = 0.0
    even = 0.0
    print("z  | p(Z=z)")
    print("---|---")

    for i, j in enumerate(pmf):
        print('{:<2} | {:3.4f}'.format(i, j))
        if i % 2:
            odd += j
        else:
            even += j

    print('total sum of odd possibilties from 0 to {}: {:3.4f}'.format(N, odd))
    print('total sum of even possibilties from 0 to {}: {:3.4f}'.format(N, even))


for z in range(N):
    pmf.append(choose(z+r-1, r-1)*p**r*(1-p)**z)

# print markdown
printMD(pmf)
# draw a bar graph
draw(pmf)
