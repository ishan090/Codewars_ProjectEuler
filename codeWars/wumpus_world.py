
# Read more about it here:
# https://www.codewars.com/kata/625c70f8a071210030c8e22a/train/python

class Cell:
    def __init__(self, index, val, pos):
        self.index = index
        self.val = val
        self.pos = pos

def wumpus_world(cave):
    grid = {}
    for i in range(4):
        for j in range(4):
            grid[(i, j)] = Cell((i, j), None, "GWP")
    G, W, P = [list(grid.keys())]*3

    


