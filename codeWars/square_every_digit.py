def square_digits(num):
    num = str(num)
    out = ""
    for i in num:
        out += str(int(i)*int(i))
    return int(out)


def clean(num):
    while num % 10 == 0:
        num = num // 10
    return square_digits(num)


print(100, clean(100))
