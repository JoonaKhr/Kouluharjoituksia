import pygame as pg
import sys

class Controls:
    def check_events(self, game):

        for event in pg.event.get():

            

            if event.type == pg.QUIT:

                sys.exit()

            elif event.type == pg.KEYDOWN:

                self.check_key_down_events(event, game)



    def check_key_down_events(self, event, game):

        if event.key == pg.K_BACKSPACE:
            game.gt.nameInputText = game.gt.nameInputText[:-1]
        elif event.key != pg.K_ESCAPE:
            game.gt.nameInputText += event.unicode
        elif event.key == pg.K_ESCAPE:

            sys.exit()