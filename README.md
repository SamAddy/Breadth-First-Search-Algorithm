# Breadth-First-Search-Algorithm (Maze)
Breadth-first search (BFS) is an algorithm for traversing or searching a graph or tree data structure. It starts at the root node and explores all the nodes at the current level before moving on to the next level.

This project contains a Python implementation of the breadth-first search algorithm for solving a maze. The algorithm is designed to find a path from the starting position to the ending position of a maze represented as a 2D array of characters.

## Usage
The main function for solving a maze using the breadth-first search algorithm is find_path(), which is defined in the find_path.py. To use this function, you will need to pass it a maze represented as a 2D array of characters and stdscr.

## Algorithm 
The breadth-first search algorithm works by traversing the maze level by level, starting from the starting position and exploring all possible paths in a breadth-first manner. The algorithm maintains a queue of positions to visit, and at each step it removes the position at the front of the queue and adds all of its unvisited neighbors to the end of the queue. If the ending position is reached, the algorithm returns the path from the starting position to the ending position. If the queue becomes empty without reaching the ending position, the algorithm returns None to indicate that no solution was found.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.
