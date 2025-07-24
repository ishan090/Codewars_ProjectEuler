
# A pandigital number is defined to have as many unique digits as the number
# of digits it has
# Obviously a number with more than 9 digits cannot be pandigital
# This problem is concerned with products such as the digits of the multiplicand,
# multiplier and product are pandigital with digits from 1 to 9.

# Idea: Given a times b = c, where a < b < c,
# The value of a, b and c must each be greater than or equal to 1e1, 1e2, 1e3
# for the product to have 9 digits (2 + 3 + 4)
# This shall be the basis of the loop which shall loop over a first (1e1 through 98)
# and then b

# Imports
from math import floor, log10

def is_pandigital(n):
    string_n = str(n)
    if "0" in string_n:
        return False
    found = []
    for i in string_n:
        if i in found:
            return False
        found.append(i)
    return True

pans = []
products = []
product_sum = 0
for a in range(11, 4988):
    if not is_pandigital(a):
        continue
    for b in range(10000//a + 2):
        if not len(str(a) + str(b) + str(a*b)) == 9:
            continue
        if is_pandigital(int(str(a) + str(b) + str(a*b))) and a*b not in products:
            pans.append((a, b, a*b))
            products.append(a*b)
            product_sum += a*b
print(pans)
print(product_sum)
