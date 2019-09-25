class Unit:
    # Object information
    _unit_id = None
    _owner_id = None
    _race = None
    _unit_type = None
    _location = None

    # Unit stats
    _hit_points = None
    _status_effects = None  # TODO each status effect is an object with an Update() method that affects the class it's attached to each update before it acts. Somehow avoid circular dependencies

    # View information
    _display_value = None
    _text_color = None
    _background_color = None

    def __init__(self):
        self._background_color = (0, 0, 0)
        self._status_effects = []

    # TODO get all of these properties organized
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if type(value) is tuple and type(value[0]) is int and type(value[1]) is int:
            self._location = value
        else:
            raise TypeError("Location must be a tuple of two integers")

    def get_display_name(self):
        return self._race + " " + self._unit_type
