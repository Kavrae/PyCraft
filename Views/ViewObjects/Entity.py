class Entity:
    name = None
    value = None
    status = None

    text_color = None
    background_color = None

    # TODO eventually include more data
    # This is effectively a trimmed down version of a game character
    # But only include information necessary to display to the screen
    # No actual logic needed
    # TODO split this into different entity types that control their own colors and other properties via simpler constructors
    def __init__(self, name, value, status, text_color, background_color):
        self.name = name
        self.value = value
        self.status = status
        self.text_color = text_color
        self.background_color = background_color
