# Ian Chen
# CSC 4444
# 10/20/2020

def main():
    # declare all the starting variables - the grid, the frontier, the # dirty squares
    dirty = 5
    w,h = 5,5
    grid = [[0 for x in range(h)] for y in range(w)] # grid[x][y]
    for i in range(0,len(grid)-1): # declares all clean nodes
        for j in range(0,len(grid[0])):
            grid[j][i] = Node(j,i,False,9-i,i + j)
    for i in range(0,len(grid)):
        grid[i][4] =  Node(i,4,True,5,4+i) # declares all dirty nodes
    frontier = [grid[0][0]]
    visited = []
    while dirty > 0:
        next = frontier.pop(0)
        visited.append(next)
        frontier.appen(getAdjacent(next))
        if next.isDirty():
            dirty -= 1
            # update nodes
        # sort frontier

def getAdjacent(allNodes,visitedNodes,node):
    x,y = 0,0
    for i in range(0,5):
        try:
            y = allNodes[i].index(node)
            x = i
            break
        except ValueError:
            continue
    adjacentNodes = []
    for i in range(-1,2):
        for j in range(-1,2):
            if(not(i==0 and j==0)):
                if(((x+i >= 0 and x+i < 5) and (y+j >= 0 and y+j < 5)) and not (allNodes[x+i][y+j] in visitedNodes)):
                    adjacentNodes.append(allNodes[x+i][y+j])
    return adjacentNodes



class Node:
    def __init__(self,x,y,d,h,g):
        self.dirty = d
        self.heuristic = h
        self.distance = g
        self.x = x
        self.y = y
    def isDirty(self):
        return self.dirty
    def getF(self):
        return self.heuristic + self.distance
    def subHeuristic(self):
        self.heuristic -= 1
    def print(self):
        print(f"Coordinates: ({self.x},{self.y} | Dirty: {self.dirty} | Heuristic: {self.heuristic} | Distance: {self.distance}")



if __name__ == "__main__":
    main()