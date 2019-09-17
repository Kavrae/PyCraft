from .BotTemplate import BotTemplate


class ExampleBot(BotTemplate):
    _i = 10
    # TODO how to set things like race? That determines which units can be used. Register method?

    def run(self):
        mana = self._game_library.get_mana(id(self))  # TODO redo this with change to object in bot_data.How?
        if mana > 0:
            self._game_library.summon(id(self), 5, (0, self._i))
            self._i -= 1
