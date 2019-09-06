from Views.ViewObjects.Entity_Types.Human import Human
from Views.ViewObjects.Entity_Types.Orc import Orc


class Entity(object):
    def __init__(self):
        pass

    @staticmethod
    def get_entity(name, status, background_color):
        if name == "Human":
            return Human(status, background_color)
        elif name == "Orc":
            return Orc(status, background_color)