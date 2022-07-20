from random import randint
import pygame as pg
import Controls
import game_text as gt
import Flake, sys, highscores


class Game:
    
    def __init__(self, w, h):
        pg.init()
        self.mouse = (0,0)
        # Init started, points, fps and clock for updates
        self.playerName = ""
        self.highscores = highscores.Highscores()
        self.started = False
        self.points = 0
        self.spawned = 0
        self.FPS = 60
        self.timer = 00
        self.FramePerSec = pg.time.Clock()
        self.flakes = pg.sprite.Group()
        self.inputActive = False
        # Change icon and title
        pg.display.set_caption("Operaatio Lumihiutale Python")
        icon = pg.image.load(r"S:\koulu\OOP\Kouluharjoituksia\pygame\imgs\A1.png")
        pg.display.set_icon(icon)

        self.screen = pg.display.set_mode((w,h))
        self.controls = Controls.Controls()
        self.gt = gt.GameText(w, h, self)

    def run(self):
        # Create event and set a timer for spawning a flake every X milliseconds
        # Also event for timer
        SPAWN_NEW = pg.USEREVENT
        DECREMENT_TIMER = pg.USEREVENT+1
        pg.time.set_timer(DECREMENT_TIMER, 1000)
        pg.time.set_timer(SPAWN_NEW, 500)
        
        while True:
            self.mouse = pg.mouse.get_pos()
            #self.controls.check_events(self)
            for event in pg.event.get():
                #Start the game when you press Start Game Button, reset timer and points
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.gt.nameInputArea.collidepoint(self.mouse[0], self.mouse[1]):
                            self.inputActive = not self.inputActive
                        elif not self.gt.nameInputArea.collidepoint(self.mouse[0], self.mouse[1]):
                            self.inputActive = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.gt.startGameTextRect.collidepoint(self.mouse[0], self.mouse[1]):
                                self.points = 0
                                self.timer = 30
                                self.playerName = self.gt.nameInputText
                                print(self.playerName)
                                self.started = True
                if self.started == True:
                    # Checks if left mouse button clicked on flakes, gib point
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            for flake in self.flakes.sprites():
                                    if flake.rect.collidepoint(self.mouse[0], self.mouse[1]):
                                        self.points += 1
                                        flake.kill()
                                        self.spawnNewFlake()
                                        print(self.points)
                    # If too many flake, destroy oldest
                    if len(self.flakes.sprites()) > 5:
                        self.flakes.sprites()[0].kill()
                    # It's a timer
                    if event.type == DECREMENT_TIMER:
                        self.timer -= 1
                        # If timer 0 stop game
                        if self.timer == 0:
                            self.started = False
                            for flake in self.flakes:
                                flake.kill()
                            self.highscores.insertHighscore(self.playerName, self.points)
                    if event.type == SPAWN_NEW:
                        self.spawnNewFlake()
                if not self.started:
                    if event.type == pg.KEYDOWN:
                        if self.inputActive:
                            if event.key == pg.K_BACKSPACE:
                                self.gt.nameInputText = self.gt.nameInputText[:-1]
                            else:
                                self.gt.nameInputText += event.unicode
                if event.type == pg.QUIT:
                    sys.exit()
            self.update()
            self.FramePerSec.tick(self.FPS)

    def spawnNewFlake(self):
        self.flake = Flake.Flake(self)
        self.flakes.add(self.flake)
        self.spawned += 1
        print(self.spawned)
        print(f"missed: {self.spawned - self.points}")

    def update(self):
        self.screen.fill((255, 255, 255))
        for flake in self.flakes:
            flake.draw()
        self.gt.update()
        pg.display.update() # updates screen
# w = int(input("Input width: "))
# h = int(input("input height: "))
game = Game(400, 500)
game.run()

#lisää juttu ettei se lähetä tuloksia tyhjällä nimellä