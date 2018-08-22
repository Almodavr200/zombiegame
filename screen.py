import pygame
from settings import *


class Camera:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.Rect(0, 0, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.screen.topleft)

    def update(self, target):
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        y = -target.rect.y + int(SCREEN_HEIGHT / 2)
        self.screen = pygame.Rect(x, y, self.width, self.height)


class Map:

    def __init__(self, filename):
        self.map_data = []
        with open(filename, 'rt') as lines:
            for line in lines:
                self.map_data.append(line)

        self.tiles_quantity_row = len(self.map_data[0])
        self.tiles_quantity_col = len(self.map_data)
        self.width = self.tiles_quantity_row * WALL_SIZE
        self.height = self.tiles_quantity_col * WALL_SIZE

    def get_map(self):
        return self.map_data