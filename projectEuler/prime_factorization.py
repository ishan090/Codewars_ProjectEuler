
# Given a number, factorizes it into its prime components.

# Take 140 for example, it's prime decomposition is as follows:
# --> 2^2 * 5 * 7
# so, if one goes on checking some the smallest primes if they divide the number,
# then, once they've determined non-visivility, that prime is cleared...

## Imports
from math import sqrt, ceil
from timeit import default_timer as timer

# Relative imports
from prime_generator import gen_primes_uptil as primes_till
from prime_generator import next_prime
from prime_checker import prime_check, alt_check


def factor_prod(factors):
    out = 1
    for i in factors:
        out *= i ** factors[i]
    return out

def num_factors(prime_factors):
    """
    Given the prime factorization of a number, determines
    the number of factors it must have    
    """
    factors = 1
    for val in prime_factors.values():
        factors *= (val+1)
    return factors


def prime_factors(n):
    factors = {}
    root = ceil(n/2)
    for prime in primes_till(root):
        while n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n /= prime
    return factors

def quick_factors(n):
    is_prime = prime_check(n)
    if is_prime[0]:
        return {n: 1}
    divisor = is_prime[1]
    factors = quick_factors(int(n / divisor))
    factors[divisor] = factors.get(divisor, 0) + 1
    return factors

def all_factors(n):
    """
    Given a number n, finds all its factors     
    """
    prime_factors = quick_factors(n)
    factors = [1]
    for prime in sorted(prime_factors.keys()):
        prev_factors = factors[:]
        new_factors = []
        for power in range(1, prime_factors[prime]+1):
            new_factors += [i*prime**power for i in prev_factors]
        factors += new_factors
    return factors[:-1]

def unique_factors(n):
    """
    Returns False if n is divisible by p^x where x >= 2, p is a prime factor
    otherwise returns the prime decomposition    
    """
    is_prime = prime_check(n)
    if is_prime[0]:
        return {n: 1}
    divisor = is_prime[1]
    factors = quick_factors(int(n / divisor))
    if divisor in factors:
        return False
    factors[divisor] = factors.get(divisor, 0) + 1
    return factors

def alt_factors(n):
    is_prime = alt_check(n)
    if is_prime[0]:
        return {n: 1}
    divisor = is_prime[1]
    factors = alt_factors(int(n / divisor))
    factors[divisor] = factors.get(divisor, 0) + 1
    return factors



if __name__ == "__main__":
    ## SpeedTest
    # print("Performing speed test of the two competing algorithms")
    # val = 24876332
    # print("Timing the recusive algorithm...")
    # start = timer()
    # factors1 = quick_factors(val)
    # end = timer()
    # print("Time taken:", end-start, "\n")
    # # print(factors1)

    # print("Timing the newest algorithm...")
    # start = timer()
    # factors2 = alt_factors(val)
    # end = timer()
    # print("Time taken:", end-start, "\n")
    # print("Checking validity:", "Valid" if factors1 == factors2 else "Invalid!")
    # print(factors1)

    print(quick_factors(500))
    print(unique_factors(37))
