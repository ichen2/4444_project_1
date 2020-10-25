# Ian Chen
# CSC 4444
# 10/20/2020

def main():
    # Part A:
    # this iteration uses h1. The exact value of h1 can be found in README
    # declare all the starting variables - the grid, the frontier, the # dirty squares
    dirty = 5
    w,h = 5,5
    grid = [[0 for x in range(h)] for y in range(w)] # grid[x][y]
    for i in range(0,len(grid)-1): # declares all clean nodes
        for j in range(0,len(grid[0])):
            grid[j][i] = Node(j,i,False,9-i,i + j) # the heuristic value (h) and distance (g) of each square is hard coded.
    for i in range(0,len(grid)): # declares all dirty nodes
        grid[i][4] =  Node(i,4,True,5,4+i) 
    frontier = [grid[0][0]] # initialize the frontier with the starting square
    visited = [] # create an empty list of visited squares
    while dirty > 0: # while there are dirty squares
        next = frontier.pop(0) # pop the first square off the frontier
        visited.append(next) # add it to the 'visited' list
        frontier += getAdjacent(grid,visited,next,frontier) # add all of it's adjacent squares to the frontier (if they are not already in 'frontier' or 'visited)
        if next.isDirty(): # if the square is dirty
            next.clean() # clean it
            dirty -= 1 # update the number of dirty squares
            for i in range(0,h): # this function updates the heuristic function of all squares
                for j in range(0,w): # since h = # dirty squares + distance to closest dirty square, whenever a square is cleaned the h of all squares will decrease 
                    if(j<=next.x): # however, the h of some squares will stay the same, since the # dirty squares increases but the distance to closest square decreases 
                        break # for these squares, the h stays the same
                    grid[j][i].subHeuristic() # for all other squares, the h decreases by 1
        frontier.sort(key=getF) # sorts the frontier, so that the square with the lowest f will be on top
    # now that the grid has been searched, the algorithm must find the optimal path
    n = grid[4][4] # creates n which equals the last square
    moves = [] # creates a list to contain the sequence of moves for the optimal path
    while(n != grid[0][0]): # while the array has not reached the starting square
        moves.append(n) # add n to 'moves'
        n = n.getParent() # set n equal to its parent
    # this while loop iterates through the optimal path until it reaches the starting square
    moves.reverse() # reverses moves, so that instead of going from end to beginning it will go from beginning to end
    for move in moves: # prints all the moves of the optimal path
        move.simplePrint()
    print(f"Optimal path cost: {len(moves)}") # prints the path cost (which is the number of moves, or the length of 'moves')
    print(f"Number of nodes expanded: {len(visited)}") # prints the number of nodes expanded (which is the length of 'visited')

    # Part B:
    # this iteration uses h2. The exact value of h1 can be found in README
    # follows the same logic as previous iteration. the only difference is that each clean square has 
    # a h value of +1. this is because h2 also considers whether a square is clean or dirty.
    # if it is clean, h2 adds 1 to the heuristic function
    # this not only makes h2 dominate h1, but also make h2 prioritze dirty squares
    dirty = 5
    w,h = 5,5
    grid = [[0 for x in range(h)] for y in range(w)] 
    for i in range(0,len(grid)-1):
        for j in range(0,len(grid[0])):
            grid[j][i] = Node(j,i,False,9-i+1,i + j)
    for i in range(0,len(grid)):
        grid[i][4] =  Node(i,4,True,5,4+i)
    frontier = [grid[0][0]]
    visited = []
    count = 0
    while dirty > 0:
        next = frontier.pop(0)
        visited.append(next)
        frontier += getAdjacent(grid,visited,next,frontier)
        if next.isDirty():
            next.clean()
            dirty -= 1
            for i in range(0,h):
                for j in range(0,w):
                    if(j<=next.x):
                        continue
                    grid[j][i].subHeuristic()
        frontier.sort(key=getF)
    n = grid[4][4]
    moves = []
    while(n != grid[0][0]):
        moves.append(n)
        n = n.getParent()
    moves.reverse()
    for move in moves:
        move.simplePrint()
    print(f"Optimal path cost: {len(moves)}")
    print(f"Number of nodes expanded: {len(visited)}")

# this section contains helper functions and classes utilized by the program
def getF(n): # used to get the F of a node. requred to use the list.sort() method in python
    return n.getF()

def getAdjacent(allNodes,visitedNodes,node,addedNodes): # returns a list of all adjacent nodes which have not already been visited/ added to the frontier
    x,y = 0,0
    for i in range(0,5):
        try:
            y = allNodes[i].index(node)
            x = i
            break
        except ValueError:
            continue
    adjacentNodes = []
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for d in directions:
        i = d[0]
        j = d[1]
        if(((x+i >= 0 and x+i < 5) and (y+j >= 0 and y+j < 5)) and  (not (allNodes[x+i][y+j] in addedNodes)) and (not (allNodes[x+i][y+j] in visitedNodes))):
            allNodes[x+i][y+j].setParent(node)
            adjacentNodes.append(allNodes[x+i][y+j]) 
    return adjacentNodes

class Node: # node object 
    def __init__(self,x,y,d,h,g):
        self.dirty = d
        self.heuristic = h
        self.distance = g
        self.x = x
        self.y = y
    def isDirty(self):
        return self.dirty
    def clean(self):
        self.dirty = False
    def getF(self):
        return self.heuristic + self.distance
    def subHeuristic(self):
        self.heuristic -= 1
    def setParent(self,node):
        self.parent = node
    def getParent(self):
        return self.parent
    def print(self): # printing used for debuggin. prints all info of a node
        print(f"Coordinates: ({self.x},{self.y}) | Dirty: {self.dirty} | Heuristic: {self.heuristic} | Distance: {self.distance}")
    def simplePrint(self): # printing used in actual program. just prints a node's (x,y) coordinate
        print(f"({self.x},{self.y})")

if __name__ == "__main__": # runs main method
    main()