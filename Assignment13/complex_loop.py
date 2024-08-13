import arcade

class Diamond(arcade.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.size = size
        self.color = color

    def draw(self):
        diamond_shape = [
            (self.center_x, self.center_y + self.size),  
            (self.center_x + self.size, self.center_y),   
            (self.center_x, self.center_y - self.size),   
            (self.center_x - self.size, self.center_y)    
        ]
        arcade.draw_polygon_filled(diamond_shape, self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=400, height=400, title="Complex Loops")
        arcade.set_background_color(arcade.color.WHITE)
        self.shapes = []

    def setup(self):
        COLUMN_SPACING = 20
        ROW_SPACING = 20
        LEFT_MARGIN = 110
        BOTTOM_MARGIN = 110
        size = 7

        for row in range(10):
            for column in range(10):
                x = column * COLUMN_SPACING + LEFT_MARGIN
                y = row * ROW_SPACING + BOTTOM_MARGIN

                if (row + column) % 2 == 0:
                    color = arcade.color.RED
                else:
                    color = arcade.color.BLUE

                diamond = Diamond(x, y, size, color)
                self.shapes.append(diamond)

    def on_draw(self):
        arcade.start_render()
        for shape in self.shapes:
            shape.draw()


window = Game()
window.setup()
arcade.run()