
from math import floor, ceil

t = int(input())


vals = []
for i in range(t):
    n, k = [int(b) for b in input().split(" ")]
    vals.append((n, k))


def possible(n, k):

    if n == k:
        return 0
    if n == 1 and k != 1:
        return -1
    if n == 0:
        return -1

    out = n
    pows = 0
    # print("here")
    while out % 2 == 0:
        # print("out, pows", out, pows)
        pows += 1
        out /= 2
        if out == k:
            return pows
    
    other = n / (2**pows)

    # print("this is pows:", pows)

    a, b = possible(floor(other/2), k), possible(ceil(other/2), k)
    pows += 1

    if a == -1 and b == -1:
        return -1
    elif -1 in (a, b):
        return pows + max(a, b)
    else:
        return pows + min(a, b)
    

woo = []
for j, k in vals:
    woo.append(possible(j, k))

for i in woo:
    print(i)
