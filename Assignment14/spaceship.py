import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = w // 2
        self.center_y = 150
        self.change_x = 0
        self.change_y = 0
        self.width = 100
        self.height = 100
        self.name = name
        self.speed = 4
        self.game_width = w
        self.bullet_list = []
        self.fire_sound = arcade.load_sound(":resources:sounds/laser2.wav")

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
