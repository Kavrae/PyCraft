#!/usr/bin/env python
import pygame
from pygame.locals import *
from Views.Battlefield import Battlefield
from Views.GameData import GameData
from Views.TileData import TileData


# TODO abstract view sizes into GameScreen properties + math to making changing them easier.
# TODO pass in a terrain map object instead of instantiating it
# TODO pass in an entity map object instead of instantiating it
# TODO overlap these maps for the battlefield
class GameScreen:
    clock = None
    fps = None

    screen: pygame.Surface = None
    screen_rect: Rect = None

    battlefield: Battlefield = None
    game_data: GameData = None
    tile_data: TileData = None

    terrain_map = None
    entity_map = None

    def __init__(self):
        pygame.init()
        pygame.mixer = None  # handles sound
        pygame.display.set_caption('PyCraft')

        self.initialize_clock()
        self.initialize_screen()
        self.initialize_maps()
        self.initialize_battlefield()
        self.initialize_game_data()
        self.initialize_tile_data()

        self.timer()
        self.update()
        self.render()

    def initialize_clock(self):
        self.clock = pygame.time.Clock()
        self.fps = 60

    def initialize_screen(self):
        self.screen_rect = Rect(0, 0, 650, 480)
        window_style = 0

        best_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        self.screen = pygame.display.set_mode(self.screen_rect.size, window_style, best_depth)
        self.screen.fill((0, 0, 0))

    def initialize_battlefield(self):
        rect = Rect(0, 0, int(self.screen_rect.width * 0.8), self.screen_rect.height)
        tile_size = 12
        background_color = (0, 0, 0)
        self.battlefield = Battlefield(rect, tile_size, self.terrain_map, self.entity_map, background_color)

    def initialize_game_data(self):
        rect = Rect(int(self.screen_rect.width * 0.8), 0,
                    int(self.screen_rect.width * 0.2), int(self.screen_rect.height * 0.5))
        background_color = (240, 240, 240)
        self.game_data = GameData(rect, self.clock, background_color)

    def initialize_tile_data(self):
        rect = Rect(int(self.screen_rect.width * 0.8), int(self.screen_rect.height * 0.5),
                    int(self.screen_rect.width * 0.2), int(self.screen_rect.height * 0.5))

        background_color = (240, 240, 240)
        self.tile_data = TileData(rect, background_color)

    # TODO this will eventually go away in favor of a map builder to generate default or randomized maps
    def initialize_maps(self):
        temp_map = []
        for row in range(100):
            new_row = []
            for column in range(30, 126):
                index = row + column
                while index > 126:
                    index -= 96
                new_row.append(chr(index))
            temp_map.append(new_row)

        self.terrain_map = temp_map.copy()
        self.entity_map = temp_map.copy()

    def timer(self):
        self.clock.tick(self.fps)

    def update(self):
        self.battlefield.update()
        selected_tile = self.battlefield.get_selected_tile()

        self.game_data.update()

        self.tile_data.set_selected_tile(selected_tile)
        self.tile_data.update()

    def render(self):
        self.battlefield.render()
        self.game_data.render()
        self.tile_data.render()

        self.screen.blits(((self.battlefield.surface, self.battlefield.rect.topleft),
                           (self.game_data.surface, self.game_data.rect.topleft),
                           (self.tile_data.surface, self.tile_data.rect.topleft)))

        pygame.display.flip()


# TODO replace with game runner
gameScreen = GameScreen()
while True:
    gameScreen.timer()
    gameScreen.update()
    gameScreen.render()

    # Hack - prevent windows "not responding" timeouts
    # TODO move this when I start to handle user events, such as using menus (if any)
    pygame.event.get()
pygame.quit
