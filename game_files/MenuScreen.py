import pygame, sys

import GameScreen, OptionsScreen

class MenuScreen():
    def __init__(self):
        '''Constructor of MenuScreen sets up the backdrop colour, screen size, caption, and runs game loop.
        Paramaters: void
        Returns: void'''

        # Initialises PyGame.
        pygame.init()

        # Sets screen, screen dimension variables, and caption.
        self.screen = pygame.display.set_mode()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Dungeon Slayer")

        # Runs game loop and quits
        self.game_loop()
        self.exit_game()

    def game_loop(self):
        '''Runs the game loop, creating text and implementing button mechanics.
        Parameters: void
        Returns: void'''
        running = True
        while running:
            # Sets backround to black in order to avoid bugs.
            self.screen.fill((0, 0, 0))

            # Displays text and buttons.
            self.create_text()
            mouse_over_start, mouse_over_options, mouse_over_quit = self.create_buttons()

            # Refreshes page.
            pygame.display.flip()
            for event in pygame.event.get():
                if (mouse_over_quit and event.type == pygame.MOUSEBUTTONDOWN):
                    running = False
                
                if (mouse_over_options and event.type == pygame.MOUSEBUTTONDOWN):
                    OptionsScreen.OptionsScreen()
                    running = False

                if (mouse_over_start and event.type == pygame.MOUSEBUTTONDOWN):
                    GameScreen.GameScreen()
                    running = False

    def create_text(self):
        '''Creates title text and displays
        Parameters: void
        Returns: void'''

        # Sets font size and font for code reusability.
        font_size = 125
        font = pygame.font.Font('freesansbold.ttf', font_size)

        # Renders text, centres, and displays.
        text = font.render('Dungeon Slayer', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width//2, font_size)
        self.screen.blit(text, text_rect)
    
    def create_buttons(self):
        '''Creates buttons by creating rectangles, centering text over them, and displays them.
        Parameters: void
        Returns: void'''

        # Names variables for code reusability and readability.
        button_width = 100
        button_height = 50
        start_button_x = 100 - button_width // 2
        options_button_x = self.width // 2 - button_width // 2
        quit_button_x = self.width - 100 - button_width/2
        button_y = self.height - 150

        # Renders text and buttons.
        font_size = 50
        font = pygame.font.Font('freesansbold.ttf', font_size)
        start_text = font.render('Start', True, (0, 0, 0), (255, 255, 255))
        options_text = font.render('Options', True, (0, 0, 0), (255, 255, 255))
        quit_text = font.render('Quit', True, (0, 0, 0), (255, 255, 255))
        start_text_rect = start_text.get_rect()
        options_text_rect = options_text.get_rect()
        quit_text_rect = quit_text.get_rect()
        start_text_rect.center = (start_button_x + button_width // 2, button_y + button_height // 2)
        options_text_rect.center = (options_button_x + button_width // 2, button_y + button_height // 2)
        quit_text_rect.center = (quit_button_x + button_width // 2, button_y+ button_height // 2)
        self.screen.blit(start_text, start_text_rect)
        self.screen.blit(options_text, options_text_rect)
        self.screen.blit(quit_text, quit_text_rect)
        return self.mouse_over_button(start_text, start_text_rect), self.mouse_over_button(options_text, options_text_rect), self.mouse_over_button(quit_text, quit_text_rect)

    def mouse_over_button(self, button, button_rect):
        '''Uses Pythagorean Theorem to detect if the mouse is iver the button.
        Parameters: button, button_rect
        Return: boolean'''
        x_mouse, y_mouse = pygame.mouse.get_pos()
        button_mid_length = abs(((button.get_width())**2 + (button.get_height())**2)**(1/2))
        mouse_distance_length_x = button_rect.left - x_mouse
        mouse_distance_length_y = button_rect.top - y_mouse
        mouse_distance_length = abs(((mouse_distance_length_x)**2 + (mouse_distance_length_y)**2)**(1/2))
        # If the distance between the left hand and the mouse is less than or equal to the distance 
        # between the top left and bottom right corners of the button, the mouse is over the button.
        # A proof for this can be seen in the notes.
        return mouse_distance_length <= button_mid_length
    
    def exit_game(self):
        '''Exits game and exits system to prevent run-time errors when closing program
        Parameters: void
        Return: void'''
        pygame.quit()
        sys.exit()

menu_screen = MenuScreen()