import random
from Views.ViewObjects import TerrainFactory
from Views.ViewObjects import EntityFactory


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

    def generate_example_entities(self):
        entity_map = []
        for row in range(100):
            new_row = []
            for column in range(100):
                status = "Alive" if random.randint(0, 1) == 0 else "Dead"
                if random.randint(0, 100) < 2:
                    new_row.append(EntityFactory.create_entity('Orc', status, (0, 0, 0)))
                elif random.randint(0, 100) < 4:
                    new_row.append(EntityFactory.create_entity('Human', status, (0, 0, 0)))
                else:
                    new_row.append(None)
            entity_map.append(new_row)
        return entity_map
