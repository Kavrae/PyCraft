#!/usr/bin/env python
import pygame

from Views import GameScreen
from MapFactory import MapFactory  # Why is this angry? Confused. Doesn't work with .MapFactory like everything else
from GameState.GameState import GameState
from GameLibrary.ExampleLibrary import ExampleLibrary
from Bots.ExampleBot import ExampleBot  #  TODO figure out how to dynamically import all bots at runtime (do int _init__.py)


# TODO register bots
# TODO generate map based on user or random selection
# TODO game engine instantiation
class GameRunner:
    _gameState = None
    _mapFactory = None
    _gameScreen = None
    _gameLibrary = None

    _clock = None
    _fps = None

    def __init__(self):
        pygame.init()
        pygame.mixer = None  # handles sound
        pygame.display.set_caption('PyCraft')

        self.initialize_clock()
        self.initialize_map_factory()
        self.initialize_game_state()
        self._gameLibrary = ExampleLibrary(self._gameState)  # TODO proper library initialization
        self.initialize_bots()

        self._gameScreen = GameScreen(self._clock, self._gameState)

    def run(self):
        # TODO got input parsing
        for bot_data in self._gameState._bots:
            bot_data._bot.run()
        # TODO game engine's "turn" (resource growth, wild animals, natural events, etc)
        self.clock_tick()
        self._gameScreen.update()
        self._gameScreen.render()

        # Hack - prevent windows "not responding" timeouts
        # TODO move this when I start to handle user events, such as using menus (if any)
        pygame.event.get()

    def initialize_clock(self):
        self._clock = pygame.time.Clock()
        self._fps = 60

    # TODO map seeds
    def initialize_map_factory(self):
        self._mapFactory = MapFactory()

    def initialize_game_state(self):
        self._gameState = GameState()

        self._gameState.set_terrain_map(self._mapFactory.generate_example_map())

    # todo parse bots and bot_wrappers
    def initialize_bots(self):
        # TODO increment each bot id by 1
        # TODO pull by indexer. More efficient than artificial id
        self._gameState.add_bot(ExampleBot(0, self._gameLibrary))
        self._gameState.add_bot(ExampleBot(1, self._gameLibrary))

    def clock_tick(self):
        self._clock.tick(self._fps)


# TODO error handling wrapper
gameRunner = GameRunner()
while True:
    gameRunner.run()
pygame.quit
