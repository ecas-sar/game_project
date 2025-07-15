import random
import pygame
import Character
import Enemy

class GameScreen():
    def __init__(self):
        '''Makes screen and character and its initial position and velocity.
        Parameters: Void
        Return: Void'''
        self.game_screen = pygame.display.set_mode()
        pygame.display.set_caption("Game Screen")

        # Defines variables for readability.
        self.width = self.game_screen.get_width()
        self.height = self.game_screen.get_height()

        # Sets initial position coordinates and velocity and creates player.
        self.player_coords_x = self.width//2
        self.player_coords_y = self.height//2
        self.player_velocity = 5


        self.background = pygame.image.load('/Users/cassar.eddie.l/game_project/sprite_sheets/background.png')
        self.background_big = pygame.transform.scale(self.background, (self.width, self.height))
        self.background_rect = self.background_big.get_rect()

        # Creating the main character.
        self.main_character = Character.Character(self.player_coords_x, self.player_coords_y, self.player_velocity)

        self.enemy = Enemy.Enemy(self.width, self.height)

        # Putting sprites in variabled to be used later.
        self.char_idle, self.char_right, self.char_left, self.char_down, self.char_up = self.main_character.load_sprites()
        
        # Runs game loop.
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


            # Loads background image
            self.game_screen.blit(self.background_big, self.background_rect)

            # Loads character image
            self.game_screen.blit(current_sprite, (self.main_character.x, self.main_character.y))

            # Load enemy image
            self.display_enemy()

            # Display health of character
            self.display_char_health()

            # Refreshes page
            pygame.display.flip()

            for event in pygame.event.get():
                # Implements dash logic in for loop so user can't just hold D and zoom around quickly, avoiding all enemies and removing all challenge.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if current_sprite == self.char_down:
                            self.main_character.dash_down()
                        if current_sprite == self.char_left:
                            self.main_character.dash_left()
                        if current_sprite == self.char_up:
                            self.main_character.dash_up()
                        if current_sprite == self.char_right:
                            self.main_character.dash_right()
                if event.type == pygame.QUIT:
                    running = False

    def display_char_health(self):
        '''Displays character's health at the top right corner of the screen.
        Parameters: Void
        Return: Void'''

        # Naming variables for code readability.
        health_x = 140
        health_y = 50
        font_size = 50
        font = pygame.font.Font('freesansbold.ttf', font_size)
        health_text = font.render('Health: ' + str(self.main_character.health), True, (0, 0, 0), (255, 255, 255))
        health_text_rect = health_text.get_rect()
        health_text_rect.center = (health_x, health_y)
        self.game_screen.blit(health_text, health_text_rect)

    def display_enemy(self):
        self.game_screen.blit(self.enemy.load_sprites(), (self.enemy.initial_x, self.enemy.inital_y))