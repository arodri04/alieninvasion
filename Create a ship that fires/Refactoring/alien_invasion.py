############################################
# Software Req Doc: Alien Invasion
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Start of the alien invasion
# In this folder will be creating 
#  a ship and making it fire.
############################################

import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

#defining global variables
screenSize = (1200, 800)

def run_game():
    #Start things that pygame needs to run
    #Create a display window.
    #initialize settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #This sets title at top of window
    pygame.display.set_caption("Alien Invasion")

    #adding the ship from import
    ship = Ship(screen)
    #background Color
    bg_color = (230, 230, 230)

    while True:
        #Getting key and mouse events ---MOVED TO GAME FUNCTION-----
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        ship.update()
        
        #applying the bg color to screen ---MOVED TO GAME FUNCTION-----
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #Make Screen visible now
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship)

run_game()