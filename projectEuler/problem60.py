
from prime_checker import prime_check
from prime_generator import gen_indefinite


def concatenate(prime, primes):
    output = []
    for i in primes:
        output.append(int(str(prime)+str(i)))
        output.append(int(str(i)+str(prime)))
    return output


p = gen_indefinite()
ps = [3, 7]
while True:
    val = next(p)
    to_check = concatenate(val, ps)
    print("val:", val)
    if all([prime_check(j)[0] for j in to_check]):
        print("found it:", val)
        break


