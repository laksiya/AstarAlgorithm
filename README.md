# Pathfinding Algorithms in Python

This repository contains two Python files that implement pathfinding algorithms using the A* search algorithm. The algorithms are designed to find the most efficient path between two points on a grid, navigating around obstacles and considering different terrain costs where applicable. The code is based on examples from Red Blob Games, with modifications to illustrate different pathfinding scenarios and grid configurations.

## File Descriptions

### File 1: `Astartask1.py` - Basic Pathfinding 

This file implements a basic version of the A* search algorithm to find the shortest path between two points on a grid. The grid is defined by a set of obstacles (walls) that the path cannot cross, and the algorithm seeks the shortest path from a start point (A) to a goal point (B).

**Key Features:**
- Implementation of the A* search algorithm.
- A grid system where obstacles can be placed to simulate walls.
- Functionality to read the grid configuration from a text file (`board-1-1.txt`).
- Visualization of the grid, the start and goal points, the path found, and the obstacles.

### File 2: `Astartask2.py` -  Weighted Pathfinding

This file extends the basic pathfinding algorithm by introducing a `GridWithWeights` class, which allows for different costs for moving through different types of terrain. This version can handle grids where moving through certain cells is more "expensive" than others, simulating real-world scenarios like roads, forests, mountains, etc.

**Key Features:**
- Inherits and extends the `SquareGrid` class to support weighted movement costs.
- Supports reading a grid configuration from a text file (`board-2-1.txt`), where different symbols represent different terrain types with associated movement costs.
- Visualization tools to display the grid, start and goal points, the path found, terrain types, and their costs.

## Usage

To use these scripts, you will need a Python environment with no external dependencies required. Each file can be run independently to demonstrate the A* pathfinding algorithm on predefined grid configurations. Ensure you have the corresponding board configuration text files (`board-1-1.txt` for `basic_pathfinding.py` and `board-2-1.txt` for `weighted_pathfinding.py`) in the same directory as the scripts.

**Running a Script:**
```bash
python Astartask1.py
```
or
```bash
python Astartask2.py
```

The output will be printed to the console, showing the grid with the start and goal points, the path found, and any obstacles or terrain costs.

## License

The original sample code from Red Blob Games is licensed under the Apache v2.0 license. Please ensure to follow the license agreement when using or modifying this code in your projects.
