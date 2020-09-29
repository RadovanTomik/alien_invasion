import pygame

class Ship:
    """A class for the ship."""
    
    def __init__(self, ai_game):
        """Init. the ship and set the starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/tomas/PycharmProjects/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at mid bottom
        self.rect.midbottom = self.screen_rect.midbottom
        # Store decimal value of horizontal value of the ship
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """Center a neew ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the shps position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        #Update the object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship in it's current location"""
        self.screen.blit(self.image, self.rect)