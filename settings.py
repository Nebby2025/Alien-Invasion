class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 243, 0)
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 25
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1