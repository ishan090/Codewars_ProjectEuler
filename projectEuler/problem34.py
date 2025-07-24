
# "145 is a curious number as 1! + 4! + 5! = 145"
# Find the sum of all such numbers whose sum is equal to 


# CASE BY CASE Analysis:
# Single digits aren't sums, so they are out
# two digits numbers must be composed of digits from [1, 2, 3, 4] as 5! = 120 > 100
# three digit numbers could include 1 through 6
# 4 -> 1 through 7
# 5 -> 1 to 8
# 6 -> 1 to 9
# 7 -> 1 through 9, but must have atleast 3 9s. Highest 7 digit num: 2540160
# That's it.


def are_permutations(a, b):
    a, b = str(a), str(b)
    assert len(a) == len(b), "If the length isn't the same, then they're\
        obviously not the same number!"
    dict1 = {}
    dict2 = {}
    for i in range(len(a)):
        dict1[a[i]] = dict1.get(a[i], 0) + 1
        dict2[b[i]] = dict2.get(b[i], 0) + 1
    return dict1 == dict2


def main():
    pass



print(are_permutations(5353, 5533))
