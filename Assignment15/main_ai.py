import arcade
import random
from snake import Snake
from fruits import Apple, Pear, RottenFruit


class AISnake(Snake):
    def __init__(self, game):
        super().__init__(game)

    def auto_move(self, fruits):
        head_x = self.center_x
        head_y = self.center_y

        closest_fruit = min(
            (fruit for fruit in fruits), 
            key=lambda fruit: abs(fruit.center_x - head_x) + abs(fruit.center_y - head_y))

        if closest_fruit:
            if abs(head_x - closest_fruit.center_x) > abs(head_y - closest_fruit.center_y):
                if head_x < closest_fruit.center_x:
                    self.change_x = 1
                    self.change_y = 0
                else:
                    self.change_x = -1
                    self.change_y = 0
            else:
                if head_y < closest_fruit.center_y:
                    self.change_y = 1
                    self.change_x = 0
                else:
                    self.change_y = -1
                    self.change_x = 0

        self.move()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍 AI Mode")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = AISnake(self)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.rottenfruit = RottenFruit(self)

        self.fruits = [self.apple, self.pear, self.rottenfruit]
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        self.snake.draw()
        for fruit in self.fruits:
            fruit.draw()

        arcade.draw_text(f"Score: {self.snake.score}", 10, 10, arcade.color.WHITE, 16)
        if self.game_over:
            arcade.draw_text("Game Over", self.width // 2 - 140, self.height // 2, arcade.color.RED, font_size=40)

    def on_update(self, delta_time: float):
        if self.game_over:
            return

        self.snake.auto_move(self.fruits)

        for fruit in self.fruits:
            if arcade.check_for_collision(self.snake, fruit):
                self.snake.score += fruit.score_fruit
                self.fruits.remove(fruit)

                new_fruit = random.choice([Apple(self), Pear(self)]) if fruit.score_fruit > 0 else RottenFruit(self)
                self.fruits.append(new_fruit)

        if self.snake.score < 0:
            self.snake.score = 0
            self.game_over = True


if __name__ == "__main__":
    game = Game()
    arcade.run()

