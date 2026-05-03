
# Relates to Composite numbers
from prime_generator import gen_indefinite, gen_n_primes

def composite_indefinite():
    x = 2
    for p in gen_indefinite():
        m = [i for i in range(x+1, p)]
        for composite in m:
            yield composite
        x = p

def composite_odd():
    for i in composite_indefinite():
        if i % 2 == 1:
            yield i


if __name__ == "__main__":
    # blah = composite_odd()
    # print(blah)
    out = []

    for p in gen_n_primes(10):
        out.append([2 * s*s + p for s in range(1, 11)])
    for row in out:
        print(row)
    


