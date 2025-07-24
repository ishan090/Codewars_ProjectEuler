
from math import floor, log10

def is_pandigital(n):
    """
    Checks if a number is pandigital
    """
    nums_set = set([int(i) for i in str(n)])
    # print(nums_set)
    num_digits = floor(log10(n)) + 1
    # print(num_digits)
    if len(nums_set) == num_digits and max(nums_set) == num_digits and 0 not in nums_set:
        return True
    return False


