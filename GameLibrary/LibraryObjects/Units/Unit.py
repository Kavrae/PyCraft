class Unit:
    _unit_id = None
    _owner_id = None
    _race = None
    _unit_type = None
    _status = None
    _location = None

    def __init__(self, unit_id, owner_id, race, unit_type, status, location):
        self._unit_id = unit_id
        self._owner_id = owner_id
        self._race = race
        self._unit_type = unit_type
        self._status = status
        self._location = location

    # TODO get all of these properties organized
    @property
    def location(self):
        return self._location

    @location.setter
    def position(self, value):
        if type(value) is tuple and type(value[0]) is int and type(value[1]) is int:
            self._location = value
        else:
            raise TypeError("Position must be a tuple of two integers")