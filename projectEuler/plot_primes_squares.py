
# Package imports
import matplotlib.pyplot as plt

# Relative imports
from prime_generator import gen_n_primes as primes
from prime_generator import list_n_primes


def primes_diffs(n):
    """
    The first n differences between primes    
    """
    first = True
    prev_val = 0
    diffs = []
    for new_prime in primes(n+1):
        # print("newprime is", new_prime)
        if first:
            first = False
            prev_val = new_prime
            continue
        diffs.append(new_prime - prev_val)
        prev_val = new_prime
    return diffs


def square_diffs(n):
    prev = 1
    diffs = []
    for i in range(2, n+2):
        diffs.append(i*i - prev)
        prev = i*i
    return diffs


nums = 10000
y1 = primes_diffs(nums)
print("Done!")
# y2 = square_diffs(nums)
# print(len(y2))
x = [*range(1, nums+1)]

plt.scatter(x, y1, label="prime diffs", color="red")
# plt.plot(x, y2, label="square diffs", color="blue")

plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Plotting of differences of primes and squares')
plt.show()
