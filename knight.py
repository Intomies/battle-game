import pygame as pg

from settings import *

from fighter import Fighter


class Knight(Fighter):

    def __init__(self, char_type, max_hp, strength, potions, count):

        self.char_type = char_type
        self.max_hp = max_hp
        self.strength = strength
        self.count = count
        
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
        self.images_list = Fighter.load_images(self)
        self.image = self.images_list[self.current_action][self.current_frame_index]
        self.rect = Fighter.get_rect(self)
        self.rect.center = (Fighter.get_position(self))