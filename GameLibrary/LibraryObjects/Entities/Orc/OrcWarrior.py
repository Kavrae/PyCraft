from .Orc import Orc


class OrcWarrior(Orc):
    def __init__(self, status):
        Orc.__init__(self, 'Warrior', status)
