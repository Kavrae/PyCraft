import pygame
from pygame.locals import *

from Views.ViewObjects.Tile import Tile


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
        pass

    def render(self):
        self.display_data_rows([self.display_tile_name(),
                                self.display_tile_status()])

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
        if self.selected_tile is None:
            text = "No Tiles Selected"
        elif self.selected_tile.entity is not None:
            text = self.selected_tile.entity.name
        else:
            text = self.selected_tile.terrain.name
        return self.font.render(text, antialias, text_color, self.background_color)

    def display_tile_status(self):
        antialias = True
        text_color = (0, 0, 0)
        if self.selected_tile is None:
            text = ""
        elif self.selected_tile.entity is not None:
            text = self.selected_tile.entity.status
        else:
            text = self.selected_tile.terrain.status
        return self.font.render(text, antialias, text_color, self.background_color)
