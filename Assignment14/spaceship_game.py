import time
import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.error_sound = arcade.load_sound(":resources:sounds/error2.wav")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover3.wav")
        self.heart_img = arcade.load_texture("Images/heart.webp")
        self.me = Spaceship(self.width, "Nastaran")
        self.enemy = Enemy(self.width, self.height)
        self.enemy_list = []
        self.score = 0
        self.hearts = 3
        self.game_over = False
        self.time_between_enemies = 3
        self.last_spawn_time = time.time()

    def on_draw(self):
        arcade.start_render()

        if self.game_over:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("GAME OVER", self.width // 2, self.height // 2, arcade.color.RED, font_size=40, anchor_x="center", bold=True)
            
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
            self.me.draw()
            for enemy in self.enemy_list:
                enemy.draw()

            for bullet in self.me.bullet_list:
                bullet.draw()

            for i in range(self.hearts):
                arcade.draw_lrwh_rectangle_textured(10 + i * 50, 10, 40, 40, self.heart_img)

            arcade.draw_text(f"Score: {self.score}", self.width - 120, 10, arcade.color.WHITE, font_size=20, bold=True)
            
    def on_key_press(self, symbol: int, modifiers: int):
        print("dokmeee")
        print(symbol)
        if symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.SPACE:
            self.me.fire()
            arcade.play_sound(self.me.fire_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                self.enemy_list.remove(enemy)
                arcade.play_sound(self.error_sound)
                self.hearts -= 1
                if self.hearts == 0:
                    self.game_over = True
                    arcade.play_sound(self.gameover_sound)
             
        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    arcade.play_sound(self.explosion_sound)
                    self.score += 1

        self.me.move()

        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)

        for bullet in self.me.bullet_list:
            if bullet.center_y >= self.height:
                self.me.bullet_list.remove(bullet)

        time_now = time.time()
        if time_now - self.last_spawn_time >= 3:
            self.new_enemy = Enemy(self.width, self.height)
            self.new_enemy.speed = self.enemy.speed 
            self.enemy_list.append(self.new_enemy)
            self.last_spawn_time = time_now
            self.enemy.speed += 0.3



window = Game()
arcade.run()
        


