import random
import arcade

class Fruits(arcade.Sprite):
    def __init__(self, game, image, score_fruit):
        super().__init__(image)
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.score_fruit = score_fruit

class Apple(Fruits):
    def __init__(self, game):
        super().__init__(game, "Images/Apple.webp", 1)

class Pear(Fruits):
    def __init__(self, game):
        super().__init__(game, "Images/Pear.webp", 2)

class RottenFruit(Fruits):
    def __init__(self, game):
        super().__init__(game, "Images/RottenFruit.png", -1)
