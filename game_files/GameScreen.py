import pygame
import Character
import Enemy
import Losing
import Winning

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

        # To help with attack mechanics and animation.
        self.attacking = False
        self.attack_start_time = 0
        self.attack_end_time = 300 

        # Creating enemy.
        self.enemy = Enemy.Enemy(self.width, self.height)
        self.last_switch_time = pygame.time.get_ticks()
        self.sprite_index = 0
        self.sprites = self.enemy.load_sprites()

        # Creates score.
        self.score = 0

        # Putting sprites in variables to be used later.
        self.char_idle, self.char_right, self.char_left, self.char_down, self.char_up, self.up_attack, self.down_attack, self.left_attack, self.right_attack = self.main_character.load_sprites()

        # Creates sound effects.
        self.bat_hit_char = pygame.mixer.Sound("/Users/cassar.eddie.l/game_project/sound_effects/bat_hit.mp3")
        self.char_hit_bat = pygame.mixer.Sound("/Users/cassar.eddie.l/game_project/sound_effects/char_hit.mp3")
        self.winning_sfx = pygame.mixer.Sound("/Users/cassar.eddie.l/game_project/sound_effects/win.mp3")
        self.dying_sfx = pygame.mixer.Sound("/Users/cassar.eddie.l/game_project/sound_effects/bruh.mp3")

        self.last_direction = self.char_idle
        
        # Runs game loop.
        self.game_loop()

    def game_loop(self):
        '''Runs game loop for the game screen and implements all motion.
        Parameters: Void
        Return: Void'''
        running = True
        while running:
            self.game_screen.fill((0, 0, 0)) 

            # Sets initial sprite to idle as the player is not moving at the start.
            current_sprite = self.char_idle 

            # Implements attacking mechanics, makes sure player can't attack when already attacking.
            if self.attacking:
                current_time = pygame.time.get_ticks()
                if current_time - self.attack_start_time <= self.attack_end_time:
                    if self.last_direction == self.char_down:
                        current_sprite = self.down_attack
                    if self.last_direction == self.char_left:
                        current_sprite = self.left_attack
                    if self.last_direction == self.char_up:
                        current_sprite = self.up_attack
                    if self.last_direction == self.char_right:
                        current_sprite = self.right_attack
                else:
                    self.attacking = False
            else:
                # Implements movement mechanics
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]: 
                    self.main_character.move_left()
                    current_sprite = self.char_left
                    self.last_direction = self.char_left
                    # This if statement (and others similar below it) make sure the character can't exit boundaries.
                    if self.main_character.x < 0:
                        self.main_character.x = 0
                if pressed[pygame.K_RIGHT]:
                    self.main_character.move_right()
                    current_sprite = self.char_right
                    self.last_direction = self.char_right
                    if self.main_character.x > self.width - 64:
                        self.main_character.x = self.width - 64
                if pressed[pygame.K_UP]:
                    self.main_character.move_up()
                    current_sprite = self.char_up
                    self.last_direction = self.char_up
                if self.main_character.y < 0:
                    self.main_character.y = 0
                if pressed[pygame.K_DOWN]:
                    self.main_character.move_down()
                    current_sprite = self.char_down
                    self.last_direction = self.char_down
                    if self.main_character.y > self.height - 110:
                        self.main_character_y = self.height - 110      
            # Loads background image
            self.game_screen.blit(self.background_big, self.background_rect)

            # Loads character image
            self.game_screen.blit(current_sprite, (self.main_character.x, self.main_character.y))

            # Load enemy image
            self.display_enemy()

            # Creates a player rectangle so that the bat chases that rectangle, hence the player, all the time.
            main_character_rect = pygame.Rect(self.main_character.x, self.main_character.y, current_sprite.get_width(), current_sprite.get_height())
            self.enemy.chase_player(main_character_rect)

            # If the enemy touches the player, the characters health will be decreased by 5.
            if (self.enemy.touching_other(main_character_rect)):
                if (not self.attacking):
                    pygame.mixer.Sound.play(self.bat_hit_char)
                    self.main_character.health -= 5
                else: 
                    pygame.mixer.Sound.play(self.char_hit_bat)
                    self.score += 1
                self.enemy.decide_initial_coords(self.width, self.height)
            
            # If the character's health goes to 0 or less, the game will close and the losing screen will open.
            if self.main_character.health <= 0:
                pygame.mixer.Sound.play(self.dying_sfx)
                Losing.Losing()
                running = False


            # If the character gets a score of ten, the game closes and the winning screen will open.
            if self.score >= 10:
                pygame.mixer.Sound.play(self.winning_sfx)
                Winning.Winning()
                running = False

            # Display health of character
            self.display_char_health()

            # Displays current score
            self.display_score()

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
                    # Implements attack logic in for loop for the same reasoning as dash.
                    if event.key == pygame.K_a:
                        self.attacking = True
                        self.attack_start_time = pygame.time.get_ticks()
                if event.type == pygame.QUIT:
                    running = False

    def display_char_health(self):
        '''Displays character's health at the top left corner of the screen.
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

    def display_score(self):
        '''Displays score at the top corner of the screen.
        Parameters: Void
        Return: Void'''

        # Naming variables for code readability.
        score_x = self.width - 140
        score_y = 50
        font_size = 50
        font = pygame.font.Font('freesansbold.ttf', font_size)
        score_text = font.render('Score: ' + str(self.score), True, (0, 0, 0), (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (score_x, score_y)
        self.game_screen.blit(score_text, score_text_rect)

    def display_enemy(self):
        '''Displays the enemy and animates the flapping.
        Parameters: Void
        Return: Void'''


        current_time = pygame.time.get_ticks()
        rate_of_switching = 125
        if current_time - self.last_switch_time >= rate_of_switching:
            self.last_switch_time = current_time
            self.sprite_index = (self.sprite_index + 1) % len(self.sprites)
        current_sprite = self.sprites[self.sprite_index]
        self.game_screen.blit(current_sprite, (self.enemy.x, self.enemy.y))