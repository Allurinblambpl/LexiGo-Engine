import random
from math3d import Vector3

class Terrain:
    def __init__(self, width, height, max_height=5):
        self.width = width
        self.height = height
        self.max_height = max_height
        self.grid = self.generate_terrain()

    def generate_terrain(self):
        """Generates random terrain grid."""
        terrain = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                height = random.uniform(0, self.max_height)
                row.append(Vector3(x, y, height))
            terrain.append(row)
        return terrain

    def get_point(self, x, y):
        """Returns the height of the terrain at (x, y)."""
        return self.grid[x][y]
