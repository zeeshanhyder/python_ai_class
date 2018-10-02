'''
'' Program to demonstrate BFS using Romania Roadmap
'' Date 09/14/2017
'' Author Zeeshan Hyder Bhat
'''


# Tree structure
class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children


    def __str__(self):
        return str(self.value)

# Fringe is basically the FIFO Queue
fringe = []
path = []

# BFS method
def BFS(tree, iter):
    global fringe
    global path

    print(tree.value)
    # path.append(tree.value)

    # Goal State
    if(tree.value == 'Bucharest'):
        print("\n\n")
        return;

    if tree.children != None:
        path.append(len(fringe))
        fringe = fringe+tree.children


    iter = iter+1
    if iter == path[0]:
        path.pop(0)
        print("\n---------------\n")
    if(iter == len(fringe)):
        fringe = []
        print("Tree exhausted")
        return # tree exhausted
    else:
        BFS(fringe[iter],iter)




'''
'' Romania Road map in tree structure
'''

nodeBucharest = Tree("Bucharest")
nodeFagaras = Tree("Fagaras", [nodeBucharest])
nodeArad = Tree("Arad")
nodeSibiu = Tree("Sibiu",[nodeArad, nodeFagaras])
nodePitesti = Tree("Pitesti",[nodeBucharest])
nodeCraiova = Tree("Craiova",[nodePitesti])
nodeRV = Tree("Rimnicu Vilcea",[nodeCraiova, nodePitesti, nodeSibiu])

## Tree end

## fringe index pointer at the beginning
itr = -1

## start at first node which is RV
BFS(nodeRV,itr)
