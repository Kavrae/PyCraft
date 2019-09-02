#!/usr/bin/env python
import time
import pygame
from pygame.locals import *


class App:

    def __init__(self):
        self._screen = None

        pygame.init()
        pygame.mixer = None

        display = Rect(0, 0, 640, 480)
        window_style = 0

        best_depth = pygame.display.mode_ok(display.size, window_style, 32)
        self._screen = pygame.display.set_mode(display.size, window_style, best_depth)
        pygame.display.set_caption('PyCraft')

    def color_test(self, color_val):
        self._screen.fill((color_val, 0, 0))

    def display_test(self, color_number):
        text = "Color: {0}".format(color_number)
        print(text)


app = App()
for i in range(256):
    app.color_test(i)
    app.display_test(i)
    pygame.display.flip()
    time.sleep(0.01)
pygame.quit
