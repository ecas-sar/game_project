import pygame
import random

class Enemy():
    def __init__(self, screen_width, screen_height):
        self.alive = False
        self.initial_x = random.uniform(0, screen_width)
        self.inital_y = random.uniform(0, screen_height)

    def load_sprites(self):
        sprite_one = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_one.png').convert_alpha(), (50, 50))
        sprite_two = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_two.png').convert_alpha(), (50, 50))
        return sprite_one, sprite_two