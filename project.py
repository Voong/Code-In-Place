import pygame
import random
import time
import sys
import os

from pygame.locals import *
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Define commonly used colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#Establish the size of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
res = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(res)

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.image.load(r'H:\CodeInPlace\FinalProject\karel.png').convert()
        self.surf.set_colorkey(white, RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)
            #move_up_sound.play()

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
            #move_down_sound.play()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


if __name__ == '__main__':
    pygame.init()