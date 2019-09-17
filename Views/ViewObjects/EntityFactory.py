from .Entity_Types.Human import Human
from .Entity_Types.Orc import Orc


class EntityFactory:
    @staticmethod
    def create_entity(name, status, background_color):
        if name == "Human":
            return Human(status, background_color)
        elif name == "Orc":
            return Orc(status, background_color)