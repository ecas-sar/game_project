import pygame
import random

class Projectile:
    def __init__(self, screen_width, screen_height):
        '''Constructor method initialising dimensions and initial coords.
        Parameters: Double, Double
        Return: Void'''
        self.width = 25
        self.height = 25
        self.velocity = 4
        self.horizontal = None
        self.x, self.y = self.decide_initial_coords(screen_width, screen_height)

    def load_sprites(self):
        '''Loads projectile sprite.
        Parameters: Void
        Return: Pygame Image'''
        projectile_sprite = char_idle = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/projectile.png').convert_alpha(), (self.width, self.height))
        return projectile_sprite

    def decide_initial_coords(self, screen_width, screen_height):
        '''Decides initial coordinates such that there will be a 50-50 chance of the projectile moving across the screen vertically or horizontally.
        Parameters: Double, Double
        Return: Double, Double'''
        vertical = random.choice([0, 1])
        if vertical == 0:
            self.x = 0
            self.y = random.uniform(self.height, screen_height - self.height)
            self.horizontal = True
        else:
            self.y = 0
            self.x = random.uniform(self.width, screen_width - self.width)
            self.horizontal = False
        return self.x, self.y

    def move_down(self):
        '''Moves projectile down.
        Parameters: Void
        Return: Void'''
        self.y += self.velocity

    def move_right(self):
        '''Moves projectile to the right.
        Parameters: Void
        Return: Void'''
        self.x += self.velocity