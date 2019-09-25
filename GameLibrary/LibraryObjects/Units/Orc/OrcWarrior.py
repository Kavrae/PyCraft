from .Orc import Orc


class OrcWarrior(Orc):
    def __init__(self, owner_id, unit_id, location):
        self._owner_id = owner_id
        self._unit_id = unit_id
        self._location = location
        self._unit_type = 'Warrior'
        self._hit_points = 30

        Orc.__init__(self)
