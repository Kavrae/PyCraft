from .StatusEffect import StatusEffect


class Poisoned(StatusEffect):
    def __init__(self):
        self._name = "Poisoned"
        self._start_duration = 5
        self._ticks_remaining = self._start_duration

        self._damage_per_tick = 1
        # TODO change text color of unit to lime green

    def run(self):
        self._ticks_remaining -= 1
        # TODO remove x hp from target
        if self._ticks_remaining == 0:
            self.on_removed()
            # TODO need some way from outside of this class to remove it from the unit
            # Maybe a flag of some kind indicating that it needs removed?

    def on_added(self):
        print('Poisoned')

    def on_removed(self):
        print('No longer poisoned')
        # TODO change unit text color back