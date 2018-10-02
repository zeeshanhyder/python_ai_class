'''
'' Program to find solution to 8-Queens problem when k=1, k=10 and k=50
''
'' Please note that since beam search is not complete, so solution (i.e cost=0) is not always possible.
'' However it will always return the minimum cost from all search costs
''
'' Author Zeeshan Hyder Bhat
'' 10/18/2017
'''


from random import *
import time

# get total queens attacking
def getAttackingQueens(queensList):
    # stores count of attacking queens
    totalCount = 0

    for i,c in enumerate(queensList):
        if i < 7:
            for j in xrange(i+1, len(queensList)):
                # find attacking queens horizontally
                if c == queensList[j]:
                    totalCount+=1
                # find attacking queens diagonally top to bottom
                if int(queensList[j]) == int(c)+(j-i):
                    totalCount += 1
                # find attacking queens diagonally bottom to top
                if int(c) == int(queensList[j])+(j-i):
                    totalCount+=1
    return totalCount

# generates random input to start our beam search with
def generateInput(inputSize):
    items = [0,1, 2, 3, 4, 5, 6, 7]
    inputList = []

    for num in range(inputSize):
            gen = sample(items, 8)
            gen = ''.join(str(e) for e in gen)
            gen = str(gen)
            if gen not in inputList:
                inputList.append(gen)
    return inputList


# getSuccessors returns the successors of each node
def getSuccessors(inputList):
    successor_list = []

    for i,c in enumerate(inputList):
        num = int(c)
        num_range = range(8)
        num_range.remove(int(c))

        for num in num_range:
            c = str(num)
            newList = inputList[:i] + c + inputList[i+1:]
            successor_list.append(newList)
    return successor_list

# from the successors generated using getSuccessors(), select best Successor that has lowest cost
def getBestSuccessors(board):

    # contains map from 0 or more [basically cost]
    successorCostList = dict()

    # will contain the best successor we find
    bestSuccessor = []

    # first, get all possible successors
    successors = getSuccessors(board)

    # iterate each successor and find their cost
    for successor in successors:
        cost = int(getAttackingQueens(successor))
        # put them in the map based on their cost
        successorCostList[cost] = successor


    # get the lowest cost and put it in bestSuccessor
    for key in sorted(successorCostList.iterkeys()):
        if len(bestSuccessor) < 1 :
            bS = dict()
            bS['cost'] = key
            bS['list'] = successorCostList[key]
            bestSuccessor.append(bS)

    return bestSuccessor




def beamSearch(boards, beam_width):
    startTime = time.time()
    # our queue to hold successors based on their increasing cost
    fringe = []

    # our beam width
    k = beam_width

    # on our first iteration, get best successors of first two generated boards
    for board in boards:
        fringe += getBestSuccessors(board)

    # now find the solution
    while(len(fringe) != 0 and k > 0 ):
        # get the lowest cost item from fringe
        current_node = fringe.pop()

        # cost of current node
        solution = current_node['cost']

        # if it's not the solution
        if solution != 0:
            fringe += getBestSuccessors(current_node['list'])
            k = k-1
        else:
            #solution found
            print("Solution found!")
            # no solution found i.e. cost > 0
            endTime = time.time()
            totalTime = endTime-startTime
            print("Total time taken: "+str(totalTime)+" seconds")
            return current_node
    else:
        # no solution found i.e. cost > 0
        endTime = time.time()
        totalTime = endTime-startTime
        print("Total time taken: "+str(totalTime)+" seconds")
        return current_node

# our entry point of program
def main():

    # generate large 8-queens problems
    boards = generateInput(100)
    print("Input:")
    for board in boards:
        print(board)
    print("----------")

    k=1
    print("When K=1 ------------")
    finalBoard = beamSearch(boards, k)
    print("Board: "+finalBoard['list'])
    print("Conflicts: "+str(finalBoard['cost']))

    boards = generateInput(100)
    k=10
    print("When K=10 ------------")
    finalBoard = beamSearch(boards, k)
    print("Board: "+finalBoard['list'])
    print("Conflicts: "+str(finalBoard['cost']))

    boards = generateInput(100)
    k=50
    print("When K=50 ------------")
    finalBoard = beamSearch(boards, k)
    print("Board: "+finalBoard['list'])
    print("Conflicts [cost]: "+str(finalBoard['cost']))

# call to main()
main()
