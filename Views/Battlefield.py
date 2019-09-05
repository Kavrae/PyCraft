import pygame
from pygame.locals import *
from Views.Tile import Tile


class Battlefield:
    font = None
    rect = None
    surface = None
    background_color = None

    tile_size = None
    tiles = None

    # TODO change maps to a class
    # includes arrays of objects
    # includes map size
    # maybe various other helper functions
    terrain_map = None
    terrain_map_size = None
    entity_map = None
    entity_map_size = None

    tiles_horizontal = None
    tiles_vertical = None

    mouse_position = None

    def __init__(self, rect: pygame.Rect, tile_size: int, terrain_map, entity_map, background_color: tuple):
        self.rect = rect
        self.tile_size = tile_size
        self.background_color = background_color

        self.tiles_horizontal = int(rect.width / self.tile_size)
        self.tiles_vertical = int(rect.height / self.tile_size)

        self.initialize_fonts()
        self.set_terrain_map(terrain_map)
        self.set_entity_map(entity_map)

        self.generate_tiles()

    def initialize_fonts(self):
        battlefield_font_name = 'freesansbold.ttf'
        battlefield_font_size = 11
        self.font = pygame.font.Font(battlefield_font_name, battlefield_font_size)

    def set_terrain_map(self, terrain_map):
        self.terrain_map = terrain_map
        self.terrain_map_size = (len(terrain_map), len(terrain_map[0]))

    def set_entity_map(self, entity_map):
        self.entity_map = entity_map
        self.entity_map_size = (len(entity_map), len(entity_map[0]))

    # TODO place all map values into a tile, so it can render whichever it needs
    def update(self):
        self.update_mouse_position()
        self.update_tiles()

    def render(self):
        self.surface = pygame.Surface(self.rect.size)
        self.surface.fill(self.background_color)

        self.render_tiles()

    def get_selected_tile(self):
        for row in self.tiles:
            for tile in row:
                if tile.is_selected:
                    return tile
        return None

    # TODO This is a mess. Fix to work properly with new mouse position
    # TODO scroll map somehow. Maybe when mouse gets to the edge of the battlefield
    def generate_tiles(self):
        self.tiles = []

        for left in range(self.tiles_horizontal):
            row = []
            for top in range(self.tiles_vertical):
                tile_position = (left * self.tile_size, top * self.tile_size)
                tile = Tile(rect=Rect(tile_position[0], tile_position[1], self.tile_size, self.tile_size),
                            terrain_value=self.terrain_map[top][left],
                            entity_value=self.entity_map[top][left],
                            font=self.font,
                            mouse_position=self.mouse_position)
                row.append(tile)
            self.tiles.append(row)

    def update_tiles(self):
        for row in self.tiles:
            for tile in row:
                tile.mouse_position = self.mouse_position
                tile.update()

    def render_tiles(self):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.render()
                self.surface.blit(tile.surface, tile.rect)

    def update_mouse_position(self):
        self.mouse_position = pygame.mouse.get_pos()

    def clip_to_battlefield(self, position):
        return sorted((0, position[0], self.tiles_horizontal))[1], sorted((0, position[1], self.tiles_vertical))[1]