from vpython import *

# scene.height = 800
# scene.width = 1300


sun=sphere(radius=18, color=color.red)
mercury=sphere(radius=0.4, color=vec(153/255, 56/255, 0), pos=vec(19,0,0))
venus=sphere(radius=0.9, color=color.yellow, pos= vec(21,0,0))
earth=sphere(radius=1, texture=textures.earth, pos=vec(25,0,0))
mars=sphere(radius=0.5, color=color.yellow, pos=vec(30,0,0))
jupiter=sphere(radius=11.2, color=vec(153/255, 56/255, 0), pos=vec(50,0,0))
saturn=sphere(radius=9.4, color=vec(242/255,150/255,97/255), pos=vec(80,0,0))
uranos=sphere(radius=4, color=color.cyan, pos=vec(105,0,0))
neptune=sphere(radius=4.2, color=vec(74/255, 108/255, 238/255), pos=vec(164, 0, 0))
planets = []
planets.append([mercury, mercury.pos.x])
planets.append([venus, venus.pos.x])
planets.append([earth, earth.pos.x])
planets.append([mars, mars.pos.x])
planets.append([jupiter, jupiter.pos.x])
planets.append([saturn, saturn.pos.x])
planets.append([uranos, uranos.pos.x])
planets.append([neptune, neptune.pos.x])


while True:
  rate(50)
  for i in planets:
    if i[0].pos.z >= 0:
      if i[0].pos.x + 0.1 >= i[1]:
        i[0].pos.x -= 0.1
        i[0].pos.z = -abs((i[1] ** 2 - i[0].pos.x ** 2)) ** 0.5
      else:
        i[0].pos.x += 0.1
        i[0].pos.z = abs((i[1] ** 2 - i[0].pos.x ** 2)) ** 0.5
    else:
      if i[0].pos.x - 0.1 <= -i[1]:
        i[0].pos.x += 0.1
        i[0].pos.z = abs((i[1] ** 2 - i[0].pos.x ** 2)) ** 0.5
      else:
        i[0].pos.x -= 0.1
        i[0].pos.z = -abs((i[1] ** 2 - i[0].pos.x ** 2)) ** 0.5