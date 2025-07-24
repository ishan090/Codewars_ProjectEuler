

def next_bigger(n):
    n = str(n)
    for i in range(len(n)-2, -1, -1):
        if n[i] < max(n[i+1:]):
            print("index", i, "relating to", n[i], "selected")
            r = best_match(i, n)
            print("best match found to be", r, n[r])
            sorted_rest = "".join(sorted(n[i:r] + n[r+1:]))
            n = n[:i] + n[r] + sorted_rest
            return int(n)
        else:
            print("index", i, "relating to", n[i], "not selected")
    return -1


def best_match(i, n):
    best, best_index = 10, i
    print("\trange being considered", [*range(i+1, len(n))])
    print("value of n[i]", n[i])
    for r in range(i+1, len(n)):
        print("\tindex", r, n[r])
        if int(n[i]) < int(n[r]) and int(n[r]) < best:
            print("\t\tpasses the test", n[r])
            best = n[r]
            best_index = r
        else:
            print("\t\t", n[r], "fails the test")
    return best_index


print(next_bigger(1234567890))

