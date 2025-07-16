import pygame
import random

class Enemy():
    def __init__(self, screen_width, screen_height):
        '''Prepares enemy for use by initialising alive, voordinate, and velocity variables.
        Parameters: Int, Int
        Return: Void'''
        self.alive = False
        self.x = random.uniform(0, screen_width)
        self.y = random.uniform(0, screen_height)
        self.velocity = 4

    def load_sprites(self):
        '''Loads sprites so that GameScreen can make the bat switch between them to give the illusion of flapping wings.
        Parameters: Void
        Return: Tuple'''
        sprite_one = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_one.png').convert_alpha(), (50, 50))
        sprite_two = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_two.png').convert_alpha(), (50, 50))
        return sprite_one, sprite_two
    
    def chase_player(self, player_rect):
        '''Makes bat chase player.
        Parameters: pygame.Rect
        Return: Void'''
        if player_rect is None:
            return
        
        # Movement logic.
        if self.x < player_rect.x:
            self.x += self.velocity
        elif self.x > player_rect.x:
            self.x -= self.velocity
        if self.y > player_rect.y:
            self.y -= self.velocity
        elif self.y < player_rect.y:
            self.y += self.velocity