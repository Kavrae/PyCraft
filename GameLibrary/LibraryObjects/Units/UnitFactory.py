from .Human.HumanWarrior import HumanWarrior
from .Orc.OrcWarrior import OrcWarrior  #TODO simplify this. Going to be too many imports


class UnitFactory:
    _game_state = None

    def __init__(self, game_state):
        self._game_state = game_state

    def create_new_unit(self, owner_id, race, unit_type, status, location):
        # TODO make this into an abstract factory later with individual race factories
        # TODO this also seems like a lot of duplication of parameters. Simplify?
        unit_id = len(self._game_state.units)

        if race == "Human":
            if unit_type == "Warrior":
                return HumanWarrior(owner_id, unit_id, status, location)
            elif unit_type == "Cleric":
                pass
        elif race == "Orc":
            if unit_type == "Warrior":
                return OrcWarrior(owner_id, unit_id, status, location)
            elif unit_type == "Shaman":
                pass
