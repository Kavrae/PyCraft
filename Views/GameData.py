import pygame
from pygame.locals import *


class GameData:
    clock = None
    ticks = None

    font = None
    rect = None
    surface = None
    background_color = None

    fps = None
    utilization = None

    def __init__(self, rect: Rect, clock, background_color: tuple = (0, 0, 0)):
        self.clock = clock
        self.ticks = 0

        self.rect = rect
        self.background_color = background_color
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(background_color)

        self.fps = 0
        self.utilization = 0

        self.initialize_fonts()

    def initialize_fonts(self):
        font_name = 'helvetica'
        stats_font_size = 14
        self.font = pygame.font.SysFont(font_name, stats_font_size)

    def update(self):
        self.ticks += 1
        self.update_fps()
        self.update_utilization(60)

    def render(self):
        self.display_data_rows([self.display_fps(),
                                self.display_utilization()])

    def display_data_rows(self, data_surfaces):
        row_num = 0
        background_color = self.background_color
        top_margin = 5
        height = 16
        width = self.rect.width

        for data_surface in data_surfaces:
            row_surface = pygame.Surface((width, height))
            row_surface.fill(background_color)

            data_rect = data_surface.get_rect()
            row_surface.blit(data_surface, data_rect)

            self.surface.blit(row_surface, Rect(0, row_num * height + top_margin, width, height))
            row_num += 1

    def update_fps(self, update_rate=0):
        if update_rate == 0 or self.ticks % update_rate == 0:
            self.fps = int(self.clock.get_fps())

    def update_utilization(self, update_rate=0):
        if update_rate == 0 or self.ticks % update_rate == 0:
            total_time = self.clock.get_time()
            used_time = self.clock.get_rawtime()
            if total_time > 0:
                utilization = int(100 * used_time / total_time)
            else:
                utilization = 0
            if abs(self.utilization - utilization) > 0:
                self.utilization = utilization

    def display_fps(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "FPS = {0:02d}".format(self.fps)
        return self.font.render(text, antialias, text_color, self.background_color)

    def display_utilization(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "Frame Utilization = {0:02d}%".format(self.utilization)
        return self.font.render(text, antialias, text_color, self.background_color)

