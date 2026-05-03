

# IMPORTS
import random
from binary_search import closest
from math import ceil



def load_matrix(matrix_path):
    with open(matrix_path) as file:
        data = file.read()
    matrix = [[int(c) for c in row.split(",")] for row in data.splitlines()]
    return matrix


# LOAD
MATRIX = load_matrix("problem81_matrix.txt")
print(MATRIX)
NUM_ROWS = len(MATRIX)
NUM_COLS = len(MATRIX[0])



def mean(matrix):
    rows = 0
    for row in matrix:
        rows += sum(row)
    return rows / len(matrix) / len(matrix[0])


class Marker():
    def __init__(self, index, previous=None, cost=None):
        """
        assumes previous is in the reversed order. i.e., most recent cells first
        """
        # print("this is index:", index)
        if previous == None:
            previous = []
        if cost == None:
            cost = sum([MATRIX[i][j] for i, j in previous]) + MATRIX[index[0]][index[1]]
        self.previous = previous
        self.cost = cost
        self.index = index
        self.steps = len(self.previous) + 1
        self.mean = self.cost / self.steps
    
    def history(self):
        return self.previous + [self.index]
    
    def getCost(self):
        return self.cost
    
    def getMean(self):
        return self.mean
    
    def eval(self):
        return self.getMean()


class Frontier():
    def __init__(self):
        self.frontier = []
    
    def new_element(self, elem: Marker):
        if len(self.frontier) == 0:
            self.frontier = [elem]
        costs = [item.eval() for item in self.frontier]
        i = closest(costs, elem.eval())
        self.frontier = self.frontier[:i] + [elem] + self.frontier[i:]
    
    def remove(self):
        if random.random() < 0.1:
            return self.frontier.pop(random.randint(0, len(self)-1))
        return self.frontier.pop(0)
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.frontier)


def getActions(state, end_index=(NUM_ROWS-1, NUM_COLS-1)):
    i, j = state.index
    out = []
    if i < end_index[0]:
        out.append((i+1, j))
    if j < end_index[1]:
        out.append((i, j+1))
    return out

def revActions(state, end_index=(0, 0)):
    i, j = state.index
    out = []
    if i > end_index[0]:
        out.append((i-1, j))
    if j > end_index[1]:
        out.append((i, j-1))
    return out

def rev3way(state):
    i, j = state.index
    out = []
    if j > 0:
        out.append((i, j-1))

    if i < NUM_ROWS-1:
        out.append((i+1, j))

    if i > 0:
        out.append((i-1, j))

    
    return out

def actionAny(state, vectors):
    ind = state.index
    out = []
    for v in vectors:
        new = [ind[i] + v[i] for i in range(len(ind))]
        if 0 <= new[0] <= NUM_ROWS-1 and 0 <= new[1] <= NUM_COLS-1:
            out.append(new)
    return out


def search(initial, final, actionFunction):
    initial = Marker(initial)
    front = Frontier()
    front.new_element(initial)
    max_steps = 0

    print("Searching routes from", initial.index, "to", final)

    while not front.isEmpty():
        
        # print(len(front))


        state = front.remove()

        if state.index == final:
            return state
        if state.steps > max_steps:
            max_steps = state.steps
            # print("Max Steps:", max_steps, "Front len", len(front))

        actions = actionFunction(state, final)
        
        for act in actions:
            new_marker = Marker(act, state.history())
            front.new_element(new_marker)
    
    print("BLAHWAHAHA")


class Memo():
    def __init__(self, size: tuple):
        self.memo = [[0 for i in range(size[1])] for j in range(size[0])]
        # print("this is the size of the memo", (len(self.memo), len(self.memo[0])))
    
    def get(self, index, default):
        # print("trying to fetch index", index, "from", (len(self.memo), len(self.memo[0])))
        # print(len(self.memo), index[0])
        val = self.memo[index[0]][index[1]]
        if val == 0:
            return default
        return val
    
    def set(self, index, val):
        self.memo[index[0]][index[1]] = val
    
    def backtrack2way(self, index):
        return revActions(Marker(index))
    
    def backtrack3way(self, index):
        return rev3way(Marker(index))


