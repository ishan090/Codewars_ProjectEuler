

class Node:
    def __init__(self, index, canGetTo=None):
        self.index = index
        if canGetTo is None:
            canGetTo = []
        self.next_nodes = canGetTo
    
    def canGo(self, here):
        self.next_nodes.append(here)
    
    def canGoWhere(self):
        return self.next_nodes
    
    def __eq__(self, other):
        return self.index == other.index
    
    def __repr__(self):
        return str(self.index)
    def __str__(self):
        return str(self.index)
    
    def inside(self, l):
        for node in l:
            if node == self:
                return True
        return False


def create_nodes(size):
    """
    Creates nodes according to the param `size` (rows, cols)
    """
    print("size found to be:", size)
    nodes = []
    for i in range(size[0]):
        # print("val i", i)
        nodes.append([])
        for j in range(size[1]):
            # print("val j", j)
            nodes[i].append(Node((i, j)))
    # print("size of nodes:", (len(nodes), len(nodes[0])))
    return nodes

def getSize(grid):
    return int((len(grid)-1)/2), int((len(grid[0])-1)/3)


def parse(grid, nodes):
    """
    Assumes grid to be a list of strings. With each element representing a row
    Parses a grid of ascii by finding edges and then adding them to the nodes
    Assumes the grid to be `neat`
    """
    # print("grid in", grid, len(grid), len(grid[0]))
    num_rows = int((len(grid)-1)/2)
    num_cols = int((len(grid[0])-1)/3)
    # print("numrows, numcols", num_rows, num_cols)
    for row in range(1, num_rows+1):
        for col in range(1, num_cols):
            # print("index", (row, col))
            # print("row val", grid[row*2-1][col*3])
            if grid[row*2-1][col*3] != "|":
                n1 = (row-1, col)
                n2 = (row-1, col-1)
                nodes[n1[0]][n1[1]].canGo(nodes[n2[0]][n2[1]])
                nodes[n2[0]][n2[1]].canGo(nodes[n1[0]][n1[1]])
                

    # print([*range(1, num_cols+1)])
    for col in range(1, num_cols+1):
        for row in range(1, num_rows):
            # print("index", (row, col))
            # print("col val", grid[row*2][col*3-2:col*3])
            if grid[row*2][col*3-2:col*3] != "--":
                n1 = (row, col-1)
                n2 = (row-1, col-1)
                nodes[n1[0]][n1[1]].canGo(nodes[n2[0]][n2[1]])
                nodes[n2[0]][n2[1]].canGo(nodes[n1[0]][n1[1]])
    return nodes


def main(nodes):
    all_nodes = [val for row in nodes for val in row]
    groups = {}
    while len(all_nodes) != 0:
        print(len(all_nodes), "nodes to go...")
        start = all_nodes.pop()
        frontier = [start]
        explored = []
        chain_len = 0
        while len(frontier) > 0:
            elem = frontier.pop()
            explored.append(elem)
            print("nodes explored:", len(explored), "frontier has", len(frontier))
            chain_len += 1
            for node in elem.canGoWhere():
                if not node.inside(explored) and not node.inside(frontier):
                    frontier.append(node)
        print("broke out!")
        groups[chain_len] = groups.get(chain_len, 0) + 1
        for n in explored[1:]:
            del all_nodes[all_nodes.index(n)]
        print("deletions done")
    return sorted([(key, val) for key, val in groups.items()], key=lambda x: x[0], reverse=True)


x = x.split("\n")
ns = create_nodes(getSize(x))
# print("here are the nodes", ns)
n = parse(x, ns)
print("parsing done", (len(n), len(n[0])), "nodes")
# for row in n:
#     for node in row:
#         print(node, "can get to", node.next_nodes)
print(main(n))
