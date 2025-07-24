# Lexicographic Permutations
# Are permutations of the digits of a number arranged in an alpha-numeric order

# What is the millionth permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9?

from math import factorial as f

def greedy_factorials(n, i):
    """
    Tries to obtain the number n from multiples of factorials of numbers i and below
    E.g., 1000 = 6! + 2*5! + 4! + 2*3! + 2*2!
    """
    x = n
    facts = {}
    while x != 0:
        if x < f(i):
            i -= 1
            continue
        mult = x // f(i)
        facts[i] = mult
        x %= f(i)
        i -= 1
    return facts


# print(greedy_factorials(999, 6))

def lexo_next(n):
    """
    Given a lexographic permutation, finds the next one. Skips duplicates. 
    """
    perm = str(n)
    length = len(perm)
    # print(length)
    if length == 1:
        return None
    # print("length of the number is greater than 1. noice")
    digits = {}
    for i in str(n):
        digits[i] = digits.get(i, 0) + 1
    digits_sorted = sorted(digits.keys())
    # print("it has the following digits:", digits_sorted)
    new_perm = None
    # Find the next digit from the ones place which is smaller than the last
    # print("going through its digits one at a time now...")
    change = False
    for depth in range(2, len(perm)+1):
        for j in range(len(perm)-1, length-depth, -1):
            for i in range(j, length-1-depth, -1):
                # print("digit", perm[i])
                if perm[i] < perm[j]:
                    new_perm = perm[:i] + perm[j] + "".join(sorted(perm[i:j] + perm[j+1:]))
                    change = True
                    2341
                    break
            if change:
                break
        if change:
            break
    if not change:
        return None
    return new_perm



# start = 1234
# while start is not None:
#     print("next perm:")
#     start = lexo_next(start)
#     if start is not None:
#         start = int(start)
#         print(start)


def lexo_solve_brute(perm_index):
    index = 1
    initial = "0123456789"
    while index != perm_index:
        print(initial)
        initial = lexo_next(initial)
        index += 1
    return initial

def lexo_solve_greedy(perm_index, digits):
    greed_results = greedy_factorials(perm_index, len(digits))
    scope = list(greed_results.keys())[0]

    untouched = "".join([str(i) for i in digits[:len(digits)-scope]])
    print(untouched)
    concerned = digits[len(digits)-scope:]
    end = ""
    for i in greed_results:
        end += str(concerned[greed_results[i]-1])
        del concerned[greed_results[i]-1]
    for r in concerned:
        end += str(r)
    return untouched + end


print(lexo_solve_greedy(10, [*range(0, 10)]))

