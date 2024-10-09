############################################
# Software Req Doc: Alien Invasion
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module to create bullets
############################################

import pygame
from pygame.sprite import Sprite

#Creating the bullet class

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #make bullet at (0, 0) then set position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top =  ship.rect.top

        #store bullet position as float
        self.y = float(self.rect.y)

        #Settings
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    #Moving bullet up the screen
    def update(self):
        self.y -= self.speed_factor
        #update position
        self.rect.y = self.y

    def draw_bullet(self):
        #draw bullet to screen
        pygame.draw.rect(self.screen, self.color, self.rect)