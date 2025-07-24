# A perfect number is a number for which the sum of its proper divisors is exactly equal
# to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28,  which means that 28 is a perfect number.

# Now, 12 is the first abundant number with the sum of its factors equalling 16
# Apparently, by mathematical analysis it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.

from prime_factorization import all_factors as factors
from prime_factorization import quick_factors
import pandas as pd




abundant = []
odd_abundant = []
perfect = []
deficient = []
for i in range(1, 28123):
    factor_sum = sum(factors(i))
    if factor_sum == i:
        perfect.append(i)
    elif factor_sum > i:
        abundant.append((i, factor_sum))
        if i % 2 == 1:
            odd_abundant.append((i, factor_sum, quick_factors(i), factors(i)))
    else:
        deficient.append((i, factor_sum))

df=pd.DataFrame(odd_abundant)
df.to_csv('output_file.csv', index=False,header="Abundant Numbers")

