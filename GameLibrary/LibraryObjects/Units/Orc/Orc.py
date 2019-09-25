from GameLibrary.LibraryObjects.Units.Unit import Unit
import pygame


class Orc(Unit):
    def __init__(self):
        self._race = 'Orc'
        self._display_value = 'O'
        self._text_color = self.generate_text_color()

        Unit.__init__(self)

    def generate_text_color(self):
        status = 'Alive'  # TODO base this on something else later
        if status == 'Alive':
            return pygame.Color('red')
        elif status == 'Dead':
            return pygame.Color('white')
