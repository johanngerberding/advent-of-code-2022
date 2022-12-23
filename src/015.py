
def manhattan(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("../inputs/015.txt", 'r') as fp: 
    data = [el.strip() for el in fp.readlines()]

sensors = []
beacons = []

for line in data: 
    sensor, beacon = line.split(":")
    bx = int(beacon[beacon.index("x=") + 2:beacon.index(",")])
    by = int(beacon[beacon.index("y=") + 2:])
    beacons.append((bx, by)) 
    sx = int(sensor[sensor.index("x=") + 2:sensor.index(",")])
    sy = int(sensor[sensor.index("y=") + 2:])
    md = manhattan((bx, by), (sx, sy)) 
    sensors.append((sx, sy, md))

row = 2000000 
min_x = 10000000
max_x = -10000000
for sensor, beacon in zip(sensors, beacons): 
    md = manhattan(sensor, beacon)
    minx = sensor[0] - md 
    maxx = sensor[0] + md 
    # miny = sensor[1] - md 
    # maxy = sensor[1] + md 
    if minx < min_x: 
        min_x = minx
    if maxx > max_x: 
        max_x = maxx

    """ 
    for i in range(minx, maxx + 1): 
        for j in range(miny, maxy + 1):
            temp = manhattan(sensor, (i, j))
            if temp <= md and not area.get((i, j)):
                area[(i, j)] = "#" 
    """
count = 0
points = []
for x in range(min_x, max_x): 
    point = (x, row)
    for sensor in sensors: 
        md = manhattan((sensor[0], sensor[1]), point)
        if md <= sensor[2]: 
            points.append(point)

points = set(points)
count = len(points)
sbs = []

for sensor, beacon in zip(sensors, beacons): 
    if sensor[1] == row:
        sbs.append((sensor[0], sensor[1]))
    if beacon[1] == row:
        sbs.append(beacon)

sbs = set(sbs)
count -= len(sbs)
"""
for key, val in area.items(): 
    if key[1] == 2000000 and val == "#": 
        count += 1
"""

print(f"Solution Part 1: {count}")