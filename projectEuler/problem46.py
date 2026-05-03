# Relates to Goldbach's other conjecture that:
# "every odd composite number can be written as:
# the sum of a prime and twice a square."

# --> odd composite = prime + 2 * square
# This conjecture happened to be False.
# Find the smallest odd composite number that cannot be written
# in this way

# IMPORTS:
from prime_checker import prime_check
from composite import composite_odd
from math import sqrt, ceil




def goldbach(n):
    assert n % 2 == 1, "Not odd"
    print(n)
    r = ceil(sqrt(n/2))
    print("this is the r for", n, "->", r)
    for i in range(1, r+1):
        print(f"{i}/{r}")
        to_check = n - 2 * i*i
        print("to check:", to_check)
        if prime_check(to_check)[0]:
            # FALSE
            return True, "GOLDBACH"
    return False, n


if __name__ == "__main__":
    blah = composite_odd()
    k = next(blah)
    while True:
        out = goldbach(k)
        if not out[0]:
            print(out)
            break
        k = next(blah)

