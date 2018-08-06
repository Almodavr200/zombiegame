from random import randint
import pygame
from player import Player


class Zombie(Player, pygame.sprite.Sprite):

    def __init__(self, x, y, victim, width, height, color=(255, 0, 0), max_speed=1):
        super(Player, self).__init__(width, height, x, y, color)
        pygame.sprite.Sprite.__init__(self)
        self.max_speed = max_speed
        self.image = self.surface
        self.rect = self.image.get_rect(x=x, y=y)
        self.victim = victim
        self.picture = None

    def zombie_natural_moves(self):
        moves_list = [0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0]
        a = randint(0, len(moves_list) - 1)
        self.move_x(moves_list[a], 1000)
        a = randint(0, len(moves_list) - 1)
        self.move_y(moves_list[a], 600)

    def zombie_follows(self):
        if self.rect.x > self.victim.rect.x:
            x = self.max_speed
        else:
            x = -self.max_speed
        self.move_x(x, 1000)
        if self.rect.y > self.victim.rect.y:
            y = self.max_speed
        else:
            y = -self.max_speed
        self.move_y(y, 600)

    def zombie_attacks(self):
        pass
