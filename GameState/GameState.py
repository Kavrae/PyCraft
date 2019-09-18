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

    def get_bot_data(self, bot_id):
        if len(self._bots) > bot_id:
            return self._bots[bot_id]
        return None
