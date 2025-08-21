### Checks if a number is prime

## Imports
from math import sqrt, ceil
from timeit import default_timer as timer
# Relative imports
from prime_generator import gen_primes_uptil as primes_till
from prime_nearest import index_prime


def prime_check(n):
    if n == 1:
        return False, False
    if n == 2:
        return True, True
    root = ceil(sqrt(n))
    for num in range(2, root+1):
        if n % num == 0:
            return False, num
    return True, True


def prime_check_given_primes(n, primes):
    try:
        root = ceil(sqrt(n))
    except ValueError:
        return False, False
    nearest_prime = index_prime(root, primes)
    for num in range(0, nearest_prime+1):
        if n % primes[num] == 0:
            return False, num
    return True, True


def alt_check(n):
    root = ceil(sqrt(n))
    for num in primes_till(root+1):
        if n % num == 0:
            return False, num
    return True, True


if __name__ == "__main__":
    speed_check = False
    if speed_check:
        print("Performing speed test of the two competing algorithms")
        val = 10112269203786181
        print("Timing the recusive algorithm...")
        start = timer()
        factors1 = prime_check(val)
        end = timer()
        print("Time taken:", end-start, "\n")
        # print(factors1)

        print("Timing the newest algorithm...")
        start = timer()
        factors2 = alt_check(val)
        end = timer()
        print("Time taken:", end-start, "\n")
        print("Checking validity:", "Valid" if factors1 == factors2 else "Invalid!")
        print(factors1)
    to_check = [133]
    for p in to_check:
        result = prime_check(p)
        print(p, "is", "" if result[0] else f"not ({result[1]})", "a prime")

