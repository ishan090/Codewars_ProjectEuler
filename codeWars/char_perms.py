
def permutations(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    first = list(sorted_freq.keys())[0]
    total = first*sorted_freq[first]
    del sorted_freq[first]
    str_dict = "".join([str(i*sorted_freq[i]) for i in sorted_freq])
    for i in str_dict:
        total = add_all(i, total, sorted_freq[i] > 1)
    return total


def handle_all_duplicates(char, s):
    total = []
    for i in s:
        to_add = add_one(char, i)
        for i in to_add:
            if i not in total:
                total.append(i)
    return total


def add_all(char, s, duplicate=None):
    total = []
    if duplicate:
        return handle_all_duplicates(char, s)
    for i in s:
        to_add = add_one(char, i)
        total.extend(to_add)
    return total

def add_one(char, s):
    new = []
    for i in range(0, len(s)+1):
        new.append(s[:i] + char + s[i:])
    return new

print(permutations("1223"))
