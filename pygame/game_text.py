import pygame as pg


class GameText:
    def __init__(self, width, points, game):
        self.font = pg.font.Font('freesansbold.ttf', 20)
        game.text = "Start Game"
        #region startGameText
        self.startGameTextArea = self.font.render(game.text, True, (100, 100, 100), (200, 200, 200))
        self.startGameTextRect = self.startGameTextArea.get_rect()
        self.startGameTextRect.center = (int(width) // 2, 400)
        #endregion

        #region timerText
        self.timerTextArea = self.font.render("Timer", True, (100, 100, 100), (200, 200, 200))
        self.timerTextRect = self.timerTextArea.get_rect()
        self.timerTextRect.center = (int(width) // 6, 430)
        #endregion

        #region pointsText
        self.pointsTextArea = self.font.render("Boints", True, (100, 100, 100), (200, 200, 200))
        self.pointsTextRect = self.timerTextArea.get_rect()
        self.pointsTextRect.center = (int(width) // 6, 460)
        #endregion
        
        #region nameInput
        self.nameInputArea = pg.Rect(100, 100, 140, 32)
        self.done = False
        self.color_active = pg.Color(100, 100, 100)
        self.color_inactive = pg.Color(140, 140, 140)
        self.inputBoxColor = self.color_inactive
        self.nameInputText = ''
        #endregion
        self.game = game

    def update(self):
        x, y = self.game.mouse
        if self.startGameTextRect.collidepoint(x, y):
            self.startGameTextArea = self.font.render(self.game.text, True, (100, 100, 100), (200, 200, 200))
        else:
            self.startGameTextArea = self.font.render(self.game.text, True, (100, 100, 100), (10, 10, 10))
        self.inputBoxColor = self.color_active if self.game.inputActive else self.color_inactive
        self.txtSurface = self.font.render(self.nameInputText, True, (0,0,0))
        self.timerTextArea = self.font.render(str(f"Timer: {self.game.timer}"), True, (100, 100, 100), (200, 200, 200))
        self.pointsTextArea = self.font.render(str(f"Points: {self.game.points}"), True, (100, 100, 100), (200, 200, 200))
        self.game.screen.blit(self.pointsTextArea, self.pointsTextRect)
        self.game.screen.blit(self.timerTextArea, self.timerTextRect)
        self.game.screen.blit(self.startGameTextArea, self.startGameTextRect)
        self.game.screen.blit(self.txtSurface, (self.nameInputArea.x + 5, self.nameInputArea.y + 5))
        pg.draw.rect(self.game.screen, self.inputBoxColor, self.nameInputArea, 2)
