from Views.ViewObjects.Terrain_Types.Grass import Grass
from Views.ViewObjects.Terrain_Types.Tree import Tree


class Terrain(object):
    def __init__(self):
        pass

    @staticmethod
    def get_terrain(name, status, background_color):
        if name == "Grass":
            return Grass(status, background_color)
        elif name == "Tree":
            return Tree(status, background_color)