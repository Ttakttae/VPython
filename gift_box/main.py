# big box #
box(pos=vec(0, -5, 0), size=vec(10, 1, 10))
box(pos=vec(-5, 0, 0), size=vec(1, 10, 10))
box(pos=vec(5, 0, 0), size=vec(1, 10, 10))
box(pos=vec(0, 0, -5), size=vec(10, 10, 1))
box(pos=vec(0, 0, 5), size=vec(10, 10, 1))

doors = [box(pos=vec(-2.5, 5, 0), size=vec(5, 1, 10)), \
        box(pos=vec(2.5, 5, 0), size=vec(5, 1, 10))]

door_open_time = 3

timer = 0

while True:
  rate(60)
  timer += 1 / 60
  
  if door_open_time 
  door_x = 2.5 + (2.5 / door_open_time * timer)
  
  doors[0].pos.x = - door_x
  doors[1].pos.x = door_x
