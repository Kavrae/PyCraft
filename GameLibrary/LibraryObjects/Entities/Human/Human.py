from GameLibrary.LibraryObjects.Entities.Entity import Entity


class Human(Entity):
    def __init__(self, unit, status):
        Entity.__init__(self, 'Human', unit, status)  # TODO change to type check instead of "human"?