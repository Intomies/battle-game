import pygame as pg

from settings import *

class BattleInterface:

    def __init__(self):
        
        self.position = (0, SCREEN_HEIGHT - BOTTOM_PANEL)
        self.images = self.load_images()
        self.healthbars = []

    def update(self):
        
        pass

    
    def draw(self, screen):

        screen.blit(self.images["panel_img"], self.position)
        
        # for healthbar in self.healthbars:
        #     healthbar.draw()

    
    def load_images(self):
        
        panel_img = pg.image.load('img/Icons/panel.png').convert_alpha()

        temp_images = {
            "panel_img": panel_img
        }

        return temp_images

    # def create_healthbar(self, x, y, current_hp, max_hp, screen):
        
    #     self.healthbars.append(pg.draw.rect(screen, RED, (x, y, current_hp, max_hp)))