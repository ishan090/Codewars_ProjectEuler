

def sum_strings(x, y):
    if x != "0":
        x = x.lstrip("0")
    if y != "0":
        y = y.lstrip("0")
    l_x, l_y = len(x), len(y)
    till = -min(len(x), len(y))
    z = -1
    carry = 0
    out = ""
    for z in range(-1, till-1, -1):
        carry = int(x[z]) + int(y[z]) + carry
        out = str(carry % 10) + out
        carry = carry // 10
    if l_x > l_y:
        greater = x
        smaller = y
    else:
        greater = y
        smaller = x
    for z in range(till-1, -len(greater), -1):
        carry = int(greater[z]) + carry
        out = str(carry % 10) + out
        carry = carry // 10
        if carry == 0:
            out = greater[:z] + out
            break
    # print(carry)
    if str(carry) != str(0):
        out = str(carry) + out
    if out == "":
        return "0"
    return out




a = "124879423984632"
b = "8798962349326"
print(sum_strings(a, b))

