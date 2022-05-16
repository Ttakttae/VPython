from vpython import *


class Ball:
    def __init__(self, main):
        self.main = main
        self.make_ball_bar()
        self.make_ball()

    def make_ball_bar(self):
        self.ball_bar = box(color=color.blue, size=vector(5, 0.3, 0.1), pos=vector(0, -7.5, 0))

    def bar_movement(self):
        ev = keysdown()
        if 'left' in ev:
            if self.ball_bar.pos.x - 2.6 <= self.main.wall.left_wall.pos.x:
                pass
            else:
                self.ball_bar.pos.x -= 0.00003
        elif 'right' in ev:
            if self.ball_bar.pos.x + 2.6 >= self.main.wall.right_wall.pos.x:
                pass
            else:
                self.ball_bar.pos.x += 0.00003

    def make_ball(self):
        self.ball = sphere(color=color.magenta, pos=vector(0, -7, 0), size=vector(0.7, 0.7, 0.7))

class Blocks:
    def __init__(self, main):
        self.main = main
        self.blocks = []
        self.set_blocks()

    def set_blocks(self):
        for x in range(-10, 10, 2):
            for y in range(2, 6):
                if y == 2:
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.green))
                elif y == 3:
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.yellow))
                elif y == 4:
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.orange))
                elif y == 5:
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.red))

class Wall:
    def __init__(self, main):
        self.main = main
        self.make_wall()

    def make_wall(self):
        self.left_wall = box(size=vector(0.1, 15, 0.1), pos=vector(-10.1, 0, 0))
        self.right_wall = box(size=vector(0.1, 15, 0.1), pos=vector(10.1, 0, 0))
        self.upper_wall = box(size=vector(20.2, 0.1, 0.1), pos=vector(0, 7.5, 0))

class Main:
    def __init__(self):
        monitor = canvas(width=1300, height=800)
        self.ball = Ball(self)
        self.blocks = Blocks(self)
        self.wall = Wall(self)

if __name__ == "__main__":
    main = Main()
    while True:
        main.ball.bar_movement()