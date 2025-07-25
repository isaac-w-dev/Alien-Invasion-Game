import random
class Settings:
    def __init__(self):
        self.clock_tick = 60
        self.screen_width = 1200
        self.screen_height = 800
        self.dimensions = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.alien_speed = 30.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1
        self.number_of_lives = 3
        self.ships_in_each_row = []
        
        for i in range(0, 5):
            self.ships_in_each_row.append(random.randint(1, 7))