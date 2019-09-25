from GameLibrary.LibraryObjects.Units.Unit import Unit
import pygame


class Human(Unit):
    def __init__(self):
        self._race = 'Human'
        self._display_value = 'H'
        self._text_color = self.generate_text_color()

        Unit.__init__(self)

    def generate_text_color(self):
        status = 'Alive'  # TODO base this on something else later
        if status == 'Alive':
            return pygame.Color('blue')
        elif status == 'Dead':
            return pygame.Color('white')
