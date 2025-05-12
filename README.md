## Conway's Game of Life – Python Terminal Version
This is a Python implementation of Conway's Game of Life, a classic example of cellular automata. The simulation runs in the terminal, using ASCII characters to represent living and dead cells.
##  About
Conway's Game of Life is a zero-player game devised by mathematician John Conway. It simulates the life and death of cells on a grid, based on a set of simple rules.

This version features:
- A randomly initialized starting grid.
- Periodic screen clearing to show successive generations.
- Simple terminal-based visualization.
- Wrapping edges (toroidal grid).
## Requirements
- Python 3.x
- Works on Linux, macOS, and Windows (terminal support required)
## Rules of the Game
Each cell can be either alive (#) or dead ( ). For each generation:
- A live cell with 2 or 3 live neighbors survives.
- A dead cell with exactly 3 live neighbors becomes alive.
- All other cells die or remain dead.

The grid wraps around at the edges, simulating an infinite surface.
