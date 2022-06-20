import pygame as pg
import random
import os

class Flake(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        pg.init()
        self.image = pg.image.load(r"imgs\A1.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(32, 400-32), random.randint(32, 350-32))
        self.game = game
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def load_images(path_to_dir):
        image_dict = {}
        for filename in os.listdir(path_to_dir):
            path = os.path.join(path_to_dir, filename)
            key = filename[:]
            image_dict[key] = pg.image.load(path).convert()