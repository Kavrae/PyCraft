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

    is_first_render = None
    is_selected = None
    is_changed = None
    
    def __init__(self, rect: Rect, terrain_value, entity_value, font, mouse_position: tuple, background_color: tuple = pygame.Color("black")):
        self.rect = rect
        self.terrain_value = terrain_value
        self.entity_value = entity_value
        self.font = font
        self.mouse_position = mouse_position
        self.background_color = background_color

        self.is_first_render = True
        self.is_selected = False
        self.is_changed = True

        self.surface = pygame.Surface(self.rect.size)
        self.surface.fill(self.background_color)

    def update(self):
        self.update_selected()

    # TODO change this to determine which value to use. entity > terrain > blank
    def render(self):
        if self.is_changed:
            # Reset Tile
            self.surface.fill(self.background_color)

            # Create Font surface
            antialias = True
            text_color = (0, 175, 0)
            font_surface = self.font.render(self.terrain_value, antialias, text_color, self.background_color)
            font_rect = font_surface.get_rect()
            font_rect.center = (self.rect.width / 2, self.rect.height / 2)

            # Add font to tile.
            self.surface.blit(font_surface, font_rect)

            # Add selected box highlight to tile
            if self.is_selected:
                self.render_selected()

    def update_selected(self):
        # Skip all selection logic when first creating the tile
        if self.is_first_render:
            self.is_first_render = False
            return

        if self.mouse_position is not None:
            if self.rect.collidepoint(self.mouse_position[0], self.mouse_position[1]):
                # Do not update tile if the mouse was hover over it and still is
                if self.is_selected:
                    self.is_selected = True
                    self.is_changed = False
                # Update tile if the mouse is hovering over it and wasn't before
                else:
                    self.is_selected = True
                    self.is_changed = True
            else:
                # Reset tile if it was previously selected but no longer is
                if self.is_selected:
                    self.is_selected = False
                    self.is_changed = True
                # Do nothing if the tile wasn't selected and still isn't
                else:
                    self.is_changed = False
                    self.is_selected = False

    def render_selected(self):
        width = 1
        selected_color = pygame.Color("red")
        rect = Rect(0, 0, self.rect.width, self.rect.height)
        pygame.draw.rect(self.surface, selected_color, rect, width)
