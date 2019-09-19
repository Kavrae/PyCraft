from .Human.HumanWarrior import HumanWarrior
from .Orc.OrcWarrior import OrcWarrior  #TODO simplify this. Going to be too many imports


class EntityFactory:
    @staticmethod
    def create_new_unit(race, unit, status):
        # TODO make this into an abstract factory later with individual race factories
        if race == "Human":
            if unit == "Warrior":
                return HumanWarrior(status)
        if race == "Orc":
            if unit == "Warrior":
                return OrcWarrior(status)
