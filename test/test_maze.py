"""
Maze test file.
"""

import unittest

from src.mazeEnv.maze import Maze


class TestMaze(unittest.TestCase):
    def test_init(self):
        """
        Test that it can sum a list of integers
        """
        maze = Maze(10)
        self.assertEqual(maze.size, 10)
        self.assertEqual(maze.complexity, .75)
        self.assertEqual(maze.density, .75)
        self.assertEqual(maze.maze.shape, (3, 10, 10))

if __name__ == '__main__':
    unittest.main()
