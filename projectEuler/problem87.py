

from math import pow
from problem60 import AllPrimes


class Memo():
    def __init__(self):
        self.memos = [{}, {}]
    
    def get(self, power, val):
        """
        returns the maximum recorded val for power-1 given a `val` for `power`
        """
        if val not in self.memos[power-2]:
            self.memos[power-2][val] = self.memos[power-2].get(val-1, 1)
        return self.memos[power-2][val]
    
    def update(self, power, val, uptil):
        self.memos[power-2][val] = uptil


def nextDiff(vals):
    out = [int(pow(p_s.val(vals[i]+1), i+2) - pow(p_s.val(vals[i]), i+2)) for i in range(len(vals))]
    return out

def 


def main():
    initial = [1, 1, 1]
    vals = 
    nexts = nextDiff(initial)






if __name__ == "__main__":
    p_s = AllPrimes(exclude=None)

    print(nextDiff([1, 1, 1]))



