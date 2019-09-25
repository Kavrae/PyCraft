from .BotData import BotData
import numpy


class GameState:
    def __init__(self):
        self._bots = []
        self._units = []
        self._terrain_map = None
        self._unit_map = None

        self._units_changed = True

    @property
    def bots(self): return self._bots

    @property
    def units(self): return self._units

    def add_unit(self, unit):
        self._units.append(unit)
        self._units_changed = True

    @property
    def terrain_map(self): return self._terrain_map

    @terrain_map.setter
    def terrain_map(self, new_map): self._terrain_map = new_map

    def add_bot(self, bot):
        new_bot_data = BotData(bot)
        self._bots.append(new_bot_data)

    def get_bot_data(self, bot_id):
        if len(self._bots) > bot_id:
            return self._bots[bot_id]
        return None

    def get_unit(self, unit_id):
        if len(self._units) > unit_id:
            return self._units[unit_id]
        return None

    # TODO Move this to the map factory or view utility file?
    # TODO manually move things around the map when they move/die/created?
    def generate_unit_map(self):
        if self._units_changed:
            self._unit_map = numpy.full([100, 100], fill_value=None)
            for unit in self._units:
                self._unit_map[unit.location[0], unit.location[1]] = unit
            self._units_changed = False
        return self._unit_map
