import pygame

class GameScreen():
    def __init__(self):
        '''Makes screen and character and its initial position and velocity.
        Parameters: Void
        Return: Void'''
        self.game_screen = pygame.display.set_mode()
        pygame.display.set_caption("Game Screen")

        # Defines variables for readability
        self.width = self.game_screen.get_width()
        self.height = self.game_screen.get_height()

        # Sets initial position coordinates and velocity and creates rectangle.
        self.player_coords_x = self.width//2
        self.player_coords_y = self.height//2
        self.player_velocity = 10
        self.test_character = pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character.png').convert_alpha()
        self.game_loop()

    def game_loop(self):
        '''Runs game loop for the game screen and implements all motion.
        Parameters: Void
        Return: Void'''
        running = True
        while running:

            # Dark red background
            self.game_screen.fill((128, 0, 0))  

            # Draws rectangle
            self.game_screen.blit(self.test_character, (self.player_coords_x, self.player_coords_y))

            # Implements movement mechanics
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.player_coords_x -= self.player_velocity
            elif pressed[pygame.K_RIGHT]:
                self.player_coords_x += self.player_velocity
            elif pressed[pygame.K_UP]:
               self.player_coords_y -= self.player_velocity
            elif pressed[pygame.K_DOWN]:
                self.player_coords_y += self.player_velocity

            # Refreshes page
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False