from .Human import Human


class HumanWarrior(Human):
    def __init__(self, owner_id, unit_id, status, location):
        Human.__init__(self, owner_id, unit_id, 'Warrior', status, location)  # TODO change to type check instead of "warrior"?
