from vpython import *
import random


balls = []

for i in range(50):
    x = random.randint(-10, 10)
    for j in range(2):
        if j == 0:
            y = (100 - x ** 2) ** 0.5
        if j == 1:
            y = -(100 - x ** 2) ** 0.5
    balls.append(sphere(pos=vec(x, y, 0), radius=0.5))

while True:
    rate(180)
    for i in balls:
        if i.pos.y >= 0:
            if i.pos.x >= 10:
                i.pos.x -= 0.1
                i.pos.y = -(103 - i.pos.x ** 2) ** 0.5
            else:
                i.pos.x += 0.1
                i.pos.y = (103 - i.pos.x ** 2) ** 0.5
        else:
            if i.pos.x <= -10:
                i.pos.x += 0.1
                i.pos.y = (103 - i.pos.x ** 2) ** 0.5
            else:
                i.pos.x -= 0.1
                i.pos.y = -(103 - i.pos.x ** 2) ** 0.5
    for j in balls:
        r = random.randint(0, 10)
        g = random.randint(0, 10)
        b = random.randint(0, 10)
        j.color = vec(r/10, g/10, b/10)