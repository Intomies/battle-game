import pygame as pg
import os

from settings import *


class Fighter:

    def __init__(self):
        pass

    def update(self):

        self.image = self.images_list[self.current_action][self.current_frame_index]
        
        if pg.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.current_frame_index += 1

        if self.current_frame_index >= len(self.images_list[self.current_action]):
            self.current_frame_index = 0



    def draw(self, screen):
        
        screen.blit(self.image, self.rect)

    
    def load_images(self):

        all_images = {}

        for i in range(len(self.actions)):
            
            temp_list = []
            DIR = f'img/{self.char_type}/{self.actions[int(i)]}'
            
            for j in range(len([name for name in os.listdir(DIR)])):
                img = pg.image.load(f'{DIR}/{j}.png')
                img = pg.transform.scale(img, (img.get_width() * self.image_scale, img.get_height() * self.image_scale))
                temp_list.append(img)
            
            all_images[self.actions[int(i)]] = temp_list

        return all_images


    def get_rect(self):
        
        return self.image.get_rect()

    
    def get_position(self):
            
        return self.starting_positions[self.char_type][self.count], self.fighter_height[self.char_type]
