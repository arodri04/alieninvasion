############################################
# Software Req Doc: Model for the controls
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Handles all the inputs for
# button.
############################################
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

#making a handler to check events
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

#starts new game when user presses play
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #hide the mouse when game starts
        pygame.mouse.set_visible(False)
        #reset stats
        stats.reset_stats()
        stats.game_active = True

        #get rid of bullets and aliens
        aliens.empty()
        bullets.empty()

        #create new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        

#update the screen when something happens
def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    #each time main loop goes it will redraw screen
    screen.fill(ai_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #make the play button
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #making a new bullet
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    #quit on Q
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #updates the fired bullets
    bullets.update()

    #Remove Bullets that disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    #Check if bullets collide with aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #check if fleet is empty and repopulate
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    

def change_fleet_direction(ai_settings, aliens):
    #drop fleet and change directions
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    #Remove life
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #empty list of alien and bullets
        aliens.empty()
        bullets.empty()

        #Make a new fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    #check if aliens get to the bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat it like ship getting hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break



def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    #updates the alien positions in the fleet
    check_fleet_edges(ai_settings, aliens)

    #once aliens are updated check if they hit the bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def fire_bullet(ai_settings, screen , ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    #find out and return how many aliens from row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    #number of rows of aliens on screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #create alien and place it in roll
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    #create aliens and find out how many are in the rows
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Create alien and place it in row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
