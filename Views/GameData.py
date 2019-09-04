import pygame
from pygame.locals import *
import time


# TODO figure out how to get this to pull data from every other view and other places
class GameData:
    font = None
    rect = None
    surface = None
    background_color = None

    time = None
    ticks = 0
    fps = None

    def __init__(self, rect: Rect = (0, 0, 0, 0), background_color: tuple = (0, 0, 0)):
        self.rect = rect
        self.background_color = background_color
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(background_color)

        # fps tracking until it's properly implemented using the clock in the GameScreen and passed in somehow
        self.time = 0
        self.ticks = 0
        self.fps = 0

        self.initialize_fonts()

    def initialize_fonts(self):
        stats_font_name = 'freesansbold.ttf'
        stats_font_size = 11
        self.font = pygame.font.Font(stats_font_name, stats_font_size)

    def update(self):
        self.calculate_fps()

    def render(self):
        self.display_data_rows([self.display_fps()])

    # Only calculate FPS once every second
    def calculate_fps(self):
        self.ticks += 1

        current_time = time.time()
        if current_time - self.time > 1:  # 1 second
            self.time = current_time
            self.fps = self.ticks
            self.ticks = 0

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

    # TODO blit multiple text boxes into a single surface to do multiple colors?
    #  good test would be to make the number red if it's below an acceptable value
    def display_fps(self):
        antialias = True
        text_color = (0, 0, 0)
        text = "FPS = {0:03d}".format(int(self.fps))
        return self.font.render(text, antialias, text_color, self.background_color)
