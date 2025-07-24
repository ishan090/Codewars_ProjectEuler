# Generates prime numbers based on many different criteria:
# There cumulative sum, product, largest prime, next prime after a previous prime, etc.

### Package Imports
import math
from math import sqrt, ceil
from timeit import default_timer as timer

### Relative Imports
from prime_nearest import index_prime


### Based on the cumulative product
# Not a generator
def list_prime_till_prod(n):
    """
    Lists all the consecutive primes whose prod is less than n
    Outputs a tuple with the list of primes and their prod    
    """
    primes_list = [2]
    prod = 2
    x = 3
    while prod * x <= n:
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
        if is_prime:
            primes_list.append(x)
            prod *= x
        x += 1
    return primes_list, prod

# Generator for the same
def gen_prime_till_prod(n):
    primes_list = [2]
    prod = 2
    x = 3
    while prod * x <= n:
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
        if is_prime:
            primes_list.append(x)
            prod *= x
            yield primes_list, prod
        x += 1
    return primes_list, prod


## Based on the cumulative sum
def list_prime_till_sum(n):
    primes_list = [2]
    total = 2
    x = 3
    while total + x <= n:
        print("exploring num", x)
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
        if is_prime:
            primes_list.append(x)
            total += x
        x += 1
    return primes_list, total


def gen_prime_till_sum(n):
    primes_list = [2]
    total = 2
    x = 3
    while total + x <= n:
        print("exploring num", x)
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
        if is_prime:
            primes_list.append(x)
            total += x
            yield primes_list, totall
        x += 1
    return primes_list, total


### Primes by number of primes
def list_n_primes(n):
    primes_list = [2]
    total = 1
    x = 3
    while total + 1 <= n:
        # print("exploring num", x)
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
        if is_prime:
            primes_list.append(x)
            total += 1
        x += 1
    return primes_list


def gen_n_primes(n):
    primes_list = [2]
    yield 2
    total = 1
    x = 3
    while total + 1 <= n:
        # print("exploring num", x)
        is_prime = True
        root = ceil(sqrt(x))
        prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
            total += 1
            yield x
        x += 1

def alt_gen_n(n):
    primes_list = [2]
    prime_index = 0
    yield 2
    total = 1
    x = 3
    while total + 1 <= n:
        # print("exploring num", x)
        is_prime = True
        root = ceil(sqrt(x))
        if root > primes_list[prime_index]:
            prime_index += 1
        # prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
            total += 1
            yield x
        x += 1


def alt2_n(n):
    def when_index_change(index_val):
        return index_val*index_val
    primes_list = [2]
    prime_index = 0
    theshold = when_index_change(2)
    yield 2
    total = 1
    x = 3
    while total + 1 <= n:
        # print("exploring num", x)
        is_prime = True
        if x > theshold:
            prime_index += 1
            theshold = when_index_change(primes_list[prime_index])
        # prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
            total += 1
            yield x
        x += 2

def gen_primes_uptil(n):
    def when_index_change(index_val):
        return index_val*index_val
    primes_list = [2]
    prime_index = 0
    theshold = when_index_change(2)
    yield 2
    x = 3
    while x <= n:
        # print("exploring num", x)
        is_prime = True
        if x > theshold:
            prime_index += 1
            theshold = when_index_change(primes_list[prime_index])
        # prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
            yield x
        x += 2

def list_primes_uptil(n):
    def when_index_change(index_val):
        return index_val*index_val
    primes_list = [2]
    prime_index = 0
    theshold = when_index_change(2)
    x = 3
    while x <= n:
        # print("exploring num", x)
        is_prime = True
        if x > theshold:
            prime_index += 1
            theshold = when_index_change(primes_list[prime_index])
        # prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
        x += 2
    return primes_list


# for p in gen_primes_uptil(100):
#     print(p)


def gen_primes_from(x, n, primes):
    """
    Generates primes from ater a number given the primes that come before it
    x: the number to generates primes from
    n: the number of primes to generate
    primes: the number of primes uptil x
    x has to be prime checked
    """
    def when_index_change(index_val):
        return index_val*index_val
    primes_list = primes
    prime_index = index_prime(ceil(sqrt(x)), primes)
    theshold = when_index_change(primes[prime_index])
    total = 0
    if x % 2 == 0:
        x += 1
    while total + 1 <= n:
        # print("exploring num", x)
        is_prime = True
        if x > theshold:
            prime_index += 1
            theshold = when_index_change(primes_list[prime_index])
        # prime_index = index_prime(root, primes_list)
        for i in range(prime_index+1):
            if x % primes_list[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(x)
            total += 1
            yield x
        x += 2

# for p in gen_primes_from(8, 10, [2, 3, 5, 7]):
#     print(p)




### Outputs the next prime after a number given a complete list of primes preceding it
def next_prime(n, primes_before):
    """
    Given a number n and the primes that precede it,
    finds the prime that succeeds n.
    Assumes that n isn't a prime
    """
    if n < primes_before[-1]: # if the number is inside the known list of primes, then
        # just index it.
        return index_prime(n+1, primes_before)
    # Otherwise, run a loop testing numbers after n
    while True:
        is_prime = True
        root = ceil(sqrt(n))
        prime_index = index_prime(root, primes_before)
        for i in range(prime_index+1):
            if n % primes_before[i] == 0:
                is_prime = False
        if is_prime:
            return n
        n += 1


if __name__ == "__main__":
    test_size = 10000
    print("Speed test between two competing prime generator algorithms")
    print("New Alt method...")
    start = timer()
    primes1 = []
    for i in alt2_n(test_size):
        primes1.append(i)
    end = timer()
    print("Time Taken:", end-start, "\n")

    print("Timing the alternative method...")
    start1 = timer()
    primes2 = []
    for i in alt_gen_n(test_size):
        primes2.append(i)
    end1 = timer()
    print("Time Taken:", end1-start1, "\n")
    print("Last prime:", primes2[-1])

    print("Measuring validity of the results:", primes1 == primes2)



