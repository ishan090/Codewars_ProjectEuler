from math import pow as p, log, ceil

def last_digit(lst, base=None):
    if not lst:
        return 1
    # print("going to solve:", recur_print(lst))
    if base is None:
        base = 10
    # print("base:", base)
    print(lst[0]%base)
    if not lst or lst == [0, 0]:
        # print("here1")
        return 1
    elif len(lst) == 1:
        # print("here2")
        return lst[0]%base
    c, zeroing = cycle_size(lst[0]%base, base)
    if zeroing is not None:
        # print("zeroing not none", zeroing)
        # print("result from less than")
        if less_than(lst[1:], zeroing):
            # print("in fact", lst[1:], "<", zeroing)
            return int(y(lst))%base
        return 0
    r = last_digit(lst[1:], c)
    if lst[1] != 0 and r == 0:
        r += c
    # print("\toutput from recursion:", r)
    return p(lst[0]%base, r) % base

y = lambda x: x[0] ** y(x[1:]) if len(x) > 1 else x[0]
print(y([2, 2, 1]))

def recur_print(lst):
    if not len(lst):
        return None
    elif len(lst) == 1:
        return str(lst[0])
    else:
        return f"({lst[0]} ^ {recur_print(lst[1:])})"

def zero_check(lst):
    if len(lst) == 1:
        return lst[0] == 0
    elif lst[0] != 0:
        return False
    return not zero_check(lst[1:])

# print(zero_check([0, 0, 34]))
def less_than(lst, n):
    """    
    Tries to determine whether the expansion of lst is less than n     
    """
    # print("here's what came", lst, n)
    assert lst
    if len(lst) == 1:
        return lst[0] < n
    elif lst[0] >= n:
        if zero_check(lst[1:]):
            return 1 < n
        return False
    elif lst[0] == 0:
        if zero_check(lst[1:]):
            return 1 < n
        return True
    elif lst[0] == 1:
        return 1 < n
    return less_than(lst[1:], ceil(log(n)/log(lst[0])))



def cycle_size(num, base):
    """
    Returns the size of the cycle for the num ^ x (mod base) where num is already
    the residue of the class
    """
    num = num % base
    begin = num
    size = 1
    for i in range(2, base+1):
        if int(p(num, i))%base == 0:
            return size, i
        if int(p(num, i))%base == begin:
            return size, None
        size += 1
    return size, None



# test_data = [
#             ([], 1),
#             ([0, 0], 1),
#             ([0, 0, 0], 0),
#             ([1, 2], 1),
#             ([3, 4, 5], 1),
#             ([4, 3, 6], 4),
#             ([7, 6, 21], 1),
#             ([12, 30, 21], 6),
#             ([2, 2, 2, 0], 4),
#             ([937640, 767456, 981242], 0),
#             ([123232, 694022, 140249], 6),
#             ([499942, 898102, 846073], 6)
#         ]
# for d in test_data:
#     print("last digit of", d[0])
#     print(last_digit(d[0]))
#     print("\tshould be", d[1])
print(last_digit([2]*3, 100000))

