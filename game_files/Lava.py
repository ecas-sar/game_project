import pygame
import random

class Lava:
    def __init__(self, screen_width, screen_height):
        '''Constructor for Lava, initialises dimensions and location.
        Parameters: Double, Double
        Return: Void'''
        self.width = 75
        self.height = 75
        self.x, self.y = self.decide_initial_coords(screen_width, screen_height)
    
    def decide_initial_coords(self, screen_width, screen_height):
        '''Uses a uniform distribution to decide the spawn point of the x and y coordinate.
        Parameters: Double, Double
        Returns: Double Tuple'''
        self.x = random.uniform(self.width, screen_width-self.width)
        self.y = random.uniform(self.height, screen_height-self.height)
        return self.x, self.y

    def load_sprites(self):
        '''Loads the sprite for the lava.
        Parameters: Void
        Returns: Pygame Image.'''
        wall_sprite = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/lava.png').convert_alpha(), (self.width, self.height))
        return wall_sprite