import pygame
from .Unit import Unit


class Orc(Unit):
    def __init__(self, status, background_color):
        super().__init__("Orc", "O", status, self.generate_text_color(status), background_color)

    def generate_text_color(self, status):
        if status == 'Alive':
            return pygame.Color('red')
        elif status == 'Dead':
            return pygame.Color('white')
