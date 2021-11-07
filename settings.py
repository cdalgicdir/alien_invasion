
class Settings:
    
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Bomb settings
        self.bomb_speed = 1.0
        self.bomb_width = 300
        self.bomb_height = 30
        self.bomb_color = (255, 0, 0)
        self.bombs_allowed = 1

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1 # 1: right, -1: left