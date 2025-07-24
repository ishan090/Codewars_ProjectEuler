
# Triangular numbers are obtained by adding consecutive natural numbers:
# 1 + 2 + 3 + 4 + ... + n

# This program is concerned with how divisible they are:

###Imports
from math import factorial as fac
from triangular import gen_nums, check_triangular, n_th
from prime_factorization import quick_factors, num_factors, factor_prod
from prime_generator import alt2_n


print(num_factors(quick_factors(28)))


# Naive attempt. Runs a loop through many many triangular numbers
# x = 1
# while True:
#     if x % 2 == 0:
#         fac1 = num_factors(quick_factors(x/2))
#         fac2 = num_factors(quick_factors(x+1))
#     else:
#         fac1 = num_factors(quick_factors(x))
#         fac2 = num_factors(quick_factors((x+1)/2))
#     print(x, x*(x+1)/2, fac1+fac2)
#     if fac1 + fac2 > 500:
#         print("Found triangular number with more than 500 divisors", x)
#         break
#     x += 1

# p = []
# prod = 1
# mult_order = [5]*3
# divisors = 500
# mult_order = []
# for k, j in quick_factors(divisors).items():
#     mult_order += [k] * j
# mult_order = [7, 5, 4, 2, 2]
# print("mult order is", mult_order)
# mult_val = 0
# triags = []
# for prime in alt2_n(len(mult_order)):
#     print("prime", prime)
#     new = prime ** (mult_order[mult_val]-1)
#     prod *= new
#     if mult_val != 0:
#         triags.append(triags[-1]*new)
#     else:
#         triags.append(new)
#     mult_val += 1

# print()
# print(prod)
# print(quick_factors(prod))
# 62370000

# print(num_factors(quick_factors(prod)))
# print(quick_factors(500))
# print("*"*50)

# for i in triags:
#     print("~~~~BLAH")
#     x = n_th(i)
#     print(quick_factors(x))
#     print(factor_prod(quick_factors(x)))
#     print(num_factors(quick_factors(x)))

n = 5369
while num_factors(quick_factors(int(n_th(n)))) <= 500:
    n += 1
print("found:", n, int(n_th(n)))

