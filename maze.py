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
        # Adjust complexity and density relative to maze size
        complexity = int(self.complexity * self.size)  # number of components
        density = int(self.density * self.size ** 2)  # size of components
        # Make aisles
        for _ in range(density):
            x, y = torch.randint(self.size // 2, (1,)) * 2, torch.randint(self.size // 2, (1,)) * 2  # pick an even random position
            maze[:, y, x] = 0
            for _ in range(complexity):
                neighbours = []
                if x > 1:
                    neighbours.append((y, x - 2))
                if x < shape[1] - 2:
                    neighbours.append((y, x + 2))
                if y > 1:
                    neighbours.append((y - 2, x))
                if y < shape[0] - 2:
                    neighbours.append((y + 2, x))
                if len(neighbours):
                    y_, x_ = neighbours[torch.randint(len(neighbours), (1,))]
                    if maze[:, y_, x_].any():
                        maze[:, y_, x_] = 0
                        maze[:, y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 0
                        x, y = x_, y_
        return maze

    def show_maze(self):
        plt.figure(figsize=(10, 5))
        # Transpose maze to show it correctly
        plt.imshow(torch.einsum("cwh->whc", self.maze))
        plt.xticks([]), plt.yticks([])
        plt.show()

if __name__ == '__main__':
    maze = Maze(41, .75, .8)
    maze.show_maze()