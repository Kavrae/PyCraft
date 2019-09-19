from .LibraryObjects.Units.UnitFactory import UnitFactory


class ExampleLibrary:
    _game_state = None
    _unit_factory = None

    def __init__(self, game_state):
        self._game_state = game_state
        self._unit_factory = UnitFactory(game_state)

    def get_mana(self, bot_id):
        bot_data = self._game_state.get_bot_data(bot_id)
        return bot_data.mana

    def get_map_size(self):
        terrain_map = self._game_state.terrain_map
        return len(terrain_map), len(terrain_map[0])

    def summon(self, bot_id, unit_type, location):
        bot_data = self._game_state.get_bot_data(bot_id)

        if bot_data.mana > 0:
            bot_data.mana -= 1
            self._game_state.add_unit(self._unit_factory.create_new_unit(bot_id, bot_data.race, unit_type, "Alive", location))
