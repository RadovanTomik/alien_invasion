import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the current position of a ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet at (0,0) and reposition
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullets position as a decimal
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    