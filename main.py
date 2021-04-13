import pygame as pg
import os

from settings import *

from game import Game

def main():

    pg.init()
    pg.mixer.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    running = True
    playing = True

    game = Game(screen, clock)

    while running:
        pass
        # Start menu

        while playing:
            # Game loop
            game.run()


if __name__ == "__main__":
    
    main()