class Tree:
    name = None
    value = None
    status = None

    text_color = None
    background_color = None

    def __init__(self, status, background_color):
        self.name = 'Tree'
        self.value = '$'
        self.status = status
        self.text_color = self.set_text_color()
        self.background_color = background_color

    def set_text_color(self):
        if self.status == 'Alive':
            return 0, 255, 0
        elif self.status == 'Burned':
            return 163, 181, 109
