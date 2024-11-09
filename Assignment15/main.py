import random 
import arcade
from snake import Snake
from fruits import Apple, Pear, RottenFruit
from main_ai import AISnake
        
    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.rottenfruit = RottenFruit(self)

        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.rottenfruit.draw()

        arcade.draw_text(f"Score: {self.snake.score}", self.width - 120, 10, arcade.color.WHITE, font_size=20, bold=True)
        if self.game_over:
            arcade.draw_text("Game Over", self.width // 2 - 140, self.height // 2, arcade.color.RED, font_size=40)

        arcade.finish_render()

    def on_update(self, delta_time: float):
        if self.game_over:
            return

        self.snake.move()

        if (self.snake.center_x < 0 or self.snake.center_x > self.width or
            self.snake.center_y < 0 or self.snake.center_y > self.height):
            self.game_over = True

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat(self.apple)
            self.apple = Apple(self)
        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat(self.pear)
            self.pear = Pear(self)
        if arcade.check_for_collision(self.snake, self.rottenfruit):
            self.snake.eat(self.rottenfruit)
            self.rottenfruit = RottenFruit(self)

        if self.snake.score < 0:
            self.snake.score = 0
            self.game_over = True

        if self.snake.check_self_collision():
            self.game_over = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()