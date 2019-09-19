class BotData:
    def __init__(self, bot):
        self._bot = bot
        self._mana = 10
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

    @property
    def race(self):
        return self._race
