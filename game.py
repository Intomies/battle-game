from bandit import Bandit
from knight import Knight
import pygame as pg
import sys

from settings import *

from world import World
from battle_interface import BattleInterface
from knight import Knight
from bandit import Bandit

class Game:

    def __init__(self, screen, clock):

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(self.width, self.height)
        self.battle_interface = BattleInterface()
        self.knight = Knight('Knight', 30, 10, 3, 0)
        self.bandits = self.create_bandits(2)

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
        self.battle_interface.draw(self.screen)
        self.knight.draw(self.screen)
        
        for bandit in self.bandits:
            bandit.draw(self.screen)

        pg.display.flip()

    def create_bandits(self, amount):

        arr = []
        
        for i in range(amount):
            arr.append(Bandit("Bandit", 20, 6, 1, i))

        return arr
            
