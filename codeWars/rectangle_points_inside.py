
from math import sqrt, floor

def rectangle_rotation(b, a):
    a1 = floor(a/2/sqrt(2))*2+1

    print(a1)
    a2 = (floor((a/2 - sqrt(2)/2)/sqrt(2)) + 1 )*2
    print(a2)

    b1 = floor(b/2/sqrt(2))*2+1
    print(b1)
    b2 = (floor((b/2 - sqrt(2)/2)/sqrt(2)) + 1 )*2
    print(b2)

    return a1 * b1 + a2 * b2


print(rectangle_rotation(30, 2))

