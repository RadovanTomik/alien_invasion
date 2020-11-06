class Settings:
    """A class to store all setings for the game"""
    
    def __init__(self):
        """Init. the game settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 0
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # Fleet direction, 1 represents right and -1 left
        self.fleet_direction = 1
        
        #Speeding up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Setting that change"""
        # Fleet direction, 1 represents right and -1 left
        self.fleet_direction = 1
        
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.ship_speed = 1.5
        self.alien_points = 50
        self.score_scale = 1.5
        
    def increase_speed(self):
        """Increase speed and alien points"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)