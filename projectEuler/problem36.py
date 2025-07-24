# Related to palindromes in two bases

from palindromes import make_palindrome, is_palindrome
from number_systems import NumberSystem

total = 0
num = NumberSystem([1], 10)
until = NumberSystem([1, 0, 0, 0], 10)
while num < until:
    digits1 = make_palindrome(num.getDigits())
    digits2 = make_palindrome(num.getDigits(), False)
    # print(digits1, digits2)
    for i in [digits1, digits2]:
        to_test = NumberSystem(i, 10).convertToBase(2)
        # print("checking:", to_test.inBase10())
        if is_palindrome(to_test.getDigits()):
            # print("palindrome")
            total += to_test.inBase10()
    num = num.increment()
print(total)
