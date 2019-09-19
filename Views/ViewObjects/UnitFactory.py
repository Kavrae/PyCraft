from .UnitTypes.Human import Human
from .UnitTypes.Orc import Orc


class UnitFactory:
    @staticmethod
    # TODO make use of unit_type
    def create_unit(race, unit_type, status, background_color=(0, 0, 0)):
        if race == "Human":
            return Human(status, background_color)
        elif race == "Orc":
            return Orc(status, background_color)

    @staticmethod
    def library_unit_to_view_unit(library_unit):
        return UnitFactory.create_unit(library_unit._race, library_unit._unit_type, library_unit._status)
