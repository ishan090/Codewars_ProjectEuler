
from prime_generator import gen_primes_uptil
from pandigital import is_pandigital
from prime_checker import prime_check

m = 0
for prime in gen_primes_uptil(7654321):
    if is_pandigital(prime):
        m = prime
print(m)
