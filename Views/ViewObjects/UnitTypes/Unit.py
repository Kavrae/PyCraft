class Unit(object):
    # TODO proper properties
    _name = None
    _value = None
    _status = None

    _text_color = None
    _background_color = None

    def __init__(self, name, value, status, text_color, background_color):
        self._name = name
        self._value = value
        self._status = status
        self._text_color = text_color
        self._background_color = background_color

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_status(self):
        return self._status

    def get_text_color(self):
        return self._text_color

    def get_background_color(self):
        return self._background_color
