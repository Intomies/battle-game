import pygame as pg

from settings import *

class Healthbar():
    
    def __init__(self, x, y, hp, max_hp):
        
        self.x_pos = x
        self.y_pos = y
        self.height = HEALTH_BAR_HEIGHT
        self.width = HEALTH_BAR_WIDTH
        self.health_color = GREEN
        self.dmg_color = RED
        self.hp = hp
        self.max_hp = max_hp
        self.ratio = self.get_ratio()
        self.damage_amount = self.get_damage()


    
    def update(self):
        
        pass

    
    def draw(self, hp, screen):

        self.hp = hp
        pg.draw.rect(screen, self.dmg_color, (self.x_pos, self.y_pos, self.width, self.height))
        pg.draw.rect(screen, self.health_color, (self.x_pos, self.y_pos, self.damage_amount, self.height))

    def get_ratio(self):

        return self.hp / self.max_hp
    

    def get_damage(self):

        return self.width * self.ratio
    