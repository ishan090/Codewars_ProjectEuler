# Related to pandigital multiple



def no_same(*args):
    individual_lengths = 0
    empty = set()
    for arg in args:
        individual_lengths += len(arg)
        empty = empty | set(arg)
    return len(empty) == individual_lengths

def num_unique(num):
    num = str(num)
    if "0" in num:
        return False
    unique = []
    for digit in num:
        if digit not in unique:
            unique.append(digit)
    return len(unique)


def try_pandigital(num):
    digits_left = 9
    multiples = []
    i = 1
    mult = str(i * num)
    while digits_left > 0:
        mult = str(i * num)
        if len(mult) <= digits_left:
            multiples.append(mult)
            digits_left -= len(mult)
        else:
            return False
        i += 1
    return multiples

print(try_pandigital(9))

print(no_same("123", "456"))

x = 1
best = x
while x < 10000:
    mults = try_pandigital(x)
    print(mults)
    if not mults:
        x += 1
        continue
    concatenated = "".join(mults)
    print(num_unique(concatenated), "concatenated unique")
    if num_unique(concatenated) == 9:
        print(mults)
        best = x
    x += 1
print(best)

# print(9352, 9352*2)