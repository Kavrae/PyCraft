from .BotTemplate import BotTemplate


class ExampleBot(BotTemplate):
    name = "Example Bot"
    race = "Human"  # TODO how to enforce this and show all options? Registration method of some kind maybe?

    def run(self):
        mana = self._game_library.get_mana(self._bot_id)
        if mana > 0:
            unit_name = "Warrior"
            location = (0, mana)
            self._game_library.summon(self._bot_id, unit_name, location)
