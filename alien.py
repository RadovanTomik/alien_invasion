import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Init. the alien and it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load the alien image ane set rect atribute
        self.image = pygame.image.load(
        'C:/Users/tomas/PycharmProjects/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's next horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """ Move the alien to the reight"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        """Return true if alien is on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True