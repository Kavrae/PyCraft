#!/usr/bin/env python
import time
import pygame
import numpy
from pygame.locals import *


# TODO surface outlines for different screen areas
# TODO pass in a terrain map object instead of instantiating it
# TODO pass in an entity map object instead of instantiating it
# TODO overlap these maps for the battlefield
# TODO move different Surfaces into their own classes
class GameScreen:
    def __init__(self):
        self._screen = None
        self._screen_rect = None

        self._battlefield = None
        self._battlefield_rect = None
        self._battlefield_tile_size = 12
        self._battlefield_tiles_horizontal = None
        self._battlefield_tiles_vertical = None

        self._gamedata = None
        self._gamedata_rect = None

        self._tileinfo = None
        self._tileinfo_rect = None

        self._terrain_map = None
        self._entity_map = None

        self._viewer_position = None

        pygame.init()
        pygame.mixer = None     # handles sound
        pygame.display.set_caption('PyCraft')

        self.initialize_screen()
        self.initialize_battlefield()
        self.initialize_gamedata()
        self.initialize_tileinfo()
        self.initialize_viewer()
        self.initialize_maps()

    def initialize_screen(self):
        self._screen_rect = Rect(0, 0, 650, 480)
        window_style = 0

        best_depth = pygame.display.mode_ok(self._screen_rect.size, window_style, 32)
        self._screen = pygame.display.set_mode(self._screen_rect.size, window_style, best_depth)
        self._screen.fill((0, 0, 0))

    def initialize_battlefield(self):
        self._battlefield_rect = Rect(0, 0, int(self._screen_rect.width * 0.65), self._screen_rect.height)

        self._battlefield = pygame.Surface(self._battlefield_rect.size)
        self._battlefield.fill((0, 255, 0))

        self._battlefield_tiles_horizontal = int(self._battlefield_rect.width / self._battlefield_tile_size)
        self._battlefield_tiles_vertical = int(self._battlefield_rect.height / self._battlefield_tile_size)

    def initialize_gamedata(self):
        self._gamedata_rect = Rect(int(self._screen_rect.width * 0.65), 0,
                                   int(self._screen_rect.width * 0.35), int(self._screen_rect.height * 0.5))

        self._gamedata = pygame.Surface(self._gamedata_rect.size)
        self._gamedata.fill((0, 255, 255))

    def initialize_tileinfo(self):
        self._tileinfo_rect = Rect(int(self._screen_rect.width * 0.65), int(self._screen_rect.height * 0.5),
                                   int(self._screen_rect.width * 0.35), int(self._screen_rect.height * 0.5))

        self._tileinfo = pygame.Surface(self._tileinfo_rect.size)
        self._tileinfo.fill((0, 0, 255))

    def initialize_viewer(self):
        self._viewer_position = (int(self._battlefield_tiles_horizontal / 2), int(self._battlefield_tiles_vertical / 2))
        print(self._viewer_position)

    def initialize_maps(self):
        temp_map = []
        for row in range(100):
            new_row = []
            for column in range(100):
                new_row.append(str(column))
            temp_map.append(new_row)
        self._terrain_map = temp_map.copy()
        self._entity_map = temp_map.copy()

    def update(self):
        self.update_viewer()
        self.update_battlefield()
        #update gamedata
        #update tileinfo

        self._screen.blit(gameScreen._battlefield, self._battlefield_rect.topleft)
        self._screen.blit(gameScreen._gamedata, self._gamedata_rect.topleft)
        self._screen.blit(gameScreen._tileinfo, self._tileinfo_rect.topleft)

        pygame.display.flip()

    #TODO left and right now working? Unsure. maybe it's an issue with the tile color instead
    #TODO stop moving the map when it hits 0/0. Don't go negative when selecting the map coordinate
    #update timing is also weird
    def update_viewer(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self._viewer_position = (numpy.clip(0, self._battlefield_tiles_horizontal, self._viewer_position[0])
                                         , numpy.clip(0, self._battlefield_tiles_vertical, self._viewer_position[1] - 1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self._viewer_position = (numpy.clip(0, self._battlefield_tiles_horizontal, self._viewer_position[0])
                                         , numpy.clip(0, self._battlefield_tiles_vertical, self._viewer_position[1] + 1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self._viewer_position = (numpy.clip(0, self._battlefield_tiles_horizontal, self._viewer_position[0] - 1)
                                         , numpy.clip(0, self._battlefield_tiles_vertical, self._viewer_position[1]))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self._viewer_position = (numpy.clip(0, self._battlefield_tiles_horizontal, self._viewer_position[0] + 1)
                                         , numpy.clip(0, self._battlefield_tiles_vertical, self._viewer_position[1]))

    #TODO if the offset would put it below 0 or above the map size
    # then change the offset. Clipping the final value will result in repeats
    def update_battlefield(self):
        left_offset = int(self._viewer_position[0] - (self._battlefield_tiles_horizontal / 2))
        top_offset = int(self._viewer_position[1] - (self._battlefield_tiles_vertical / 2))

        for left in range(self._battlefield_tiles_horizontal):
            for top in range(self._battlefield_tiles_vertical):
                tile_rect = Rect(left * self._battlefield_tile_size, top * self._battlefield_tile_size,
                                 self._battlefield_tile_size, self._battlefield_tile_size)
                tile_value = self._terrain_map[left + left_offset][top + top_offset]
                self.write_tile(tile_rect, tile_value)

    # TODO change to call write_tile on each object
    # which then returns a text character and color
    # to be passed into the common write_tile method
    # TODO remove background color to a common color after fixing text and size
    def write_tile(self, tile_rect: Rect, text):
        # Create Tile surface
        tile_color = (255, 255, 255) if (tile_rect.left + tile_rect.top) % (tile_rect.width * 2) == 0 else (0, 0, 0)
        tile_surface = pygame.Surface(tile_rect.size)
        tile_surface.fill(tile_color)

        # Create Font surface
        antialias = True
        text_color = (255, 0, 0)
        font_size = 10
        font_name = 'freesansbold.ttf'
        font = pygame.font.Font(font_name, font_size)
        font_surface = font.render(text, antialias, text_color, tile_color)
        font_rect = font_surface.get_rect()
        font_rect.center = (tile_rect.width / 2, tile_rect.height / 2)

        # Add font to tile. Add tile to screen
        tile_surface.blit(font_surface, font_rect)
        self._battlefield.blit(tile_surface, tile_rect)


gameScreen = GameScreen()
while True:
    gameScreen.update()
    time.sleep(0.02)
pygame.quit
