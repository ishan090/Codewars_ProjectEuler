# Related to finding all the left to right and right to left truncatable primes

from truncatable_primes import create_t_primes, is_truncatable_prime


final_list = []
maybe_t_primes = create_t_primes()
for p in maybe_t_primes:
    t1 = is_truncatable_prime(p)
    t2 = is_truncatable_prime(p, False)
    if t1[0] and t2[0]:
        final_list.append(p)
print(final_list)
print("and the sum:", sum(final_list))
