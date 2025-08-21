# Okay, this is going to be a hard one. But let's get this nevertheless

# Objective is to find the lowest such number (part of) whose digits can be replaced by
# 8 different digits, all producing primes.

# e.g., the 0's in 56003 can be replaced by 1, 3, 4, 6, 7, 9 resulting in a 7-prime family
# Only, in this case, the task is to find an 8 prime family

# Notes: Actually, this was solved quite easily, noice

from prime_generator import gen_indefinite, gen_primes_from
from prime_checker import prime_check


def combinations(f, size=3, r=1):
    """given a list, outputs the various possible combinations of size `size`"""
    # print("recursion", r, "f and size:", f, size)
    if size == 0:
        return [[]]
    if len(f) == size:
        return [f]
    else:
        out = []
        for next_val in range(len(f)-size+1):
            new_f = f[next_val+1:]
            # print("\tlooking at new_f:", new_f, "with val:", f[next_val])
            blah = combinations(new_f, size=size-1, r=r+1)
            # print("\toutput of combs:", blah)
            for other in blah:
                # print("\comb is:", other)
                out += [[f[next_val]] + other]
                # print("new out:", out)
        return out


# print("combs:", combinations([1, 2, 3, 4], 3))


def repeats(num, size=3):
    num = str(num)
    freq = {}
    conf = []
    for i in range(len(num)-1):
        freq[num[i]] = freq.get(num[i], []) + [i]
    for num, f in freq.items():
        if len(f) >= size:
            conf += combinations(f, size)
    return conf


def bin_search(item, items):
    """tries to find itme in items. returns bool"""
    start = 0
    end = len(items)-1
    while start < end:
        mid = (start + end) // 2
        if items[mid] == item:
            return True, mid
        elif item > items[mid]:
            start = mid + 1
        else:
            end = mid
    if start == len(items)-1 and item > items[start]:
        start += 1
    return False, start


print(bin_search(80, [1, 2, 5, 7, 10, 45, 56, 75]))
def replace_indicies(num, indicies, digit):
    """replaces certain indicies with `digit`"""
    out = list(str(num))
    digit = str(digit)
    for i in indicies:
        out[i] = digit
    return int("".join(out))



def prime_family(family_size, repeat_size=3):
    checked = []
    prime = gen_indefinite()
    val = 0
    progress = 0
    while val < 1111:
        val = next(prime)
    for val in prime:
        locate = bin_search(val, checked)
        if locate[0]:   # skip if already explored
            checked.pop(locate[1])
            continue
        for repeat in repeats(val, repeat_size):
            family = [val]
            start_digit = int(str(val)[repeat[0]])
            if start_digit > 9 - family_size + 1:
                continue
            crosses = 10 - family_size - start_digit
            # print("crosses available for digit", start_digit, ":", crosses)
            crossed = False
            for digit in range(start_digit+1, 10):
                check = replace_indicies(val, repeat, digit)
                if not prime_check(check)[0]:
                    crosses -= 1
                    if crosses < 0:
                        crossed = True
                elif crossed:
                    locate = bin_search(check, checked)[1]
                    checked = checked[:locate] + [check] + checked[locate:]
                else:
                    family.append(check)
            if crossed:
                family = []
                continue
            return val, family
        if val // 100000 > progress:
            print("explored primes till:", val)
            progress += 1

    print("OVER")

print(prime_family(8, 3))

