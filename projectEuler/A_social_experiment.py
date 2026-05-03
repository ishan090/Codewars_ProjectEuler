


cases = int(input())

vals = []
for i in range(cases):
    val = int(input())
    vals.append(val)

out = []
for v in vals:
    if v <= 3:
        print(2)
    elif v % 2 == 0:
        print(0)
    elif v % 3 == 0:
        print(0)
    else:
        print(1)

