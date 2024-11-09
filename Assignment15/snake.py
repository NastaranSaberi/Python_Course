import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.colors = [arcade.color.BLUE, arcade.color.ORANGE]
        self.change_x = 0
        self.center_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.colors[1])
  
        for i in range(len(self.body)):
            color = self.colors[i % 2]
            arcade.draw_rectangle_filled(self.body[i]['x'], self.body[i]['y'], self.width, self.height, color)

    def move(self):
        self.body.append({'x':self.center_x, 'y':self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def check_self_collision(self):
        head_x = self.center_x
        head_y = self.center_y
        for segment in self.body[:-1]:
            if (head_x == segment['x']) and (head_y == segment['y']):
                return True
        return False

    def eat(self, fruits):
        self.score += fruits.score_fruit
        print("Score:", self.score)
    
   
       