############################################
# Software Req Doc: Alien Invasion
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module to create aliens
############################################

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #start each new alien at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)