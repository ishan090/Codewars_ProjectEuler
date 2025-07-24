
# Here's the problem:
# https://www.codewars.com/kata/52cf02cd825aef67070008fa
# Objective to use the encoding function to figure out the decoding function
import numpy as np
import math


letters = "~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "

def decode(s):
    out = ""
    for i, j in enumerate(s):
        if j not in letters:
            out += j
            continue
        p = (i+1)%66
        if (i+1)%66 == 0:
            p += 66
        a = int(math.pow(2, p))
        v = letters.index(j)
        # Thus, (2^i)x is congruent to v (mod 67)
        # => Implies, (2^i)x - 67m = v
        # Now, I know how to solve this guy:
        # (2^i)p + 67q = gcd(coefs) = 1 (because 67 is a prime)
        # Once p is found, it can be scaled up to x by factor v/gcd(coefs)
        x, y = euclidean_gcd(a, 67)
        x *= v
        x %= 67
        out += letters[x]
    return out

def euclidean_gcd(a, b, a_val=None, b_val=None):
    """
    Given the coefs of the expression:
    ax + by,
    finds the x and y values for which the equation equals gcd(a, b)
    a_val, b_val are numpy arrays
    """
    if a_val is None or b_val is None:
        a_val = np.array([1, 0])
        b_val = np.array([0, 1])
    # The idea behind the euclidiean algorithm:
    # represent a as k*b + r
    # Then swap a for b and b for r and repeat until there's no remainder remaining. b is the gcd
    r = a % b
    r_val = a_val - (a//b)*b_val
    if b % r == 0:
        return r_val
    return euclidean_gcd(b, r, b_val, r_val)


def encode(s):
    x = 1
    out = ""
    while x <= len(s):
        if s[x-1] not in letters:
            out += s[x-1]
            x += 1
            continue
        print("x is", x)
        print("pow is", math.pow(2, x))
        print("mult component is", letters.index(s[x-1]))
        print("prod; remainder =", int(math.pow(2, x) * letters.index(s[x-1])), \
            int(math.pow(2, x) * letters.index(s[x-1])) % len(letters))
        out += letters[int(math.pow(2, x) * letters.index(s[x-1])) % len(letters)]
        x += 1
    return out



# print(euclidean_gcd(46, 26))

