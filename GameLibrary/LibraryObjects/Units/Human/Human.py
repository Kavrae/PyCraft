from GameLibrary.LibraryObjects.Units.Unit import Unit


class Human(Unit):
    def __init__(self, owner_id, unit_id, unit_type, status, location):
        Unit.__init__(self, owner_id, unit_id, 'Human', unit_type, status, location)  # TODO change to type check instead of "human"?
