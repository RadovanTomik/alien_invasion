import sys, pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

class AlienInavsion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Create an instance to store game stats
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
            
        self._create_fleet()
         
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens()
                self._update_screen()
            
            
    def _check_events(self):
        """Respond to keyboard and mouse presses"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                        
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        """Update a position of bullets and get rid of old bullets"""
        self.bullets.update()
            #Get rid of bullets that have disappered.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_allien_collision()
        
    def _check_bullet_allien_collision(self):
        """ Respond to bullet and alien collision"""
        collisions = pygame.sprite.groupcollide(self.bullets,
                self.aliens, True, True)
        if not self.aliens:
            #Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        
    def _create_fleet(self):
        """Create a fleet of aliens."""
        #make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y =(self.settings.screen_height - (3 * alien_height) -
                                ship_height)
        number_of_aliens_x = available_space_x // (2 * alien_width)
        number_of_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_aliens(self):
        """Update the position of all aliens"""
        
        self._check_fleet_edges()
        self.aliens.update()
        
        #Check for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        #check for aliens hitting bottom
        self._check_aliens_bottom()
    def _ship_hit(self):
        """Respond to the ship being hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
        
            # get rid of bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
        
            #Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
        
    def _check_aliens_bottom(self):
        """Check if any aliens made it to the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat it as if it were a hit
                _ship_hit()
                break
        
    def _update_screen(self):
        """Updates image on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible
        pygame.display.flip()
        
if __name__ == '__main__':
    #Make a game instance
    ai = AlienInavsion()
    ai.run_game()