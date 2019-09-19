import pygame
from .Unit import Unit


class Human(Unit):
    def __init__(self, status, background_color):
        super().__init__("Human", "H", status, self.generate_text_color(status), background_color)

    def generate_text_color(self, status):
        if status == 'Alive':
            return pygame.Color('blue')
        elif status == 'Dead':
            return pygame.Color('white')
