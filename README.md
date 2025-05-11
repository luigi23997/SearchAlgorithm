# Search Algorithm Project

This project implements different search algorithms to solve pathfinding problems, specifically within a maze environment. The project is designed to demonstrate the use of several classic search algorithms and provides tools for manipulating and studying mazes.

## File Structure

- `search.py`: Contains the base classes and different frontier classes required for the search algorithms.
  - **Node**: Represents a point or position within the maze.
  - **Frontier Classes**: Various classes used to manage the frontier (or open list) for the search algorithms. These include structures such as stacks, queues, and custom queues, depending on the algorithm.

- `maze.py`: Contains the **Maze** class, which includes methods to manipulate and study mazes. This includes:
  - Generating mazes.
  - Visualizing mazes.
  - Handling maze properties and related operations.

- `maze.ipynb`: A Jupyter notebook where the search algorithms are implemented using the other classes. It includes:
  - **Depth-First Search (DFS)**: A search algorithm that explores as far as possible along each branch before backtracking.
  - **Breadth-First Search (BFS)**: A search algorithm that explores all the nodes at the present depth level before moving on to the nodes at the next depth level.
  - **Greedy Best-First Search (GBFS)**: A search algorithm that expands the node that appears to be closest to the goal based on a heuristic.
  - **A\* Search (Alpha Star)**: A search algorithm that combines the best features of DFS, BFS, and GBFS. It uses both the actual cost to reach a node and an estimate of the remaining cost to the goal.

## Requirements

To run this project, you need to have the following Python packages installed:

- `PIL`: For maze visualization.
- `IPython.display`: For maze visualization in the ipynb.

You can install the required dependencies using `pip`:

```bash
pip install Pillow, ipython