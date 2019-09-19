from .Entity_Types.Human import Human
from .Entity_Types.Orc import Orc


class EntityFactory:
    @staticmethod
    # TODO make use of unit as well
    def create_entity(race, unit, status, background_color=(0, 0, 0)):
        if race == "Human":
            return Human(status, background_color)
        elif race == "Orc":
            return Orc(status, background_color)

    @staticmethod
    def library_entity_to_view_entity(library_entity):
        return EntityFactory.create_entity(library_entity._race, library_entity._unit, library_entity._status)
