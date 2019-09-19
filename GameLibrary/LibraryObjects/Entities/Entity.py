class Entity:
    _id = None
    _race = None
    _unit = None
    _status = None
    _position = None

    def __init__(self, race, unit, status):
        self._id = 0
        self._race = race
        self._unit = unit
        self._status = status

    # TODO get all of these properties organized
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is tuple and type(value[0]) is int and type(value[1]) is int:
            self._position = value
        else:
            raise TypeError("Position must be a tuple of two integers")