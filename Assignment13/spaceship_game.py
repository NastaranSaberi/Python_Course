import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = 150
        self.width = 100
        self.height = 100
        self.name = name
        self.speed = 10


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 25
        self.width = 50
        self.height = 50
        self.angle = 180
        self.speed = 4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self, "Nastaran")
        self.doshman = Enemy(self.width, self.height)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print("dokmeee")
        print(symbol)
        if symbol == 97:
            self.me.center_x += self.me.speed
        if symbol == 100:
            self.me.center_x -= self.me.speed

    def on_update(self, delta_time: float):
        self.doshman.center_y -= self.doshman.speed


window = Game()
arcade.run()
        


