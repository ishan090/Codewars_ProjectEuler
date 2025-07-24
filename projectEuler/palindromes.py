
# from number_systems import NumberSystem
# Related to palindromes

def is_palindrome(text):
    assert text, "Text must have non-zero length"
    # print("text received:", text)
    branch_len = (len(text) + 1) // 2
    # print("branch len:", branch_len)
    for i in range(0, branch_len):
        # print("i", i)
        if text[i] != text[-1-i]:
            return False
    return True


def make_palindrome(branch, odd=None):
    """
    Given a branch, makes a palindrome of an odd or even length    
    """
    if odd is None:
        odd = True
    else:
        odd = False
    out = branch
    if odd:
        out += reversed(branch[:-1])
    else:
        out += reversed(branch)
    return out

# print(make_palindrome([1, 2, 3, 4]))

