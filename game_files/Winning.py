import pygame
import GameScreen

class Winning():
    def __init__(self):
        '''Creates losing screen.
        Parameters: Void
        Return: Void'''

        pygame.init()
        self.winning_screen = pygame.display.set_mode()
        self.width = self.winning_screen.get_width()
        self.height = self.winning_screen.get_height()
        pygame.display.set_caption("You Win!")
        self.game_loop()

    def game_loop(self):
        '''Runs game loop.
        Parameters: Void
        Return: Void'''
        running = True
        while running:
            self.winning_screen.fill((0, 0, 0))

            # Creates text and buttons, logic is the same as for the menu screen.
            self.create_text()
            mouse_over_restart, mouse_over_quit = self.create_buttons()

            # Refreshes page.
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_over_restart:
                        GameScreen.GameScreen()
                        running = False
                    elif mouse_over_quit:
                        running = False

    def create_text(self):
        '''Creates the text.
        Parameters: Void
        Return: Void'''
        font_size = 125
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render('You Win!', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width//2, font_size)
        self.winning_screen.blit(text, text_rect)

    def create_buttons(self):
        '''Creates buttons for restarting and quitting.
        Parameters: Void
        Return: (Boolean, Boolean)'''

        # Names variables for code reusability and readability.
        button_width = 100
        button_height = 50
        restart_button_x = 100 - button_width // 2
        quit_button_x = self.width - 100 - button_width/2
        button_y = self.height - 150

        # Creates, renders, and displays the buttons.
        font_size = 50
        font = pygame.font.Font('freesansbold.ttf', font_size)
        restart_text = font.render('Restart', True, (0, 0, 0), (255, 255, 255))
        quit_text = font.render('Quit', True, (0, 0, 0), (255, 255, 255))
        restart_text_rect = restart_text.get_rect()
        quit_text_rect = quit_text.get_rect()
        restart_text_rect.center = (restart_button_x + button_width // 2, button_y + button_height // 2)
        quit_text_rect.center = (quit_button_x + button_width // 2, button_y + button_height // 2)
        self.winning_screen.blit(restart_text, restart_text_rect)
        self.winning_screen.blit(quit_text, quit_text_rect)
        return self.mouse_over_button(restart_text_rect), self.mouse_over_button(quit_text_rect)

    def mouse_over_button(self, button_rect):
        '''Detects if mouse is over the button.
        Parameters: button_rect
        Return: boolean'''

        # Names variables for code readability.
        x_mouse, y_mouse = pygame.mouse.get_pos()
        button_left = int(button_rect.left)
        button_right = int(button_rect.right)
        button_top = int(button_rect.top)
        button_bottom = int(button_rect.bottom)
        ''' If the x coordinate of the mouse is between the left and right edges of the button and if the y is between
         the top and bottom, the mouse is over the button.'''
        return (button_left <= x_mouse <= button_right) and (button_top <= y_mouse <= button_bottom)