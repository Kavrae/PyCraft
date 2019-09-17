from .Terrain_Types.Grass import Grass
from .Terrain_Types.Tree import Tree


class TerrainFactory:
    @staticmethod
    def create_terrain(name, status, background_color):
        if name == "Grass":
            return Grass(status, background_color)
        elif name == "Tree":
            return Tree(status, background_color)
