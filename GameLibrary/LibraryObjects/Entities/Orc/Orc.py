from GameLibrary.LibraryObjects.Entities.Entity import Entity


class Orc(Entity):
    def __init__(self, unit, status):
        Entity.__init__(self, 'Orc', unit, status)  # TODO change to type check instead of "human"?