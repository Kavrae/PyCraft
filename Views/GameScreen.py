import pygame
from pygame.locals import *
from .Battlefield import Battlefield
from .GameData import GameData
from .TileData import TileData
from GameState import GameState


# TODO abstract view sizes into GameScreen properties + math to making changing them easier.
class GameScreen:
    _screen: pygame.Surface = None
    _screen_rect: Rect = None

    _game_state: GameState = None

    _battlefield: Battlefield = None
    _game_data: GameData = None
    _tile_data: TileData = None

    def __init__(self, clock, game_state):
        self._game_state = game_state
        self.initialize_screen()
        self.initialize_battlefield()
        self.initialize_game_data(clock)
        self.initialize_tile_data()

        self.update()
        self.render()

    def initialize_screen(self):
        self._screen_rect = Rect(0, 0, 960, 680)
        window_style = 0

        best_depth = pygame.display.mode_ok(self._screen_rect.size, window_style, 32)
        self._screen = pygame.display.set_mode(self._screen_rect.size, window_style, best_depth)
        self._screen.fill((0, 0, 0))

    def initialize_battlefield(self):
        rect = Rect(0, 0, int(self._screen_rect.width * 0.8), self._screen_rect.height)
        tile_size = 12
        background_color = (0, 0, 0)
        terrain_map = self._game_state._terrain_map
        unit_map = self._game_state.generate_view_unit_map()
        self._battlefield = Battlefield(rect, tile_size, terrain_map, unit_map, background_color)

    def initialize_game_data(self, clock):
        rect = Rect(int(self._screen_rect.width * 0.8), 0,
                    int(self._screen_rect.width * 0.2), int(self._screen_rect.height * 0.5))
        background_color = (240, 240, 240)
        self._game_data = GameData(rect, clock, background_color)

    def initialize_tile_data(self):
        rect = Rect(int(self._screen_rect.width * 0.8), int(self._screen_rect.height * 0.5),
                    int(self._screen_rect.width * 0.2), int(self._screen_rect.height * 0.5))

        background_color = (240, 240, 240)
        self._tile_data = TileData(rect, background_color)

    def update_maps(self, terrain_map, unit_map):
        self._battlefield.terrain_map = terrain_map
        self._battlefield.unit_map = unit_map

    def update(self):
        self._battlefield.update(self._game_state)
        selected_tile = self._battlefield.get_selected_tile()

        self._game_data.update()

        self._tile_data.set_selected_tile(selected_tile)
        self._tile_data.update()

    def render(self):
        self._battlefield.render()
        self._game_data.render()
        self._tile_data.render()

        self._screen.blits(((self._battlefield.surface, self._battlefield.rect.topleft),
                            (self._game_data.surface, self._game_data.rect.topleft),
                            (self._tile_data.surface, self._tile_data.rect.topleft)))

        pygame.display.flip()
