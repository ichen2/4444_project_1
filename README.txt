CSC 4444 Project - Ian Chen
h1(n) = distance to closest dirty square + # dirty squares
h2(n) = distance to closest dirty square + # dirty squares + clean
	where 'clean' is 1 if the square is clean and 0 if it is dirty
	in other words, h2 adds 1 to clean squares
	the goal of this is to make h2 dominate h1, and to make the algorithm prioritize dirty squares

(I didn't use my actual h1 and h2 from the hw because they were wrong)

The basic logic of my program is:
1) Create the 5x5 grid
2) Initialize the grid with nodes, each with their cooresponding h and g values
3) Create the frontier, initialize it with the starting node 
4) While the grid is dirty: 
 - get the lowest value from the frontier
 - add its adjacent nodes to the frontier

