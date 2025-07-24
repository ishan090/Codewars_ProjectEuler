
# Solve the 33rd problem: objective is to find fractions less than one (with
# two digits each in the numerator and denominator) that have this unique property
# of being equalling to the remaining fraction obtained after crossing out common numbers

# E.g., 49/98 = 4/8 (9 got crossed out)

def gen_pairs(n):
    for i in range(11, n):
        for j in range(11, i):
            if i % 10 == 0 or j % 10 == 0:
                continue
            yield (j, i)


def has_common(pair):
    p1, p2 = str(pair[0]), str(pair[1])
    for i in p1:
        if i in p2:
            i1 = p1.index(i)
            i2 = p2.index(i)
            p1 = p1[:i1] + p1[i1+1:]
            p2 = p2[:i2] + p2[i2+1:]
            out = (p1, p2)
            # return out
            return (int(out[0]), int(out[1]))
    return False


def ratio(pair):
    try:
        return pair[0]/pair[1]
    except ZeroDivisionError:
        return 2

print(has_common((35, 58)))

# saved_pairs = []
for pair in gen_pairs(100):
    pair_check = has_common(pair)
    if pair_check:
        if ratio(pair_check) == ratio(pair):
            print("Found one:", pair, pair_check)
            # saved_pairs.append(saved_pairs)


