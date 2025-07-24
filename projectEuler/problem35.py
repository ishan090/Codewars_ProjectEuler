# A prime is circular if all rotations of its digits lead to a prime
# E.g., 197 -> 971 -> 719
# Find how many circular primes there are under 1 million
# NOTE: a rotation isn't the same as a permutation. Observe:
# 12345 -> 51234 -> 45123 -> 34512 -> 23451 -> 12345
# Just the last digit wraps around to become the first

# Imports
from prime_checker import prime_check
from prime_generator import gen_primes_uptil as primes_till

def gen_rotations(num):
    num = str(num)
    for i in range(len(num)):
        num = num[-1] + num[:-1]
        yield int(num)

def list_rotations(num):
    num = str(num)
    out = []
    for i in range(len(num)):
        num = num[-1] + num[:-1]
        out.append(num)
    return [int(i) for i in out]


def is_circular(n):
    for rot in gen_rotations(n):
        if not prime_check(rot)[0]:
            return False
    return True


def find_circular_primes_till(n):
    explored = []
    circular_primes = 0
    for prime in primes_till(n):
        # print("considering prime", prime)
        if prime in explored:
            # print("\tops, already explore.. next")
            continue
        rots = set(list_rotations(prime))
        # print("\tfound a list of rotations")
        flag = True
        for rot in rots:
            # print("\trot", rot)
            if not prime_check(rot)[0]:
                # print("\toh, was composite... next")
                flag = False
        if not flag:
            continue
        explored += rots
        # print("adding", len(rots), "to count")
        # print("current count ->", circular_primes)
        circular_primes += len(rots)
    return circular_primes


print(find_circular_primes_till(800000))
# count = 0
# for i in primes_till(800000):
#     count += 1
# print(count)


