import pygame as pg
import sys

from settings import *

from world import World
from fighter import Fighter

class Game:

    def __init__(self, screen, clock):

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(self.width, self.height)
        self.knight = Fighter('Knight', 30, 10, 3, 0)
        self.bandits = self.create_bandits()

    def run(self):

        self.playing = True
        
        while self.playing:
            
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def events(self):

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):

        self.knight.update()
        
        for bandit in self.bandits:
            bandit.update()

    def draw(self):

        self.world.draw(self.screen)
        self.knight.draw(self.screen)
        
        for bandit in self.bandits:
            bandit.draw(self.screen)

        pg.display.flip()

    def create_bandits(self):

        arr = []
        
        for i in range(3):
            arr.append(Fighter("Bandit", 20, 6, 1, i))

        return arr
            
