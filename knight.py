import pygame as pg

from settings import *

from fighter import Fighter


class Knight(Fighter):

    def __init__(self, char_type, max_hp, strength, potions, count):
        
        super().__init__(char_type, max_hp, strength, potions, count)

        self.health_bar_pos_x = HEALTH_BAR_POSITIONS_X["Knight"]
        self.health_bar_pos_y = HEALTH_BAR_POSITIONS_Y[0]