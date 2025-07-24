# If the numbers from 1 to 5 are written out in words:
# one, two, three, four, five, then there are 19 letters used in total.

# How many letters used for numbers from 1 to 1000
# Three digit numbers may use the word "and" if there are numbers present
# in the tens and units place.
# E.g., 145 = one hundred and forty-five (hyphen and spaces are excluded)


basic_map = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8
}
tens_map = {
    2: 6,
    3: 6,
    4: 5,
    5: 5,
    6: 5,
    7: 7,
    8: 6,
    9: 6
}
hund = 7
thou = 8

def letters_in_num(num):
    num = str(num)
    total = len(num)
    and_prereq = False
    and_required = False
    letters = 0
    for i in range(total):
        digit = int(num[i])
        if digit == 0:
            continue
        place = total - i
        if place == 4:
            letters += basic_map[digit] + thou
            and_prereq = True
        elif place == 3:
            letters += basic_map[digit] + hund
            and_prereq = True
        elif place == 2:
            if and_prereq:
                and_required = True
            if digit == 1:
                letters += basic_map[int(num[i:])]
                break
            else:
                letters += tens_map[digit]
        elif place == 1:
            if and_prereq:
                and_required = True
            letters += basic_map[digit]
    if and_required:
        letters += 3
    if letters == 0:
        letters = 4   # the number was likely a chain of zeros
    return letters


def number_letter_sum_till(n):
    letters = 0
    for i in range(1, n+1):
        letters += letters_in_num(i)
    return letters


if __name__ == "__main__":
    print(letters_in_num(1000))
    print(number_letter_sum_till(1000))