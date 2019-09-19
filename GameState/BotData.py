class BotData:
    def __init__(self, bot):
        self._bot = bot
        self._mana = 10
        self._entities = []
        self._race = bot.race

    @property
    def bot(self):
        return self._bot

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value >= 0:
            self._mana = value
        else:
            raise ValueError("Mana cannot go below 0")  # TODO automatically make a bot lose if it throws an exception

    # TODO Create entity and terrain objects for the GameLibrary and GameState to use.
    # Then when moving to the view, combine the entities into an entity_map. Should NEVER overlap (no flying...)
    @property
    def entities(self):
        return self._entities

    @property
    def race(self):
        return self._race

    # TODO add map position to add it at
    def add_entity(self, entity):
        if entity is not None:
            self._entities.append(entity)
