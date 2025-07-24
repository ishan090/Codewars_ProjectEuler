
# Some quadratic equations of the form: n^2 + an + b produce a string
# of primes for consecutive values of n. What's the longest such string
# for |a| and |b| <= 1000.
from prime_generator import list_primes_uptil as primes_till
from prime_checker import prime_check_given_primes as prime_check

primes = primes_till(1000)

def check_quad_primes(a, b):
    until = b - a if a > 0 else b
    primes_streak = 0
    for n in range(0, until+1):
        x = n*n + a*n + b
        test = prime_check(x, primes)
        if test[0]:
            primes_streak += 1
        else:
            break
    return primes_streak


def perms_a_b(a, b):
    highscore = 0
    perm = ()
    for i in [-1, 1]:
        for j in [-1, 1]:
            x, y = a*i, b*j
            # print("Perm 1", x, y)
            score = check_quad_primes(x, y)
            test = check_quad_primes(x, y)
            if test > highscore:
                highscore = test
                perm = (x, y)
    return highscore, perm

longest_length = 0
pair = ()
for b in primes:
    for a in range(1, 1000, 2):
        best = perms_a_b(a, b)
        if best[0] > longest_length:
            print("New Record!", best)
            pair = best[1]
            longest_length = best[0]
print(pair, longest_length)


