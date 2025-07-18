import pygame

class Losing():
    def __init__(self):
        pygame.init()
        self.losing_screen = pygame.display.set_mode()
        self.width = self.losing_screen.get_width()
        self.height = self.losing_screen.get_height()
        pygame.display.set_caption("You Lose!")
        self.game_loop()

    def game_loop(self):
        running = True
        while running:
            self.losing_screen.fill((0, 0, 0))
            self.create_text()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def create_text(self):
        font_size = 125
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render('You Lose!', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.width//2, font_size)
        self.losing_screen.blit(text, text_rect)