class Terrain:
    _terrain_type = None
    _status = None

    _display_value = None
    _text_color = None
    _background_color = None

    def __init__(self, terrain_type, status, display_value, text_color, background_color):
        self._terrain_type = terrain_type
        self._status = status
        self._display_value = display_value
        self._text_color = text_color
        self._background_color = background_color
