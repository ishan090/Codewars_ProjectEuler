
from math import sqrt, ceil

def totient(x):
    if x == 2:
        return [x]
    s = ceil(sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return [i] + totient(int(x/i))
    return [x]

print(totient(10))
