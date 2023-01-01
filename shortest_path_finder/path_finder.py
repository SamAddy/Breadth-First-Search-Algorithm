import curses
from curses import wrapper
import queue
import time


# Define the maze as a 2D array of characters
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "X"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr, path=[]):
    """
    This function prints the maze onto the screen. 

    Parameters:
    maze - the maze to be printed out
    stdscr - the maze will be printed to this standard outputs
    path - values of coordinate are passed to it and draws them on the maze

    Returns:
    Tuple - returns a list of tuples representing the path from the start position to the end position.		
    """
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    # Iterate through the maze
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, GREEN)


def find_start(maze, start):
    """This function search in the maze to find the starting position. It does so by searching for whatever the start value is."""
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                # Return the coordinates when start is found
                return i, j
    
    # Return none if no start position is found 
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    # A queue is used in processing the nodes in breadth-first search algo
    # The first element inserted will be the first element to be poped out
    q = queue.Queue()
    # Insert into the queue
    q.put((start_pos, [start_pos]))
    
    # Store all visited nodes into this set
    visited = set()

    # Processing nodes in the queue
    while not q.empty():
        # Get the node at the front of the queue
        current_pos, path = q.get()
        row, col = current_pos

        # Clear screen
        stdscr.clear()
        stdscr.addstr(10, 10, "Breadth-First Search Algorithm for Solving a Maze", curses.A_BOLD)
        # Calling print_maze function to draw out the maze
        print_maze(maze, stdscr, path)
        # Adding a sleep time to help visualize
        time.sleep(0.2)
        # refresh the screen 
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    find_path(maze, stdscr)
    # Wait for user to press a key to exit the program
    stdscr.getch()


wrapper(main)
