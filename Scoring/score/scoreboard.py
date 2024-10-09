############################################
# Software Req Doc: Scoreboard Module
# Release Date: 10/2/24
# Sam Rodriguez
# Description: Module make the a scoreboard
# for the game.
############################################
import pygame.font

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        #initialize attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #font for scoring information
        self.text_color = (30, 30, 30)
        self. font = pygame.font.SysFont(None, 48)

        #prep initial score image
        self.prep_score()

    def prep_score(self):
        #render the score
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #put it at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #put score on screen
        self.screen.blit(self.score_image, self.score_rect)