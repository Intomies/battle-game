import pygame as pg

from settings import *

class World:

    def __init__(self, width, height):

        self.width = width
        self.height = height
     
        self.background_pos = (0,0)
        self.panel_pos = (0, SCREEN_HEIGHT - BOTTOM_PANEL)

        self.images = self.load_images()
        
    
    def update(self):
        
        pass

    
    def draw(self, screen):

        screen.blit(self.images["background_img"], self.background_pos)
        screen.blit(self.images["panel_img"], self.panel_pos)

    
    def load_images(self):
        
        background_img = pg.image.load('img/Background/background.png').convert_alpha()
        panel_img = pg.image.load('img/Icons/panel.png').convert_alpha()

        images = {
            "background_img": background_img,
            "panel_img": panel_img
        }

        return images
