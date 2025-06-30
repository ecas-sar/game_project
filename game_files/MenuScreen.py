import pygame

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
        pygame.quit()

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
            self.create_buttons()

            # Refreshes page.
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

        # Renders rectangles
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(start_button_x, button_y, button_width, button_height))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(options_button_x, button_y, button_width, button_height))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(quit_button_x, button_y, button_width, button_height))

        # Renders text.
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


menu_screen = MenuScreen()