import pygame
import random

class Enemy():
    def __init__(self, screen_width, screen_height):
        '''Prepares enemy for use by initialising alive, voordinate, and velocity variables.
        Parameters: Int, Int
        Return: Void'''
        self.alive = False
        self.x, self.y = self.decide_initial_coords(screen_width, screen_height)
        self.width = 0
        self.height = 0 # Both of these to be overriden in load_sprites.
        self.velocity = 4

    def decide_initial_coords(self, screen_width, screen_height):
        self.x = random.uniform(0, screen_width)
        self.y = random.uniform(0, screen_height)
        return self.x, self.y


    def load_sprites(self):
        '''Loads sprites so that GameScreen can make the bat switch between them to give the illusion of flapping wings.
        Parameters: Void
        Return: Tuple'''
        sprite_one = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_one.png').convert_alpha(), (50, 50))
        sprite_two = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/bat_two.png').convert_alpha(), (50, 50))

        self.width = sprite_one.get_width()
        self.height = sprite_one.get_height()
        return sprite_one, sprite_two
    
    def chase_player(self, player_rect):
        '''Makes bat chase player.
        Parameters: pygame.Rect
        Return: Void'''
        if player_rect is None:
            return
        
        # Movement logic. Two if statements to enable diagonal chasing.
        if self.x < player_rect.x:
            self.x += self.velocity
        elif self.x > player_rect.x:
            self.x -= self.velocity
        if self.y > player_rect.y:
            self.y -= self.velocity
        elif self.y < player_rect.y:
            self.y += self.velocity

    def touching_other(self, other_rect):
        '''Detects if the bat is touching something else.
        Parameters: Pygame.rect
        Return: Boolean'''

        # Create the bat's own rectangle.
        bat_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bat_rect.colliderect(other_rect)