from time import sleep

class Map:

    change_dir = {
        "right": "down",
        "down": "left",
        "left": "up",
        "up": "right"
        }

    dir_coord = {
        "down": lambda x: (x[0]+1, x[1]),
        "left": lambda x: (x[0], x[1]-1),
        "up": lambda x: (x[0]-1, x[1]),
        "right": lambda x: (x[0], x[1]+1)
        }

    def __init__(self, size):
        self.size = size
        self.grid = self.init_grid(size)

    def init_grid(self, size):
        grid = [["0"]*size for i in range(size)]
        return grid

    def inside_grid(self, coord):
        if coord[0] < 0 or coord[1] < 0:
            return False
        return coord[0] < len(self.grid) and coord[1] < len(self.grid[0])

    def edit_grid(self, coord, val):
        self.grid[coord[0]][coord[1]] = val

    def grid_val(self, coord):
        return self.grid[coord[0]][coord[1]]

    def num_touches(self, coord):
        directions = list(self.dir_coord.keys())
        if coord[0] == 0:
            del directions[directions.index("up")]
        if coord[1] == 0:
            del directions[directions.index("left")]
        moves = [self.dir_coord[i](coord) for i in directions]
        ones = 0
        for move in moves:
            if self.inside_grid(move):
                if self.grid_val(move) == "1":
                    ones += 1
        return ones


    def start_spiral(self, start):
        val = "1"
        state = start
        self.edit_grid(state, val)
        print("\tstarting state at", state)
        print(self)
        # sleep(0.5)
        dir = list(self.change_dir.keys())[0]
        while True:
            move = self.get_move(state, dir)
            if move == 1:
                dir = self.change_dir[dir]
                continue
            elif move == 0:
                break # Game over
            self.edit_grid(move, val)
            print("move made at", move)
            print(self)
            state = move
            # sleep(0.5)
        return self.grid


    def get_move(self, state, dir):
        candidate = self.dir_coord[dir](state)
        print("testing", candidate)
        if not self.inside_grid(candidate):
            print("found to be outside the grid")
            return 1
        if self.grid_val(candidate) == "1":
            print("changed direction twice and error")
            return 0
        if self.num_touches(candidate) > 1:
            print("touches the spiral at another point")
            return 1
        return candidate

    def __str__(self):
        out = "\n".join(["".join(i) for i in self.grid])
        return out


m = Map(6)
print(m)
print(m.start_spiral((0, 0)))

