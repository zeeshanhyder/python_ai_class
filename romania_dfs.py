'''
'' Program to demonstrate DFS using Romania Roadmap
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

goal_state = 0
# DFS method
def DFS(tree):
    global goal_state

    print(tree.value)

    # Goal state
    if(tree.value == 'Bucharest'):
        goal_state = 1
        return

    if tree.children == None:
        return
    else:
        for stree in tree.children:
            if goal_state == 0:
                DFS(stree)





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


DFS(nodeRV)
