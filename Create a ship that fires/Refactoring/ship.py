############################################
# Software Req Doc: Settings module
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module make the ship
############################################
import pygame

class Ship():

    def __init__(self, screen):
        #Set ship and starting position
        self.screen = screen

        #Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        
        if self.moving_left:
            self.rect.centerx -= 1
    
    #This is to create the image at the rectangle specified
    def blitme(self):

        self.screen.blit(self.image, self.rect)