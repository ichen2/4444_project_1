CSC 4444 Project - Ian Chen
h1(n) = distance to closest dirty square + # dirty squares
h2(n) = distance to closest dirty square + # dirty squares + clean
	where 'clean' has a value of 1 if the square is clean and 0 if it is dirty
	in other words, h2 adds 1 to clean squares
	the goal of this is to make h2 dominate h1, and to make the algorithm prioritize dirty squares

(I didn't use my actual h1 and h2 from the homework because they were wrong)

The basic logic of my program is:
1) Create the 5x5 grid
2) Initialize the grid with nodes, each with their cooresponding h and g values
3) Create the frontier, initialize it with the starting node 
4) While the grid is dirty: 
 - get the lowest value node from the frontier
 - add its adjacent nodes to the frontier
 - if the node is dirty, clean it and update the h values of all other nodes
 - sort the frontier
5) Start from the ending node, and trace the optimal path back to the starting node
6) Print the optimal path, its cost, and the # nodes expanded.

This logic runs twice, once with h1 and once with h2.
h1 and h2 are hard coded into the program; in other words, instead of writing a function to calculate
h1 and h2 based on the node, I just wrote the code so that when the grid is initialized, each node has the correct
h1 and h2 value.
I did this because a method to calculate each heuristic function would require another search algorithm
(since both h1 and h2 need to find the nearest dirty node) which would greatly increase the time complexity.

