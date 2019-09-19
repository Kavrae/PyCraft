from .Human import Human


class HumanWarrior(Human):
    def __init__(self, status):
        Human.__init__(self, 'Warrior', status)  # TODO change to type check instead of "warrior"?
