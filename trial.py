# Conway's Game of Life - Refactored and Commented Version
import random
import time
import os

# Set the size of the grid
WIDTH = 60
HEIGHT = 20
ALIVE = '#'  # Character to represent a living cell
DEAD = ' '   # Character to represent a dead cell

def clear_screen():
    """Clear the terminal screen between generations."""
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_grid(width, height):
    """Create and return a randomly initialized grid of cells."""
    return [
        [ALIVE if random.randint(0, 1) == 0 else DEAD for _ in range(height)]
        for _ in range(width)
    ]

def print_grid(grid):
    """Display the grid to the terminal."""
    for y in range(HEIGHT):
        row = ''.join(grid[x][y] for x in range(WIDTH))
        print(row)

def count_neighbors(grid, x, y):
    """Count how many living neighbors a given cell has."""
    # Get coordinates of neighboring cells, wrapping around edges
    left = (x - 1) % WIDTH
    right = (x + 1) % WIDTH
    above = (y - 1) % HEIGHT
    below = (y + 1) % HEIGHT

    # List all 8 neighboring cells
    neighbors = [
        grid[left][above], grid[x][above], grid[right][above],
        grid[left][y],                     grid[right][y],
        grid[left][below], grid[x][below], grid[right][below]
    ]

    # Count how many are alive
    return sum(1 for cell in neighbors if cell == ALIVE)

def compute_next_grid(current_grid):
    """Compute the next generation of the grid based on current state."""
    new_grid = [[DEAD for _ in range(HEIGHT)] for _ in range(WIDTH)]

    for x in range(WIDTH):
        for y in range(HEIGHT):
            neighbors = count_neighbors(current_grid, x, y)
            # Apply Conway's Game of Life rules:
            if current_grid[x][y] == ALIVE and neighbors in (2, 3):
                new_grid[x][y] = ALIVE  # Living cell stays alive
            elif current_grid[x][y] == DEAD and neighbors == 3:
                new_grid[x][y] = ALIVE  # Dead cell becomes alive
            else:
                new_grid[x][y] = DEAD   # All other cells die or stay dead
    return new_grid

def main():
    """Main loop of the Game of Life."""
    grid = initialize_grid(WIDTH, HEIGHT)  # Start with a random grid

    try:
        while True:
            clear_screen()         # Clear screen before printing the next state
            print_grid(grid)       # Show the current grid
            grid = compute_next_grid(grid)  # Generate next grid
            time.sleep(1)          # Pause to slow down the animation
    except KeyboardInterrupt:
        print("\nSimulation stopped.")  # Exit gracefully on Ctrl+C

# Run the program
if __name__ == "__main__":
    main()
