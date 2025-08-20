import pygame

class Wall:
    def __init__(self, initial_x, initial_y, screen):
        self.x = initial_x
        self.y = initial_y
        self.colour = (0, 0, 0)
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, 30, 30))