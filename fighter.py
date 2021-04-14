import pygame as pg
import os
import random as rand

from settings import *


class Fighter:

    def __init__(self, char_type, max_hp, strength, potions, count):

        self.char_type = char_type
        self.max_hp = max_hp
        self.strength = strength
        self.count = count
        
        self.name = self.get_name()
        self.hp = max_hp
        self.potions = potions
        self.start_potions = potions
        self.alive = True
        self.actions = FIGHTER_ACTIONS # [0: attack, 1: death, 2: hurt, 3: idle]
        
        self.current_action = "idle"
        self.current_frame_index = 0
        self.update_time = pg.time.get_ticks()
        self.animation_cooldown = 100

        self.starting_positions = FIGHTER_START_POSITIONS
        self.fighter_height = FIGHTER_HEIGHT
        self.image_scale = FIGHTER_IMAGE_SCALE
        self.images_list = self.load_images()
        self.image = self.images_list[self.current_action][self.current_frame_index]
        self.rect = self.get_rect()
        self.rect.center = (self.get_position())

        self.health_bar_pos_x = HEALTH_BAR_POSITIONS_X[self.char_type]
        self.health_bar_pos_y = HEALTH_BAR_POSITIONS_Y[self.count]

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

    
    def get_current_health(self):

        return self.hp / self.max_hp

    
    def get_name(self):

        cylls = "ara,gorn,gim,li,grish,nak,sna,ga,ug,luk,boro,mir,fara,lego,las,fro,do,bag,gins,sam,gam,gi,meri,a,doc,ran,di,buk,pe,reg,rin,tuk,gan,dalf,el,rond,dene,thor,eo,wyn,ar,wen,ga,lad,ri,el,gil,gol,lum,tho,rin,bom,ba,dil,tom,lut,hi,en,fi,ki,li,bur,theo,den,bil,bo"
        cylls_arr = cylls.split(",")

        return cylls_arr[rand.randint(0, len(cylls_arr) - 1)].capitalize() + cylls_arr[rand.randint(0, len(cylls_arr)- 1)]



