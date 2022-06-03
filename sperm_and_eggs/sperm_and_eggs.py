from vpython import *
from random import uniform, randint

scene.width = 1300
scene.height = 800


egg = sphere(radius = 50, color=color.yellow)
sperms = []
for i in range(10):
  x = randint(-1100, -900)
  y = randint(-100, 100)
  sperms.append(sphere(radius = 5, pos=vector(x, y, 0), color=color.white))



while True:
  rate(20)
  for i in sperms:
    i.v = vector(5, 0, 0)
    if i.pos.y >= 0:
      i.v.y = uniform(-200, 0)
    else:
      i.v.y = uniform(0, 200)
    i.pos += i.v
    if i.pos.x ** 2 + i.pos.y ** 2 <= 2500:
      quit()
    else:
      pass