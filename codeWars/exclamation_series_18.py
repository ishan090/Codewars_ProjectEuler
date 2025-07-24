from re import search as f


codes = {r'\1\1\1': 1000, r'\1\1': 800, r'\1(.)\2|([!?])\3([!?])\4\4': 500, r'\1': 300, r'.{1,3}([!?])\2': 200, r'': 100}

d = {"!": "1", "?": "0"}
s = "?!??!"

for code in codes:
    if f(r'(.)\1'+code, s):
        print(codes[code])
        break
