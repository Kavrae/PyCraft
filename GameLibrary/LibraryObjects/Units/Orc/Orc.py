from GameLibrary.LibraryObjects.Units.Unit import Unit


class Orc(Unit):
    def __init__(self, owner_id, unit_id, unit_type, status, location):
        Unit.__init__(self, owner_id, unit_id, 'Orc', unit_type, status, location)  # TODO change to type check instead of "Orc"?