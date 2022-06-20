import pygame as pg
import Controls
import game_text as gt
import Flake, sys


class Game:
    
    def __init__(self, w, h):
        pg.init()
        self.mouse = pg.mouse.get_pos()
        # Init started, points, fps and clock for updates
        self.started = False
        self.points = 0
        self.FPS = 60
        self.FramePerSec = pg.time.Clock()
        # Create event and set a timer for spawning a flake every X milliseconds
        self.SPAWN_NEW = pg.USEREVENT + 1
        pg.time.set_timer(self.SPAWN_NEW, 500)
        self.flakes = pg.sprite.Group()
        # Change icon and title
        pg.display.set_caption("Operaatio Lumihiutale Python")
        icon = pg.image.load(r"S:\koulu\OOP\Kouluharjoituksia\pygame\imgs\A1.png")
        pg.display.set_icon(icon)

        self.screen = pg.display.set_mode((w,h))
        self.controls = Controls.Controls()
        self.gt = gt.GameText(w, h, self)

    def run(self):
        while True:
            #self.controls.check_events(self)
            for event in pg.event.get():
                #if event.type == pg.MOUSEBUTTONDOWN:
                #self.started = True
                while self.started == True:
                    if event.type == self.SPAWN_NEW:
                        self.spawnNewFlake()
                if event.type == pg.QUIT:
                    sys.exit()
            self.update()
            self.FramePerSec.tick(self.FPS)

    def spawnNewFlake(self):
        self.flake = Flake.Flake(self)
        self.flakes.add(self.flake)

    def update(self):
        self.screen.fill((255, 255, 255))
        for flake in self.flakes:
            flake.draw()
        self.gt.update(self.mouse)
        pg.display.update() # updates screen
# w = int(input("Input width: "))
# h = int(input("input height: "))
game = Game(400, 500)
game.run()