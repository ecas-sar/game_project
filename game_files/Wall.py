import pygame
import random

class Wall:
    def __init__(self, screen_width, screen_height):
        self.width = 100
        self.height = 100
        self.x, self.y = self.decide_initial_coords(screen_width, screen_height)

    def load_sprites(self):
        wall_sprite = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/wall.png').convert_alpha(), (self.width, self.height))
        return wall_sprite

    def decide_initial_coords(self, screen_width, screen_height):
        self.x = random.uniform(self.width, screen_width - self.width)
        self.y = random.uniform(self.height, screen_height - self.height)
        return self.x, self.y