from GameLibrary.LibraryObjects.Units.Unit import Unit
import pygame


class Orc(Unit):
    def __init__(self, owner_id, unit_id, unit_type, status, location):
        Unit.__init__(self, owner_id, unit_id, 'Orc', unit_type, status, location, 'O', self.generate_text_color(status), background_color)

    def generate_text_color(self, status):
        if status == 'Alive':
            return pygame.Color('red')
        elif status == 'Dead':
            return pygame.Color('white')
