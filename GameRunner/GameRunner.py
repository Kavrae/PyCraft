#!/usr/bin/env python
import pygame

from Views import GameScreen
from GameState.GameState import GameState
from GameLibrary.ExampleLibrary import ExampleLibrary
from GameLibrary.MapFactory import MapFactory
from Bots.ExampleBot import ExampleBot  #  TODO figure out how to dynamically import all bots at runtime (do in _init__.py)


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

    _paused = None

    def __init__(self):
        pygame.init()
        pygame.mixer = None  # handles sound
        pygame.display.set_caption('PyCraft')

        self._paused = False

        self.initialize_clock()
        self.initialize_map_factory()
        self.initialize_game_state()
        self._gameLibrary = ExampleLibrary(self._gameState)  # TODO proper library initialization
        self.initialize_bots()

        self._gameScreen = GameScreen(self._clock, self._gameState)

    def run(self):
        self.get_user_input()

        if not self._paused:
            self.run_status_effects()
            self.run_bots()
            # TODO game engine's "turn" (resource growth, wild animals, natural events, etc)
            self.clock_tick()

        self._gameScreen.update()
        self._gameScreen.render()

    def initialize_clock(self):
        self._clock = pygame.time.Clock()
        self._fps = 180

    # TODO map seeds
    def initialize_map_factory(self):
        self._mapFactory = MapFactory()

    def initialize_game_state(self):
        self._gameState = GameState()
        self._gameState.terrain_map = self._mapFactory.generate_example_map()

    # TODO parse bots and bot_wrappers
    def initialize_bots(self):
        self._gameState.add_bot(ExampleBot(0, self._gameLibrary))
        self._gameState.add_bot(ExampleBot(1, self._gameLibrary))

    def clock_tick(self):
        self._clock.tick(self._fps)

    def get_user_input(self):
        for event in pygame.event.get():
            # Pause Button (spacebar)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._paused = not self._paused

            # Graceful program close
            elif event.type == pygame.QUIT:
                raise SystemExit

    def run_status_effects(self):
        for unit in self._gameState.units:
            for status_effect in unit._status_effects:
                status_effect.run()

    def run_bots(self):
        for bot_data in self._gameState.bots:
            bot_data.bot.run()


# TODO error handling wrapper
gameRunner = GameRunner()
while True:
    gameRunner.run()
