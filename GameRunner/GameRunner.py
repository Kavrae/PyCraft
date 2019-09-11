#!/usr/bin/env python
import pygame

from MapFactory import MapFactory
from Views.GameScreen import GameScreen


# TODO register bots
# TODO generate map based on user or random selection
# TODO game engine instantiation
class GameRunner:
    _mapFactory = None
    _gameScreen = None

    _clock = None
    _fps = None

    def __init__(self):
        pygame.init()
        pygame.mixer = None  # handles sound
        pygame.display.set_caption('PyCraft')

        self.initialize_clock()

        self._mapFactory = MapFactory()
        default_terrain_map = self._mapFactory.generate_example_map()
        default_entity_map = self._mapFactory.generate_example_entities()

        self._gameScreen = GameScreen(self._clock,
                                      default_terrain_map,
                                      default_entity_map)

    def run(self):
        # TODO got input parsing
        # TODO game engine run bot input
        # TODO game engine's "turn"
        self.clock_tick()
        self._gameScreen.update()
        self._gameScreen.render()

        # Hack - prevent windows "not responding" timeouts
        # TODO move this when I start to handle user events, such as using menus (if any)
        pygame.event.get()

    def initialize_clock(self):
        self._clock = pygame.time.Clock()
        self._fps = 60

    def clock_tick(self):
        self._clock.tick(self._fps)


# TODO error handling wrapper
gameRunner = GameRunner()
while True:
    gameRunner.run()
pygame.quit
