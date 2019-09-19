from Views.ViewObjects import EntityFactory
from .BotData import BotData
import random


class GameState:
    def __init__(self):
        self._bots = []

    @property
    def bots(self): return self._bots

    @property
    def terrain_map(self): return self._terrain_map

    @terrain_map.setter
    def terrain_map(self, new_map):
        self._terrain_map = new_map

    def add_bot(self, bot):
        self._bots.append(BotData(bot))

    def get_bot_data(self, bot_id):
        if len(self._bots) > bot_id:
            return self._bots[bot_id]
        return None

    # TODO use actual coordinates, not random
    # TODO Move this to the map factory or view utility file?
    def generate_view_entity_map(self):
        entity_map = []
        for x in range(0, len(self.terrain_map)):
            row = []
            for y in range(0, len(self.terrain_map[0])):
                row.append(None)
            entity_map.append(row)

        for bot in self.bots:
            for entity in bot.entities:
                if entity.position is None:
                    entity.position = (random.randint(0, len(self.terrain_map)), random.randint(0, len(self.terrain_map[0])))

                # TODO Maybe switch this to a constructor instead
                entity_map[entity.position[0]][entity.position[1]] = EntityFactory.library_entity_to_view_entity(entity)
        return entity_map
