from .Orc import Orc


class OrcWarrior(Orc):
    def __init__(self, owner_id, unit_id, status, location):
        Orc.__init__(self, owner_id, unit_id, 'Warrior', status, location)
