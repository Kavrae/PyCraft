class BotData:
    _bot_id = None
    _mana = None
    _entities = None

    def __init__(self, bot):  # todo parse bot into bot_data
        self._bot_id = id(bot)
        self._mana = 10
        self._entities = []