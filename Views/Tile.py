import pygame
from pygame.locals import *


class Tile:
    rect: Rect = None
    surface = None

    font = None

    # TODO change these to objects as well
    terrain_value = None
    entity_value = None
    
    mouse_position = None
    background_color = None

    is_selected = None
    is_changed = None
    
    def __init__(self, rect: Rect, terrain_value, entity_value, font, mouse_position: tuple, background_color: tuple = pygame.Color("black")):
        self.rect = rect
        self.terrain_value = terrain_value
        self.entity_value = entity_value
        self.font = font
        self.mouse_position = mouse_position
        self.background_color = background_color

        self.is_selected = False
        self.is_changed = True

        self.surface = pygame.Surface(self.rect.size)
        self.surface.fill(self.background_color)

    def update(self):
        self.update_selected()

    # TODO change this to determine which value to use. Maybe overlap. Maybe priority
    def render(self):
        if self.is_changed:
            # Create Font surface
            antialias = True
            text_color = (0, 175, 0)
            font_surface = self.font.render(self.terrain_value, antialias, text_color, self.background_color)
            font_rect = font_surface.get_rect()
            font_rect.center = (self.rect.width / 2, self.rect.height / 2)

            # Add font to tile. Add tile to screen
            self.surface.blit(font_surface, font_rect)

            # Add selected box highlight
            if self.is_selected:
                self.render_selected()

            self.is_changed = False

    # TODO this doesn't work
    def update_selected(self):
        if self.rect.collidepoint(self.mouse_position[0], self.mouse_position[1]):
            print('mouse update event triggered')
            self.is_selected = True
            self.is_changed = True

    def render_selected(self):
        width = 1
        selected_color = pygame.Color("red")
        pygame.draw.rect(self.surface, selected_color, self.rect, width)