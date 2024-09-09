import arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 10
        self.angle = 90

    def move(self):
        self.center_y += self.speed
     

