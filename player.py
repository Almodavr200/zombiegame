from bullet import Bullet
from drawable import Drawable
from functions import collide_with_object, vector
from settings import *


class Player(Drawable, pygame.sprite.Sprite):

    def __init__(self, game, x, y, width=20, height=20, color=(0, 0, 255), max_speed=4, angle=180):
        pygame.sprite.Sprite.__init__(self)
        self.max_speed = max_speed
        self.game = game
        self.angle = angle
        self.image = game.player_img
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(x=x, y=y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vector(0, 0)
        self.position = vector(x, y)
        self.picture = None
        self.lives = PLAYER_LIVES
        self.shield = PLAYER_SHIELD
        self.rotation = 0
        self.rotation_speed = 0
        self.last_shot = 0

    def animation(self, image_file, blit_destination, blit_area, serial=True):
        self.picture = pygame.image.load(image_file)
        if serial:
            self.surface.blit(self.picture, blit_destination, blit_area)
            self.picture = pygame.transform.scale(self.picture, (self.width, self.height))
        else:
            self.picture = pygame.transform.scale(self.picture, (self.width, self.height))
            self.surface.blit(self.picture, blit_destination, (0, 0, self.width, self.height))

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

    def get_keys(self):
        self.vel = vector(0, 0)
        self.rotation_speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotation_speed = PLAYER_ROTATION_SPEED
            self.angle = 90
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotation_speed = - PLAYER_ROTATION_SPEED
            self.angle = 270
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel = vector(self.max_speed, 0).rotate(-self.rotation)
            self.angle = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel = vector(-self.max_speed/2, 0).rotate(-self.rotation)
            self.angle = 180
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vector(1, 0).rotate(-self.rotation)
                Bullet(self.game, self.position, dir)

    def refresh(self):
        self.get_keys()
        self.rotation = (self.rotation + self.rotation_speed * self.game.dt) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.position += self.vel * self.game.dt
        self.hit_rect.centerx = self.position.x
        collide_with_object(self, self.game.walls, 'x')
        collide_with_object(self, self.game.monsters, 'x')
        self.hit_rect.centery = self.position.y
        collide_with_object(self, self.game.walls, 'y')
        collide_with_object(self, self.game.monsters, 'y')
        self.rect.center = self.hit_rect.center
        return self.angle
