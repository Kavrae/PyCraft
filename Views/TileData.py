import pygame
from pygame.locals import *
from Views.Tile import Tile


# TODO figure out how to get this to pull data from every other view and other places
class TileData:
    font = None
    rect = None
    surface = None
    background_color = None

    selected_tile: Tile = None

    def __init__(self, rect: Rect, background_color: tuple = (0, 0, 0)):
        self.rect = rect
        self.background_color = background_color
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(background_color)

        self.initialize_fonts()

    def initialize_fonts(self):
        font_name = 'helvetica'
        stats_font_size = 14
        self.font = pygame.font.SysFont(font_name, stats_font_size)

    def update(self):
        test = 1

    # TODO replace with information from the entity and terrain game objects inside the tile instead of the tile itself
    def render(self):
        self.display_data_rows([self.display_tile_name()])

    def set_selected_tile(self, tile):
        self.selected_tile = tile

    def display_data_rows(self, data_surfaces):
        row_num = 0
        background_color = self.background_color
        height = 16
        width = self.rect.width

        for data_surface in data_surfaces:
            row_surface = pygame.Surface((width, height))
            row_surface.fill(background_color)

            data_rect = data_surface.get_rect()
            row_surface.blit(data_surface, data_rect)

            self.surface.blit(row_surface, Rect(0, row_num * height, width, height))
            row_num += 1

    def display_tile_name(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "No Tiles Selected" if self.selected_tile is None else self.selected_tile.entity_value
        return self.font.render(text, antialias, text_color, self.background_color)
