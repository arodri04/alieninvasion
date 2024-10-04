import sys
import pygame

#making a handler to check events
def check_events(ship):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

#update the screen when something happens
def update_screen(ai_settings, screen, ship):
    #each time main loop goes it will redraw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False