############################################
# Software Req Doc: game stats
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module to handle all the game 
# stats
############################################

class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #create a game State
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit