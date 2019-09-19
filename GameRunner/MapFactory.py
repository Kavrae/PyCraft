import random
from Views.ViewObjects import TerrainFactory
from Views.ViewObjects import UnitFactory


# TODO an actual map generator with intelligent terrain placement OR premade maps (easier)
# TODO put this into the GameLibrary instead
# make the GameRunner worry about seed values, pulling in bots, and transforming things for the view layer
class MapFactory:
    def generate_example_map(self):
        terrain_map = []
        for row in range(100):
            new_row = []
            for column in range(100):
                status = "Alive" if random.randint(0, 1) == 0 else "Burned"
                if random.randint(0, 100) % 10 == 0:
                    new_row.append(TerrainFactory.create_terrain('Tree', status, (0, 0, 0)))
                else:
                    new_row.append(TerrainFactory.create_terrain('Grass', status, (0, 0, 0)))
            terrain_map.append(new_row)
        return terrain_map
