from .Orc import Orc

# TODO get rid of background color nonsense EVERYWHERE

class OrcWarrior(Orc):
    def __init__(self, owner_id, unit_id, status, location, background_color):
        Orc.__init__(self, owner_id, unit_id, 'Warrior', status, location, background_color)
