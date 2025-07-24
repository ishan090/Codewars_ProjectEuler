
# Euler's totient function, 
# [sometimes called the phi function], is defined as the number of
# positive integers not exceeding *n* which are relatively prime to *n*

# E.g., phi(7) = {1, 2, 3, 4, 5, 6} = 6 numbers
# The problem is concerned with the ratio n/phi(n) and finding a value
# for n where n <= 1e6 which has the maximum value of the ratio

### Hypothesis, numbers that have the largest number of prime factors
# are more likely to result in a smallest value of the phi function.

# Inbuilt Imports
import math
import random
from math import sqrt

# Relative imports
import relatively_prime
from prime_nearest import index_prime
from prime_generator import list_prime_till_prod, next_prime


# Highly interesting thoughts:
# * What's the correlation between a value of a prime and the distance
# to the next prime.
# Given p1, what's the estimated value of p2 - p1, where p2 is the next
# prime after p1



# to_test = [7, 2, 4, 0, 13, 11, 18, 21]
# test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
# for num in range(30):
#     print(index_prime(2, [2], True))


# print(next_prime(8, [2, 3, 5, 7]))


if __name__ == "__main__":
    print(list_prime_till_prod(1000000))
