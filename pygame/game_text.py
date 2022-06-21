import pygame


class GameText:
    def __init__(self, width, points, game):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        game.text = "Start Game"
        self.startGameTextArea = self.font.render(game.text, True, (100, 100, 100), (200, 200, 200))
        self.startGameTextRect = self.startGameTextArea.get_rect()
        self.startGameTextRect.center = (int(width) // 2, 400)
        self.timerTextArea = self.font.render("Timer", True, (100, 100, 100), (200, 200, 200))
        self.timerTextRect = self.timerTextArea.get_rect()
        self.timerTextRect.center = (int(width) // 4, 450)
        self.pointsTextArea = self.font.render("Boints", True, (100, 100, 100), (200, 200, 200))
        self.pointsTextRect = self.timerTextArea.get_rect()
        self.pointsTextRect.center = (int(width) // 1.5, 450)
        self.game = game

    def update(self):
        x, y = self.game.mouse
        if self.startGameTextRect.collidepoint(x, y):
            self.startGameTextArea = self.font.render(self.game.text, True, (100, 100, 100), (200, 200, 200))
        else:
            self.startGameTextArea = self.font.render(self.game.text, True, (100, 100, 100), (10, 10, 10))
        self.timerTextArea = self.font.render(str(f"Timer: {self.game.timer}"), True, (100, 100, 100), (10, 10, 10))
        self.pointsTextArea = self.font.render(str(f"Points: {self.game.points}"), True, (100, 100, 100), (200, 200, 200))
        self.game.screen.blit(self.pointsTextArea, self.pointsTextRect)
        self.game.screen.blit(self.timerTextArea, self.timerTextRect)
        self.game.screen.blit(self.startGameTextArea, self.startGameTextRect)
