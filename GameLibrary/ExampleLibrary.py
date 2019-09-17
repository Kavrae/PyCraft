class ExampleLibrary:
    _game_state = None

    def __init__(self, game_state):
        self._game_state = game_state  # TODO does this actually act as a reference type and change?

    def summon(self, bot_id, unit_id, location):
        bot_data = self._game_state.get_bot(bot_id)  # TODO does this work by reference as well?

        if bot_data._mana > 0:
            bot_data._mana -= 1
            bot_data._entities.append(unit_id)  # TODO call unit factory for the given race, passing in location IF VALID

            print("Unit {0} added to example bot".format(unit_id))
