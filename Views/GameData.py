import pygame
from pygame.locals import *


# TODO figure out how to get this to pull data from every other view and other places
class GameData:
    clock = None

    font = None
    rect = None
    surface = None
    background_color = None

    fps = None
    utilization = None

    def __init__(self, rect: Rect, clock, background_color: tuple = (0, 0, 0)):
        self.clock = clock

        self.rect = rect
        self.background_color = background_color
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(background_color)

        self.fps = 0
        self.utilization = 0

        self.initialize_fonts()

    def initialize_fonts(self):
        stats_font_name = 'freesansbold.ttf'
        stats_font_size = 11
        self.font = pygame.font.Font(stats_font_name, stats_font_size)

    def update(self):
        self.update_fps()
        self.update_utilization()

    def render(self):
        self.display_data_rows([self.display_fps(),
                                self.display_utilization()])

    # TODO left align instead of centered
    def display_data_rows(self, data_surfaces):
        row_num = 0
        background_color = self.background_color
        height = 16
        width = self.rect.width

        for data_surface in data_surfaces:
            row_surface = pygame.Surface((width, height))
            row_surface.fill(background_color)
            row_rect = row_surface.get_rect()

            data_rect = data_surface.get_rect()
            data_rect.center = (row_rect.width / 2, row_rect.height / 2)
            row_surface.blit(data_surface, data_rect)

            self.surface.blit(row_surface, Rect(0, row_num * height, width, height))
            row_num += 1

    def update_fps(self):
        self.fps = int(self.clock.get_fps())

    def update_utilization(self):
        total_time = self.clock.get_time()
        used_time = self.clock.get_rawtime()
        if total_time > 0:
            utilization = int(100 * used_time / total_time)
        else:
            utilization = 0
        if abs(self.utilization - utilization) > 0:
            self.utilization = utilization

    # TODO blit multiple text boxes into a single surface to do multiple colors?
    #  good test would be to make the number red if it's below an acceptable value
    def display_fps(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "FPS = {0:03d}".format(self.fps)
        return self.font.render(text, antialias, text_color, self.background_color)

    def display_utilization(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "Frame Utilization = {0:02d}%".format(self.utilization)
        return self.font.render(text, antialias, text_color, self.background_color)

