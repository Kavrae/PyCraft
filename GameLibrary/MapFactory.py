import random
from GameLibrary.LibraryObjects.Terrain.Grass import Grass
from GameLibrary.LibraryObjects.Terrain.Tree import Tree


class MapFactory:
    @staticmethod
    def generate_example_map():
        terrain_map = []
        for row in range(100):
            new_row = []
            for column in range(100):
                status = "Alive" if random.randint(0, 1) == 0 else "Burned"
                if random.randint(0, 100) % 10 == 0:
                    new_row.append(Tree(status, (0, 0, 0)))
                else:
                    new_row.append(Grass(status, (0, 0, 0)))
            terrain_map.append(new_row)
        return terrain_map
