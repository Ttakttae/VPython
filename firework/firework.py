from vpython import *
import random, time


while True:
    Canvas = canvas()
    # Canvas.width = 1300
    # Canvas.height = 800
    fireworks = []
    for i in range(5):
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        r = random.randint(0, 10)
        g = random.randint(0, 10)
        b = random.randint(0, 10)
        firework1 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework2 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework3 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework4 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework5 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework6 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework7 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework8 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework9 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework10 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework11 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework12 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework13 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework14 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework15 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        firework16 = sphere(pos=vec(x, y, 0), color=vec(r/10, g/10, b/10), size=vec(0.5, 0.5, 0.5), make_trail=True)
        fireworks.append(firework1)
        fireworks.append(firework2)
        fireworks.append(firework3)
        fireworks.append(firework4)
        fireworks.append(firework5)
        fireworks.append(firework6)
        fireworks.append(firework7)
        fireworks.append(firework8)
        fireworks.append(firework9)
        fireworks.append(firework10)
        fireworks.append(firework11)
        fireworks.append(firework12)
        fireworks.append(firework13)
        fireworks.append(firework14)
        fireworks.append(firework15)
        fireworks.append(firework16)
        for a in range(7):
            firework1.pos.x += 1
            firework1.pos.y += 1
            firework2.pos.x += -1
            firework2.pos.y += 1
            firework3.pos.x += -1
            firework3.pos.y += -1
            firework4.pos.x += 1
            firework4.pos.y += -1
            firework5.pos.x += 1
            firework5.pos.y += 0.5
            firework6.pos.x += -1
            firework6.pos.y += 0.5
            firework7.pos.x += -1
            firework7.pos.y += -0.5
            firework8.pos.x += 1
            firework8.pos.y += -0.5
            firework9.pos.x += 1
            firework9.pos.y += 2
            firework10.pos.x += -1
            firework10.pos.y += 2
            firework11.pos.x += -1
            firework11.pos.y += -2
            firework12.pos.x += 1
            firework12.pos.y += -2
            firework13.pos.x += 1
            firework14.pos.x += -1
            firework15.pos.y += 1
            firework16.pos.y += -1
            time.sleep(0.01)
        for b in range(3):
            firework1.pos.x += 1
            firework1.pos.y += 1
            firework2.pos.x += -1
            firework2.pos.y += 1
            firework3.pos.x += -1
            firework3.pos.y += -1
            firework4.pos.x += 1
            firework4.pos.y += -1
            firework5.pos.x += 1
            firework5.pos.y += 0.5
            firework6.pos.x += -1
            firework6.pos.y += 0.5
            firework7.pos.x += -1
            firework7.pos.y += -0.5
            firework8.pos.x += 1
            firework8.pos.y += -0.5
            firework13.pos.x += 1
            firework14.pos.x += -1
            firework15.pos.y += 1
            firework16.pos.y += -1
            time.sleep(0.01)
        for c in range(3):
            firework5.pos.x += 1
            firework5.pos.y += 0.5
            firework6.pos.x += -1
            firework6.pos.y += 0.5
            firework7.pos.x += -1
            firework7.pos.y += -0.5
            firework8.pos.x += 1
            firework8.pos.y += -0.5
            firework13.pos.x += 1
            firework14.pos.x += -1
            firework15.pos.y += 1
            firework16.pos.y += -1
            time.sleep(0.01)
        for d in range(3):
            firework13.pos.x += 1
            firework14.pos.x += -1
            firework15.pos.y += 1
            firework16.pos.y += -1
            time.sleep(0.01)
    time.sleep(5)
    Canvas.delete()