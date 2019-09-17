import pygame
from pygame.locals import *
from Views.ViewObjects import Tile


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
    max_scroll_cooldown = None
    current_scroll_cooldown = None

    rewrite_all_tiles = None
    map_offset_horizontal = None
    map_offset_vertical = None

    def __init__(self, rect: pygame.Rect, tile_size: int, terrain_map, entity_map, background_color: tuple):
        self.rect = rect
        self.tile_size = tile_size  # Square tiles
        self.background_color = background_color  # This is applied to all screens and tiles to speed up blits

        self.tiles_horizontal = int(rect.width / self.tile_size)  # int conversion forces round down
        self.tiles_vertical = int(rect.height / self.tile_size)

        self.map_offset_horizontal = 0  # Determines which map coordinates to print to the battlefield
        self.map_offset_vertical = 0

        self.rewrite_all_tiles = False  # Force expensive rebuild of all tiles

        self.max_scroll_cooldown = 0  # Use this to slow down scrolling if needed
        self.current_scroll_cooldown = 0

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

    def update(self):
        self.update_mouse_position()
        self.update_map_scroll()
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

    def generate_tiles(self):
        self.tiles = []

        for left in range(self.tiles_horizontal):
            row = []
            for top in range(self.tiles_vertical):
                tile_position = (left * self.tile_size, top * self.tile_size)
                tile_x = self.map_offset_horizontal + left
                tile_y = self.map_offset_vertical + top

                tile = Tile(rect=Rect(tile_position[0], tile_position[1], self.tile_size, self.tile_size),
                            terrain=self.terrain_map[tile_x][tile_y],
                            entity=self.entity_map[tile_x][tile_y],
                            font=self.font,
                            mouse_position=self.mouse_position)
                row.append(tile)
            self.tiles.append(row)

    def update_tiles(self):
        if self.rewrite_all_tiles:
            self.generate_tiles()
            self.rewrite_all_tiles = False
        else:
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

    # TODO change all of this if we start in the center of the map OR centered on a chosen player
    def update_map_scroll(self):
        if self.current_scroll_cooldown > 0:
            self.current_scroll_cooldown -= 1
        else:
            # Scroll left (leftmost tile but not off the map)
            if self.rect.left <= self.mouse_position[0] <= self.tile_size:
                # Don't decrement if it would shift off the left of the map
                if self.map_offset_horizontal > 0:
                    self.map_offset_horizontal -= 1
                    self.rewrite_all_tiles = True
                    self.current_scroll_cooldown = self.max_scroll_cooldown

            # Scroll Right (rightmost tile, but not off the map)
            elif (self.tiles_horizontal - 1) * self.tile_size <= self.mouse_position[0] <= self.rect.right:
                # Don't increment if it would shift off the right of the map
                if self.map_offset_horizontal < self.terrain_map_size[0] - self.tiles_horizontal:
                    self.map_offset_horizontal += 1
                    self.rewrite_all_tiles = True
                    self.current_scroll_cooldown = self.max_scroll_cooldown

            # Scroll Up (topmost tile but not off the map)
            if self.rect.top <= self.mouse_position[1] <= self.tile_size:
                # Don't decrement if it would shift off the top of the map
                if self.map_offset_vertical > 0:
                    self.map_offset_vertical -= 1
                    self.rewrite_all_tiles = True
                    self.current_scroll_cooldown = self.max_scroll_cooldown

            # Scroll Down (bottommost tile, but not off the map)
            elif (self.tiles_vertical - 1) * self.tile_size <= self.mouse_position[1] <= self.rect.bottom:
                # Don't increment if it would shift off the bottom of the map
                if self.map_offset_vertical < self.terrain_map_size[1] - self.tiles_vertical:
                    self.map_offset_vertical += 1
                    self.rewrite_all_tiles = True
                    self.current_scroll_cooldown = self.max_scroll_cooldown

    def clip_to_battlefield(self, position):
        return sorted((0, position[0], self.tiles_horizontal))[1], sorted((0, position[1], self.tiles_vertical))[1]