from GameLibrary.LibraryObjects.Units.Unit import Unit
import pygame


class Human(Unit):
    def __init__(self, owner_id, unit_id, unit_type, status, location, background_color):
        Unit.__init__(self, owner_id, unit_id, 'Human', unit_type, status, location, 'H', self.generate_text_color(status), background_color)

    def generate_text_color(self, status):
        if status == 'Alive':
            return pygame.Color('blue')
        elif status == 'Dead':
            return pygame.Color('white')
