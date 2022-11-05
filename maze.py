"""
Maze class file.
"""

# Imports
import torch
import matplotlib.pyplot as plt

# Maze class
class Maze:
    """
    Random maze generator
    """
    def __init__(self, size, complexity=.75, density=.75):
        self.size = size
        self.complexity = complexity
        self.density = density
        self.maze = self.generate_maze()

    def generate_maze(self):
        shape = (3, self.size, self.size)
        maze = torch.ones(shape, dtype=float)
        # Borders
        maze[:, 0, :] = maze[:, -1, :] = 0
        maze[:, :, 0] = maze[:, :, -1] = 0
        # Red exit
        maze[0, -1, -2] = 1
        return maze

    def show_maze(self):
        plt.figure(figsize=(10, 5))
        # Transpose maze to show it correctly
        plt.imshow(torch.einsum("cwh->whc", self.maze))
        plt.xticks([]), plt.yticks([])
        plt.show()

if __name__ == '__main__':
    maze = Maze(41, .75, .75)
    maze.show_maze()