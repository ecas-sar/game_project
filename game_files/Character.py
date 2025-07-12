import pygame


class Character():
    def __init__(self, initial_x, initial_y, velocity):
        '''Sets initial position, velocity, and health.
        Parameters: Int, Int, Int
        Return: Void'''
        self.x = initial_x
        self.y = initial_y
        self.velocity = velocity
        self.health = 100

    def move_left(self):
        '''Moves to the left.
        Parameters: Void
        Return: Void'''
        self.x -= self.velocity

    def move_right(self):
        '''Moves to the right.
        Parameters: Void
        Return: Void'''
        self.x += self.velocity

    def move_down(self):
        '''Moves to the down.
        Parameters: Void
        Return: Void'''
        self.y += self.velocity

    def move_up(self):
        '''Moves to the up.
        Parameters: Void
        Return: Void'''
        self.y -= self.velocity

    def load_sprites(self):
        '''Loads all the sprites and scales them properly.
        Parameters: Void
        Return: Void
        '''
        # Uses the pngs of sprites I created using Piskel.
        char_idle = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_idle.png').convert_alpha(), (64, 64))
        char_right = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_right.png').convert_alpha(), (64, 64))
        char_left = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_left.png').convert_alpha(), (64, 64))
        char_down = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_down.png').convert_alpha(), (64, 64))
        char_up = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_up.png').convert_alpha(), (64, 64))
        return char_idle, char_right, char_left, char_down, char_up