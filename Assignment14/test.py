import arcade
import random

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

class Enemy(arcade.Sprite):
    def __init__(self, w, h, speed):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, w)
        self.center_y = h + 25
        self.width = 50
        self.height = 50
        self.angle = 180
        self.speed = speed  # Set enemy speed
    
    def move(self):
        self.center_y -= self.speed  # Move based on speed

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 10
        self.angle = 90

    def move(self):
        self.center_y += self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width, "Nastaran")
        self.enemy_list = []
        self.score = 0
        self.lives = 3  # Number of lives
        self.game_over = False  # Track if the game is over

        # New attributes for timing and enemy speed
        self.enemy_spawn_timer = 0  # Timer to track time between enemy spawns
        self.enemy_speed = 3  # Initial speed of enemies
        self.enemy_spawn_interval = 3  # 3-second interval for enemy spawn

    def on_draw(self):
        arcade.start_render()
        
        if self.game_over:
            # Draw black screen and show "GAME OVER"
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text(
                "GAME OVER", 
                self.width // 2, 
                self.height // 2, 
                arcade.color.WHITE, 
                font_size=40, 
                anchor_x="center", 
                bold=True
            )
        else:
            # Continue game rendering
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
            self.me.draw()
            for enemy in self.enemy_list:
                enemy.draw()
            for bullet in self.me.bullet_list:
                bullet.draw()

            # Display lives and score
            arcade.draw_text(f"Score: {self.score}", self.width - 120, 10, arcade.color.WHITE, font_size=20, bold=True)
            arcade.draw_text(f"Lives: {'♥' * self.lives}", 10, 10, arcade.color.RED, font_size=20, bold=True)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        if self.game_over:
            return  # Stop updating if the game is over

        # Collision detection
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                self.lives -= 1  # Reduce lives when enemy hits the player
                self.enemy_list.remove(enemy)  # Remove enemy
                if self.lives == 0:
                    self.game_over = True  # End the game if no lives are left

        # Enemy and bullet collision
        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1  # Increase score when enemy is hit

        # Move spaceship and bullets
        self.me.move()
        for bullet in self.me.bullet_list:
            bullet.move()
        for enemy in self.enemy_list:
            enemy.move()

        # Remove bullets and enemies out of bounds
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy.center_y > 0]
        self.me.bullet_list = [bullet for bullet in self.me.bullet_list if bullet.center_y < self.height]

        # Timer for spawning enemies
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.new_enemy = Enemy(self.width, self.height, self.enemy_speed)
            self.enemy_list.append(self.new_enemy)
            self.enemy_spawn_timer = 0  # Reset timer

            # Gradually increase enemy speed
            self.enemy_speed += 0.1

window = Game()
arcade.run()
