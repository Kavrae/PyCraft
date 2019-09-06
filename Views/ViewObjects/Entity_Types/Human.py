import pygame


class Human:
    name = None
    value = None
    status = None

    text_color = None
    background_color = None

    def __init__(self, status, background_color):
        self.name = 'Human'
        self.value = '@'
        self.status = status
        self.text_color = self.set_text_color()
        self.background_color = background_color

    def set_text_color(self):
        if self.status == 'Alive':
            return pygame.Color('blue')
        elif self.status == 'Dead':
            return pygame.Color('white')
