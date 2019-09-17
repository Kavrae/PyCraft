from GameLibrary.ExampleLibrary import ExampleLibrary


# TODO way for a bot to figure out its mana and other properties from the BotData. Maybe a call to the library with id?
class ExampleBot:
    _game_library = None

    _i = 10

    def __init__(self, game_library):
        self._game_library = game_library  # TODO move this to super_class init instead. Just make them inherit from a parent bot

    def run(self):
        self._game_library.summon(id(self), 5, (0, self._i))
        self._i += 1
