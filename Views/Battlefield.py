import pygame
from pygame.locals import *
import numpy


class Battlefield:
    font = None
    rect = None
    surface = None

    tile_size = None

    #todo change maps to a class
    # includes arrays of objects
    # includes map size
    # maybe various other helper functions
    terrain_map = None
    terrain_map_size = None
    entity_map = None
    render_map = None

    tiles_horizontal = None
    tiles_vertical = None

    cursor_position = None

    def __init__(self, rect: pygame.Rect = (0, 0, 0, 0), tile_size: int = 10, background_color: tuple = (0, 0, 0)):
        self.rect = rect
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(background_color)
        self.tile_size = tile_size

        self.tiles_horizontal = int(rect.width / self.tile_size)
        self.tiles_vertical = int(rect.height / self.tile_size)

        self.initialize_cursor()
        self.initialize_fonts()

    # Place cursor in the center of the screen
    # TODO outline cursor
    def initialize_cursor(self):
        self.cursor_position = (int(self.tiles_horizontal / 2), int(self.tiles_vertical / 2))

    def initialize_fonts(self):
        battlefield_font_name = 'freesansbold.ttf'
        battlefield_font_size = 11
        self.font = pygame.font.Font(battlefield_font_name, battlefield_font_size)

    def set_terrain_map(self, terrain_map):
        self.terrain_map = terrain_map
        self.terrain_map_size = (len(terrain_map), len(terrain_map[0]))

    def set_entity_map(self, entity_map):
        self.entity_map = entity_map

    # TODO combine maps into a renderable map
    #  This map would simply replace terrain values with non-null entity values
    def update(self):
        self.update_cursor()

    # TODO Stop moving the map when it hits the boundaries
    def render(self):
        # Set the starting point for reading the map
        # Clamp it based on the size of the cursor so that it stops moving past those values
        left_start = int(self.cursor_position[0] - (self.tiles_horizontal / 2))
        left_start = sorted((0, left_start, self.terrain_map_size[0] - self.tiles_horizontal))[1]

        top_start = int(self.cursor_position[1] - (self.tiles_vertical / 2))
        top_start = sorted((0, top_start, self.terrain_map_size[1] - self.tiles_vertical))[1]

        for left in range(left_start, left_start + self.tiles_horizontal):
            for top in range(top_start, top_start + self.tiles_vertical):
                tile_position = ((left - left_start) * self.tile_size, (top - top_start) * self.tile_size)
                tile_rect = Rect(tile_position[0], tile_position[1], self.tile_size, self.tile_size)
                tile_value = self.terrain_map[top][left]
                self.write_tile(tile_rect, tile_value)

        self.render_cursor()

    # TODO this eventually needs to be moved to a cursor object embedded or separate from the battlefield
    # TODO Cursor moves off center as expected when it hits the edge
    #   BUT it needs to not move at all if the map has moved.
    #   Need to share state between the two to know when to move the cursor and when not to move it.
    #   Also need to determine what is under the cursor easily.
    # TODO might be easier just to do mouse-based movements and click-to-view-data
    def update_cursor(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.cursor_position = (
                    numpy.clip(0, self.tiles_horizontal, self.cursor_position[0])
                    , numpy.clip(0, self.tiles_vertical, self.cursor_position[1] - 1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.cursor_position = (
                    numpy.clip(0, self.tiles_horizontal, self.cursor_position[0])
                    , numpy.clip(0, self.tiles_vertical, self.cursor_position[1] + 1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.cursor_position = (
                    numpy.clip(0, self.tiles_horizontal, self.cursor_position[0] - 1)
                    , numpy.clip(0, self.tiles_vertical, self.cursor_position[1]))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.cursor_position = (
                    numpy.clip(0, self.tiles_horizontal, self.cursor_position[0] + 1)
                    , numpy.clip(0, self.tiles_vertical, self.cursor_position[1]))

    def render_cursor(self):
        cursor_color = (255, 0, 0)
        cursor_rect = Rect(self.cursor_position[0] * self.tile_size, self.cursor_position[1] * self.tile_size, self.tile_size, self.tile_size)
        width = 1
        pygame.draw.rect(self.surface, cursor_color, cursor_rect, width)

    # TODO change to call write_tile on each object
    # which then returns a text character and color
    # to be passed into the common write_tile method
    def write_tile(self, tile_rect: Rect, text):
        # Create Tile surface
        tile_color = (0, 0, 0)
        tile_surface = pygame.Surface(tile_rect.size)
        tile_surface.fill(tile_color)

        # Create Font surface
        antialias = True
        text_color = (0, 175, 0)
        font_surface = self.font.render(text, antialias, text_color, tile_color)
        font_rect = font_surface.get_rect()
        font_rect.center = (tile_rect.width / 2, tile_rect.height / 2)

        # Add font to tile. Add tile to screen
        tile_surface.blit(font_surface, font_rect)
        self.surface.blit(tile_surface, tile_rect)
