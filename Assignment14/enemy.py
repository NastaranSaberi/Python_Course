import random
from turtle import speed
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 25
        self.width = 50
        self.height = 50
        self.angle = 180
        self.speed = 2
    
    def move(self):
        self.center_y -= self.speed
