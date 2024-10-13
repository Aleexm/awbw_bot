import pygame
import numpy as np
import os
import random
from create_map import *
from dicts import TERRAIN_DICT
from terrain import Terrain

TERRAIN_SIZE = 16
SCALER = 2

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    return screen

screen = init_game()
clock = pygame.time.Clock()
clock.tick(60)
battlefield = create_battlefield_random(12,12)
# battlefield = create_battlefield_from_data(os.path.join('maps', 'spann_island.txt'))
battlefield, terrain_sprites = get_terrain_sprites(battlefield)
# change_countries_to_ge_yc(battlefield)
relocate_sprites(screen, battlefield, terrain_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    terrain_sprites.draw(screen)
    pygame.display.flip()
