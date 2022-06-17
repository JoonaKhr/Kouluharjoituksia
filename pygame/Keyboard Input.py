import pygame as pg
import Controls

class Game:
    def __init__(self, w, h):
        pg.init()
        pg.display.set_caption("Keyboard Test")
        self.screen = pg.display.set_mode((w,h))
        self.controls = Controls.Controls()

    def run(self):
        while True:
            self.controls.check_events(self)
            self.update()

    def update(self):
        pg.display.update() # updates screen
# w = int(input("Input width: "))
# h = int(input("input height: "))
game = Game(800, 600)
game.run()