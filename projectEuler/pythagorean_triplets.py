
from prettytable import PrettyTable
from math import sqrt

def list_triplets(x):
    triplets = []
    m = 2
    n = 1
    while len(triplets) + 1 <= x:
        triplets.append((m, n, 2*m*n, m*m - n*n, m*m + n*n))
        if n + 1 < m:
            n += 1
        else:
            m += 1
            n = 1
    return triplets


def test_triplet(a, b):
    if sqrt(a*a + b*b) % 1 == 0:
        return True
    return False



def brute_triplets(x):
    triplets = []
    a = 1
    b = 2
    while 2*b + 1 < x:
        if test_triplet(a, b):
            nums = [a, b, int(sqrt(a*a + b*b))]
            triplets.append(nums + [sum(nums)])
        if a + 1 < b:
            a += 1
        else:
            b += 1
            a = 1
    return triplets


trips = brute_triplets(1000)

table = PrettyTable()

table.field_names = ["a", "b", "c", "p"]
freq = {}

highest = 0
highest_val = 0
for i in range(len(trips)):
    table.add_row(trips[i])
    freq[trips[i][-1]] = freq.get(trips[i][-1], 0) + 1
    if freq[trips[i][-1]] > highest:
        highest = freq[trips[i][-1]]
        highest_val = trips[i][-1]

print(table)
print("most frequent perimenter is:", highest_val, "with", highest, "occurrences")



