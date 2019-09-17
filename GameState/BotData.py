class BotData:
    _bot = None
    _mana = None
    _entities = None  # TODO Create entity and terrain objects for the GameLibrary and GameState to use.
                      # Then when moving to the view, combine them into an entity_map. Should NEVER overlap (no flying...)


    def __init__(self, bot):
        self._bot = bot
        self._mana = 10
        self._entities = []