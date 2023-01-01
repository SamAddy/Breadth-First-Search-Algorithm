import random
import curses
from curses import wrapper

def generate_maze(rows, cols):
    # Create a 2D array filled with "#" characters
    maze = [["#" for _ in range(cols)] for _ in range(rows)]
    
    # Set the starting position of the maze
    start_row = 1
    start_col = 1
    maze[start_row][start_col] = "0"
    
    # Set the ending position of the maze
    end_row = rows - 2
    end_col = cols - 2
    maze[end_row][end_col] = "X"
    
    # Initialize a stack for the depth-first search algorithm
    stack = [(start_row, start_col)]
    
    # Set of visited positions
    visited = set()
    
    # Perform depth-first search to generate the maze
    while stack:
        row, col = stack.pop()
        visited.add((row, col))
        
        # Find all unvisited neighbors of the current position
        neighbors = [(row + dr, col + dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                     if maze[row + dr][col + dc] == "#" and (row + dr, col + dc) not in visited]
        
        # If there are no unvisited neighbors, backtrack to the previous position
        if not neighbors:
            continue
        
        # Choose a random unvisited neighbor and move to it
        next_row, next_col = random.choice(neighbors)
        maze[next_row][next_col] = " "
        stack.append((next_row, next_col))
    
    return maze
    
 
