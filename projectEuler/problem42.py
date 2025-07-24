
import json
from triangular import check_triangular

with open("0042_words.json", "r") as f:
    data = json.load(f)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value_map = {alphabet[i]:i+1 for i in range(len(alphabet))}
print(value_map)

def word_value(word):
    val = 0
    for char in word:
        val += value_map[char]
    return val

total = 0
for w in data:
    v = word_value(w)
    if check_triangular(v)[0]:
        total += 1
print("total number of triangular words:", total)

