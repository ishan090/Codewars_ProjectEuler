

def stepwise_digit(n):
    limit = 9
    mult = 1
    steps = 0
    while n > 0:
        if n == mult * limit:
            digit = mult
            n -= mult * limit
            steps += limit
            limit *= 10
            mult += 1
            break
        elif n > mult * limit:
            n -= mult * limit
            steps += limit
            limit *= 10
            mult += 1
        else:
            closest = n // mult
            if n < mult:
                closest = 1
            steps += closest
            rem = n % mult
            digit = rem
            if rem == 0:
                digit = mult
            n -= closest + digit
            break
    return steps, digit


prod = 1
for i in [1, 10, 100, 1000, 1e4, 1e5, 1e6]:
    result = stepwise_digit(int(i))
    d = int(str(result[0])[result[1]-1])
    print(f"d-{i} is {d}")
    prod *= d
print("product of the digits:", prod)
        

