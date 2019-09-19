from .LibraryObjects.Entities.EntityFactory import EntityFactory


class ExampleLibrary:
    _game_state = None

    def __init__(self, game_state):
        self._game_state = game_state

    def get_mana(self, bot_id):
        bot_data = self._game_state.get_bot_data(bot_id)
        return bot_data.mana

    def summon(self, bot_id, unit, location):
        bot_data = self._game_state.get_bot_data(bot_id)

        if bot_data.mana > 0:
            bot_data.mana -= 1
            bot_data.add_entity(EntityFactory.create_new_unit(bot_data.race, unit, "Alive"))
