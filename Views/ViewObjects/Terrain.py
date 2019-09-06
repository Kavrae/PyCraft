class Terrain:
    name = None
    value = None
    status = None

    text_color = None
    background_color = None

    # TODO have terrain and entity inherit from a common interface for Tile to use
    def __init__(self, name, value, status, text_color, background_color):
        self.name = name
        self.value = value
        self.status = status
        self.text_color = text_color
        self.background_color = background_color
