from .BotTemplate import BotTemplate
import random


class ExampleBot(BotTemplate):
    name = "Example Bot"
    race = "Human"
    _my_unit_ids = []

    def run(self):
        mana = self._game_library.get_mana(self._bot_id)
        map_size = self._game_library.get_map_size()
        if mana > 0:
            unit_name = "Warrior"
            location = (random.randint(0, map_size[0] - 1), random.randint(0, map_size[1] - 1))
            new_unit_id = self._game_library.summon(self._bot_id, unit_name, location)
            self._my_unit_ids.append(new_unit_id)
