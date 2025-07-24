
def solve_runes(expr):
    result = expr[expr.index("=")+1:]
    for i in ["+", "*", "-"]:
        if i in expr:
            operator = i
            break
    if operator == "-" and expr[0] == "-":
        ind = expr[1:].index(operator)+1
    else:
        ind = expr.index(operator)
    num1 = expr[:ind]
    num2 = expr[ind+1:expr.index("=")]

    operations = {
        "+": lambda a, b: a+b,
        "-": lambda a, b: a-b,
        "*": lambda a, b: a*b
        }

    nums = []
    for i in range(0, 10):
        if not str(i) in expr:
            nums.append(str(i))

    for n in nums:
        n1 = num1.replace("?", n)
        n2 = num2.replace("?", n)
        n3 = result.replace("?", n)
        if any([ (i[0] == "0" and i != "0") or (i[0]=="-" and i[1] == "0" and i != "0") for i in [n1, n2, n3]]):
            continue
        if
        if operations[operator](int(n1), int(n2)) == int(n3):
            return int(n)
    return -1


print(parse("-5?*-1=5?"))





