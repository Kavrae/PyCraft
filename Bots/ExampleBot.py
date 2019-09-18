from .BotTemplate import BotTemplate


class ExampleBot(BotTemplate):
    # TODO how to set things like race? That determines which units can be used. Register method?
    _name = "Example Bot"

    def run(self):
        mana = self._game_library.get_mana(self._bot_id)
        if mana > 0:
            self._game_library.summon(self._bot_id, 5, (0, mana))
