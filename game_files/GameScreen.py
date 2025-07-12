import pygame
import Character

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

        self.main_character = Character.Character(self.player_coords_x, self.player_coords_y, self.player_velocity)

        self.char_idle, self.char_right, self.char_left, self.char_down, self.char_up = self.main_character.load_sprites()
        
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
                self.main_character.move_left()
                current_sprite = self.char_left
            if pressed[pygame.K_RIGHT]:
                self.main_character.move_right()
                current_sprite = self.char_right
            if pressed[pygame.K_UP]:
               self.main_character.move_up()
               current_sprite = self.char_up
            if pressed[pygame.K_DOWN]:
                self.main_character.move_down()
                current_sprite = self.char_down

            # Loads character image
            self.game_screen.blit(current_sprite, (self.main_character.x, self.main_character.y))

            # Refreshes page
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False