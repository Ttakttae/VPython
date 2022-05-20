import random
a = []
while True:
  for i in range(100):
    rate(50)
    x = random.randint(-30, 30)
    y = random.randint(-30, 30)
    z = random.randint(-30, 30)
    if i % 3 == 0:
      a.append(box(color=color.red, pos=vec(x, y, z), size=vec(10, 10, 10)))
    elif i % 3 == 1:
      a.append(sphere(color=color.green, radius=5,pos=vec(x, y, z)))
    elif i % 3 == 2:
      a.append(cone(color=color.blue, size=vec(10, 10, 10), pos=vec(x, y, z)))
  
  end = False
  while not end:
    rate(10)
    
    # center pos: 0, 0, 0
    for j in a:
      if j.pos.x < 1 and j.pos.y < 1 and j.pos.z < 1:
        j.pos = vec(0, 0, 0)
      else:
        dx = - j.pos.x / 10
        dy = - j.pos.y / 10
        dz = - j.pos.z / 10
        
        j.pos = vec(j.pos.x + dx, j.pos.y + dy, j.pos.z + dz)
    
    all_center = True
    for j in a:
      if not j.pos == vec(0, 0, 0):
        all_center = False
        break
    
    if all_center:
      end = True
  
  for j in a:
    j.visible = False
    del j
