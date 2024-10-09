############################################
# Software Req Doc: Settings module
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module to handle all of the
# settings instead of having it in main.
############################################

#Creating class, Capitalize class name
class Settings():

    def __init__(self):
        #settings applied to self here
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #aliens settings
        self.alien_speed_factor = .1
        self.fleet_drop_speed = 10
        #fleet direction 1 is right -1 is left
        self.fleet_direction = 1