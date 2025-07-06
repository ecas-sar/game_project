import pygame

class OptionsScreen():
    def __init__(self):
        self.options_screen = pygame.display.set_mode()
        pygame.display.set_caption("Options Screen")
        self.game_loop()

    def game_loop(self):
        running = True
        while running:
            self.options_screen.fill((0, 0, 128))  # Dark blue background
            # Draw options UI here

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False