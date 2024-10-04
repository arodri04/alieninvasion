import sys
import pygame

#making a handler to check events
def check_events(ship):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #moves ship to right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

#update the screen when something happens
def update_screen(ai_settings, screen, ship):
    #each time main loop goes it will redraw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()