from .BotData import BotData


class GameState:
    # TODO bot_wrappers each contain a bot.
    # bot wrappers contain data about that bot that cannot be directly changed by the bots, such as their entity states
    # bots call the game library. Game library changes bot_wrapper inside gameState
    _bots = None
    _terrain_map = None

    def __init__(self):
        self._bots = []

    def set_terrain_map(self, terrain_map):
        self._terrain_map = terrain_map

    def add_bot(self, bot):
        self._bots.append(BotData(bot))

    # TODO use a proper filter. Does this work on id? is it slow?
    def get_bot(self, bot_id):
        for bot in self._bots:
            if id(bot == bot_id):
                return bot
        return None
