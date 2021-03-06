from vpython import *
import random

particles = []

while True:
  rate(60) # fps 60

  # particle
  # [box, [d, acc]
  particles.append([sphere(), [random.randint(0, 20) / 10 - 1, -2, random.randint(0, 20) / 10 - 1]])

  for particle in particles:
    particle[0].pos.x -= particle[1][0]
    particle[0].pos.y -= particle[1][1]
    particle[0].pos.z -= particle[1][2]

    # add acc
    particle[1][1] += 0.1

    # random color
    particle[0].color = vec(random.randint(0, 100) / 100, random.randint(0, 100) / 100, random.randint(0, 100) / 100)

    # if box y <= -100 ---> remove
    if particle[0].pos.y <= -200:
      particles.remove(particle)
