############################################
# Software Req Doc: Alien Invasion
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Start of the alien invasion
# In this folder will be creating 
#  a ship and making it fire.
############################################

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from game_stats import GameStats


def run_game():
    #Start things that pygame needs to run
    #Create a display window.
    #initialize settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #This sets title at top of window
    pygame.display.set_caption("Alien Invasion")

    #Create GameStats instance
    stats = GameStats(ai_settings)

    #adding the ship from import
    ship = Ship(ai_settings, screen)


    #Make group to store bullets in
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    while True:
        #Getting key and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        #applying the bg color to screen 
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()