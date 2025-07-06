import pygame

class GameScreen():
    def __init__(self):
        self.game_screen = pygame.display.set_mode()
        pygame.display.set_caption("Game Screen")
        self.game_loop()

    def game_loop(self):
        running = True
        while running:
            self.game_screen.fill((128, 0, 0))  # Dark blue background
            # Draw options UI here

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False