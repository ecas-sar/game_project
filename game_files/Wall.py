import pygame
import random

class Wall:
    def __init__(self, screen_width, screen_height):
        '''Constructor for Wall, initialises dimensions and location.
        Parameters: Double, Double
        Return: Void'''
        self.width = 100
        self.height = 100
        self.x, self.y = self.decide_initial_coords(screen_width, screen_height)

    def load_sprites(self):
        '''Loads the sprite for the wall.
        Parameters: Void
        Returns: Pygame Image.'''
        wall_sprite = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/wall.png').convert_alpha(), (self.width, self.height))
        return wall_sprite

    def decide_initial_coords(self, screen_width, screen_height):
        '''Uses a uniform distribution to decide the spawn point of the x and y coordinate.
        Parameters: Double, Double
        Returns: Double Tuple'''
        self.x = random.uniform(self.width, screen_width - self.width)
        self.y = random.uniform(self.height, screen_height - self.height)
        return self.x, self.y