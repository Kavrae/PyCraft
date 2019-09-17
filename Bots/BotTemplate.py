class BotTemplate:
    _game_library = None

    def __init__(self, game_library):
        self._game_library = game_library

    def run(self):
        print('Provide an implementation of the "run" method in your bot.')
