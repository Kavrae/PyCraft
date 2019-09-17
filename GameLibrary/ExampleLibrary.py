class ExampleLibrary:
    _game_state = None

    def __init__(self, game_state):
        self._game_state = game_state

    def get_mana(self, bot_id):
        bot_data = self._game_state.get_bot_data(bot_id)
        return bot_data._mana

    def summon(self, bot_id, unit_id, location):
        bot_data = self._game_state.get_bot_data(bot_id)

        if bot_data._mana > 0:
            bot_data._mana -= 1
            bot_data._entities.append(unit_id)  # TODO call unit factory for the given race, passing in location IF VALID
