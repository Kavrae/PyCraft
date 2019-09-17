from .BotData import BotData


class GameState:
    _bots = None
    _terrain_map = None

    def __init__(self):
        self._bots = []

    def set_terrain_map(self, terrain_map):
        self._terrain_map = terrain_map

    def add_bot(self, bot):
        self._bots.append(BotData(bot))

    # TODO use a proper filter. Does this work on id? is it slow?
    def get_bot_data(self, bot_id):
        for bot_data in self._bots:
            if id(bot_data._bot) == bot_id:
                return bot_data
        return None