class States_Memo(Memo):
    def __init__(self, size: tuple):
        self.memo = [[0 for i in range(size[1])] for j in range(size[0])]
    
    def get(self, index, default):

        val = self.memo[index[0]][index[1]]

        # for i in self.memo:
        #     print(i)

        # print("here's the output of get", val, "on index", index)
        if val == 0:
            return default
        return val


def dynamic2way(final):
    
    result = memo.get(final, None)
    if result is not None:
        return result
    else:
        prevs = memo.backtrack2way(final)
        min_index = None
        prev_best = None
        for prev in prevs:
            val = dynamic2way(prev)
            if prev_best is None or val < prev_best:
                min_index = prev
                prev_best = val
        
        calculated = prev_best + MATRIX[final[0]][final[1]]
        memo.set(final, calculated)
        states.set(final, Marker(final, states.get(min_index, None).history()))
        return calculated


def dynamic3way(final, previous=None):
    """
    The rules for this one:
    start anywhere in the first column, end anywhere in the last

    The entire first column shall be fed into the memo in the beginning
    Backtracking will start from each of the elements of the last row separately.
    """

    if previous is None:
        previous = tuple()
    previous += (final,)

    result = memo.get(final, None)
    if result is not None:
        # print("\tsolved")
        return result
    else:
        prevs = memo.backtrack3way(final)
        min_index = None
        prev_best = 0
        # print("no data on", final, "so looking at", prevs)
        # print("\tconsidering previous:", previous)
        for prev in prevs:
            if prev in previous:
                # print("\talready explored", prev)
                continue
            # print("\t", prev)
            val = dynamic3way(prev, previous)
            if prev_best == 0 or val < prev_best:
                min_index = prev
                prev_best = val
        # print("after looking through previous:", min_index, prev_best)
        
        calculated = prev_best + MATRIX[final[0]][final[1]]
        memo.set(final, calculated)
        states.set(final, Marker(final, states.get(min_index, None).history()))
        return calculated


def prep3way():
    finals = [(j, NUM_COLS-1) for j in range(NUM_ROWS)]

    

    least = None
    best_state = None
    for final in finals:
        global memo, states
        
        memo = Memo((NUM_ROWS, NUM_COLS))
        states = States_Memo((NUM_ROWS, NUM_COLS))

        # print("here are the already known values:")
        # for j in range(NUM_ROWS):
        #     print((j, 0), memo.get((j, 0), None))
        for elem in [(j, 0) for j in range(NUM_ROWS)]:
            memo.set(elem, MATRIX[elem[0]][elem[1]])
            states.set(elem, Marker(elem))
        print("trying: goal:", final)
        val = dynamic3way(final)
        print("\tval:", val)
        s = states.get(final, None).history()
        if least is None or val < least:
            least = val
            best_state = s

    return least, best_state


def split_search(initial, final):
    
    target_steps = ceil((abs(initial[0] - final[0]) + abs(initial[1] - final[1])) / 2)
    sub_targets = [(i, target_steps - i) for i in range(target_steps + 1)]

    best_normal = [search(initial, target, getActions) for target in sub_targets]
    best_reversed = [search(final, target, revActions) for target in sub_targets]

    best = None
    index = None
    for t in range(len(sub_targets)):
        c = best_normal[t].getCost() + best_reversed[t].getCost()
        if best is None or best > c:
            best = c
            index = t
    size
    print("Solution found!")
    print(best_normal[t].history(), list(reversed(best_reversed[t].history())))


if __name__ == "__main__":

    # blah = split_search((0, 0), (NUM_ROWS-1, NUM_COLS-1))
    

    print(prep3way())
    # print(states.get((NUM_ROWS-1, NUM_COLS-1), None).history())
    # print(blah.history())
