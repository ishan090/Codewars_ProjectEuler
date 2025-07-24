
# Attempts to solve this puzzle:
# https://gamaverse.com/switch-the-bulb-game/

# Idea to use Nodes and graphs to reprepsent connections and then evaluate them
from copy import deepcopy 


class Node:
    def __init__(self, index, child=None):
        """
        Each child is just an index, it doesn't belong to the Node class
        """
        if child is None:
            child = []
        self.index = index
        self.child = child
    
    def addChild(self, c):
        assert c not in self.child, f"{c} is already inside self.child: {self.child}"
        self.child.append(c)
    
    def __eq__(self, other):
        return self.getIndex() == other.getIndex()
    
    def getChildren(self):
        return self.child[:]
    
    def getIndex(self):
        return self.index
    def __str__(self):
        return f"N({self.index[0]}, {self.index[1]})"
    def __repr__(self):
        return f"N({self.index[0]}, {self.index[1]})"


class Grid:
    def __init__(self, nodes: list):
        """
        nodes is a list of nodes. grid maps the index of the node to the node itself
        """
        n = {}
        for i in nodes:
            n[i.getIndex()] = i
        self.nodes = n
    
    def __len__(self):
        return len(self.nodes)
    
    def getNode(self, index):
        assert index in self.nodes, "Yo, this node isn't in the graph"
        return self.nodes[index]
    
    def allNodeIndicies(self):
        return list(self.nodes.keys())
    
    def allNodes(self):
        return list(self.nodes.values())
    
    def addChildToNode(self, index, child):
        i = self.getNode(index)
        i.addChild(child)
        self.nodes[index] = i
    
    def addNode(self, node):
        self.nodes[node.getIndex()] = node

    def __repr__(self):
        return str(list(self.nodes.values()))



def parse(grid):
    # Reformat the grid
    grid = grid.split("\n")
    # Stores the indicies of the bulbs here
    indicies = []
    # Find bulbs and store them
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "B":
                indicies.append((row, col))
    # indicies = [Node(i) for i in indicies]
    # g = Grid(indicies)
    # print(g)
    children = []
    nodes = []
    print("now finding children")
    for i in range(len(indicies)):
        children.append(findChildren(indicies[i], grid))
        nodes.append(Node(indicies[i], children[i]))
        print("found children", children[i])
        print("node of the same:", nodes[i])
    for node in nodes:
        print(node)
        print("\tchildren:", node.getChildren())
    g = Grid(nodes)
    # print(g)
    return g


def findChildAlong(row_ch, col_ch, index, grid):
    """
    Here grid is the list of rows (as strings)
    """
    r, c = index
    r, c = row_ch(r), col_ch(c)
    while grid[r][c] not in "+-|":
        if grid[r][c] == "B":
            return (r, c)
        r, c = row_ch(r), col_ch(c)
    return None


def findChildren(index, grid):
    """finds all the children of node: `index` in the `grid`"""
    print("finding children of", index, "in", "\n"+"\n".join(grid))
    children = []
    plus = lambda x: x+1
    minus = lambda x: x-1
    same = lambda x: x
    children = [findChildAlong(minus, i, index, grid) for i in [same, plus]]
    children += [findChildAlong(same, plus, index, grid)]
    children += [findChildAlong(plus, i, index, grid) for i in [plus, same, minus]]
    children += [findChildAlong(i, minus, index, grid) for i in [same, minus]]

    return [i for i in children if i is not None]


def valid_actions(g, state, chain):
    """
    Assumes chain includes state
    """
    return [i for i in g.getNode(state).getChildren() if i not in chain]


def solve(grid, state, goal, chain=None):
    if chain is None:
        chain = []
    chain.append(state)
    if len(chain) == goal:
        return chain
    # print("current chain", chain)
    for action in valid_actions(grid, state, chain):
        # print("actions after taking:", action, "->", valid_actions(grid, action, chain+[action]))
        if any([(len(valid_actions(grid, a, chain+[action, a])) == 0 and len(chain)+2 < goal) for a in valid_actions(grid, action, chain+[action])]):
            continue
        sol = solve(grid, action, goal, deepcopy(chain))
        if sol is not None:
            return sol
    return None


def switch_bulbs(grid):
    g = parse(grid)
    print("parsed")
    # Get the nodes with a single child
    num_hits = []  # list of indicies
    for i in g.allNodes():
        if len(i.getChildren()) == 1:
            print(i, "has children", i.getChildren())
            num_hits.append(i.getIndex())
        elif len(i.getChildren()) == 1:  # if a node has 0 children, the grid can't be solved
            return None
    if len(num_hits) > 2: # Otherwise, if more than 2 nodes have 1 child, no solution
        print("too many starts")
        return None
    elif len(num_hits) == 0:
        print("didn't have a starting point")
        for n in g.allNodeIndicies():
            try:
                print("trying with", n)
                sols = solve(g, n, len(g))
                if sols is None:
                    continue
                return [(i[0]-1, i[1]-1) for i in sols]
            except Exception as e:
                raise e
    else:
        print("perfect start")
        sols = solve(g, num_hits[0], len(g))
        if sols is None:
            return None
        return [(i[0]-1, i[1]-1) for i in sols]


grid = "+--------+\n"+\
"|........|\n"+\
"|.BBBBBB.|\n"+\
"|.BBBBBB.|\n"+\
"|.BBBBBB.|\n"+\
"|.BBBBBB.|\n"+\
"|.BBBBBB.|\n"+\
"|.BBBBBB.|\n"+\
"|........|\n"+\
"+--------+"

print(switch_bulbs(grid))