import random
import numpy
from GameLibrary.LibraryObjects.Terrain.Grass import Grass
from GameLibrary.LibraryObjects.Terrain.Tree import Tree


# TODO use numpy integer slicing to get the subsection to view (faster)
class MapFactory:
    @staticmethod
    def generate_example_map():
        terrain_map = numpy.full([100, 100], fill_value=None)
        for row in range(100):
            for column in range(100):
                status = "Alive" if random.randint(0, 1) == 0 else "Burned"
                if random.randint(0, 100) % 10 == 0:
                    terrain_map[row, column] = Tree(status, (0, 0, 0))
                else:
                    terrain_map[row, column] = Grass(status, (0, 0, 0))
        return terrain_map
