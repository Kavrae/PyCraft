from .Human import Human


class HumanWarrior(Human):
    def __init__(self, owner_id, unit_id, status, location, background_color):
        Human.__init__(self, owner_id, unit_id, 'Warrior', status, location, background_color)
