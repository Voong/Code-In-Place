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



if __name__ == '__main__':
    pygame.init()