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

        # Sets initial position coordinates and velocity and creates player.
        self.player_coords_x = self.width//2
        self.player_coords_y = self.height//2
        self.player_velocity = 5
        # Uses the pngs of sprites I created using Piskel.
        self.char_idle = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_idle.png').convert_alpha(), (64, 64))
        self.char_right = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_right.png').convert_alpha(), (64, 64))
        self.char_left = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_left.png').convert_alpha(), (64, 64))
        self.char_down = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_down.png').convert_alpha(), (64, 64))
        self.char_up = pygame.transform.scale(pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/main_character_up.png').convert_alpha(), (64, 64))
        
        self.game_loop()

    def game_loop(self):
        '''Runs game loop for the game screen and implements all motion.
        Parameters: Void
        Return: Void'''
        running = True
        while running:

            # Dark red background
            self.game_screen.fill((0, 0, 0)) 

            # Sets initial sprite to idle as the player is not moving at the start.
            current_sprite = self.char_idle 

            # Implements movement mechanics
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.player_coords_x -= self.player_velocity
                current_sprite = self.char_left
            if pressed[pygame.K_RIGHT]:
                self.player_coords_x += self.player_velocity
                current_sprite = self.char_right
            if pressed[pygame.K_UP]:
               self.player_coords_y -= self.player_velocity
               current_sprite = self.char_up
            if pressed[pygame.K_DOWN]:
                self.player_coords_y += self.player_velocity
                current_sprite = self.char_down

            # Loads character image
            self.game_screen.blit(current_sprite, (self.player_coords_x, self.player_coords_y))

            # Refreshes page
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False