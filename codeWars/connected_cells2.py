# A more efficient way of doing the same


grid = """\
+--+--+--+
|        |
+  +  +  +
|        |
+--+--+--+"""
grid = grid.split("\n")

def actions(state, g):
    pass


groups = {}
all_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[1]))]
while all_pos:
    start = all_pos.pop()
    chain_len = 0
    frontier = set(start)
    explored = set()
    while frontier:
        state = frontier.pop()


