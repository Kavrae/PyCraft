class BotTemplate:
    _game_library = None
    _bot_id = None

    def __init__(self, bot_id, game_library):
        self._game_library = game_library
        self._bot_id = bot_id

    def run(self):
        print('Provide an implementation of the "run" method in your bot.')