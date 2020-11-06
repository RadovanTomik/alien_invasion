class GameStats:
    """Track statistics"""
    
    def __init__(self, ai_game):
        """Init the stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start the game in inactive state
        self.game_active = False
        self.high_score = 0
        
    def reset_stats(self):
        """Init stats that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0