import pygame


class GameText:
    def __init__(self, width, points, game):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        game.text = "Start Game"
        self.textArea = self.font.render(game.text, True, (100, 100, 100), (200, 200, 200))
        self.textRect = self.textArea.get_rect()
        self.textRect.center = (int(width) // 2, 400)
        self.game = game

    def update(self, mouse):
        if self.textArea.get_width() >= mouse[0] >= self.textArea.get_width() and self.textArea.get_height() >= mouse[1] >= self.textArea.get_height():
            self.textArea = self.font.render(self.game.text, True, (100, 100, 100), (200, 200, 200))
        self.textArea = self.font.render(self.game.text, True, (100, 100, 100), (10, 10, 10))
        self.game.screen.blit(self.textArea, self.textRect)
