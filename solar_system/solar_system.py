from vpython import *


sun=sphere(radius=18, color=color.red)
mercury=sphere(radius=0.4, color=vec(153/255, 56/255, 0), pos=vec(19,0,0))
venus=sphere(radius=0.9, color=color.yellow, pos= vec(21,0,0))
earth=sphere(radius=1, color=color.cyan, pos=vec(25,0,0))
mars=sphere(radius=0.5, color=color.yellow, pos=vec(30,0,0))
jupiter=sphere(radius=11.2, color=vec(153/255, 56/255, 0), pos=vec(50,0,0))
saturn=sphere(radius=9.4, color=vec(242/255,150/255,97/255), pos=vec(80,0,0))
uranos=sphere(radius=4, color=color.cyan, pos=vec(105,0,0))
planets = []
planets.append(mercury)
planets.append(venus)
planets.append(earth)
planets.append(mars)
planets.append(jupiter)
planets.append(saturn)
planets.append(uranos)



while True:
  rate(50)
  for i in planets:
    radius = i.pos.x
    if i.pos.z >= 0:
      if i.pos.x >= radius:
        i.pos.x -= 0.1
        i.pos.z = -(radius ** 2 - i.pos.x ** 2) ** 0.5
      else:
        i.pos.x += 0.1
        i.pos.z = (radius ** 2 - i.pos.x ** 2) ** 0.5
    else:
      if i.pos.x <= -radius:
        i.pos.x += 0.1
        i.pos.z = (radius ** 2 - i.pos.x ** 2) ** 0.5
      else:
        i.pos.x -= 0.1
        i.pos.z = -(radius ** 2 - i.pos.x ** 2) ** 0.5