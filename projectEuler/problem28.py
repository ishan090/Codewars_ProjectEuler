
from arithmetic_series import *


def spiral_sum(n):
    """
    Given the dimension of an n by n spiral, finds the sum of all the
    elements that lie on the diagonals    
    """
    total = 1
    depth = int((n-1)/2)
    common_diff = 2
    first = 1 + common_diff
    for layer in range(depth):
        total += sum_n(4, first, common_diff)
        first = nth_elem(4, first, common_diff)
        print("new first is:", first)
        common_diff += 2
        first += common_diff
    return total

print(spiral_sum(1001))


