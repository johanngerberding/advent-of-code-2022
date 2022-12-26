import tqdm 
from typing import Tuple 
from dataclasses import dataclass


@dataclass 
class XY: 
    x: int 
    y: int 


class Sensor:
    def __init__(self, sensor: XY, beacon: XY): 
        self.sensor = sensor 
        self.beacon = beacon
        self.md = self.manhattan(sensor, beacon)
        self.intervals = self.row_intervals() 

    def manhattan(self, p1: XY, p2: XY) -> int: 
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
    
    def row_intervals(self):
        intervals = {}  
        intervals[self.sensor.y] = [self.sensor.x - self.md, self.sensor.x + self.md] 
        for i in range(1, self.md + 1):
            diff = self.md - i 
            # up 
            intervals[self.sensor.y - i] = [self.sensor.x - diff, self.sensor.x + diff] 
            # down  
            intervals[self.sensor.y + i] = [self.sensor.x - diff, self.sensor.x + diff]

        return intervals 

    def __str__(self): 
        return f"Sensor {self.sensor} | Beacon {self.beacon} | Distance: {self.md} | Number of Intervals: {len(self.intervals)}"

    def print_intervals(self): 
        for k, val in self.intervals.items():
            print(f"Row {k}: {val}")
            

def merge_intervals(intervals: list): 
    intervals.sort()
    stack = [] 
    stack.append(intervals[0])
    for inter in intervals[1:]: 
        if stack[-1][0] <= inter[0] <= (stack[-1][-1] + 1): 
            stack[-1][-1] = max(stack[-1][-1], inter[-1])
        else:
            stack.append(inter)
    
    return stack 


with open("../inputs/015.txt", 'r') as fp: 
    data = [el.strip() for el in fp.readlines()]

sensors = []

for line in data: 
    sensor, beacon = line.split(":")
    bx = int(beacon[beacon.index("x=") + 2:beacon.index(",")])
    by = int(beacon[beacon.index("y=") + 2:])
    sx = int(sensor[sensor.index("x=") + 2:sensor.index(",")])
    sy = int(sensor[sensor.index("y=") + 2:])
    sensors.append(Sensor(XY(sx, sy), XY(bx, by)))

intervals = {}
for sensor in sensors: 
    for key, val in sensor.intervals.items():
        if key in intervals: 
            intervals[key].append(val)
        else: 
            intervals[key] = [val] 

merged_intervals = {}
for key, val in tqdm.tqdm(intervals.items()): 
    merged = merge_intervals(val)
    merged_intervals[key] = merged 

num_rows_cols = 4_000_000 
inters = {}

for i in range(num_rows_cols + 1): 
    if merged_intervals.get(i): 
        inters[i] = merged_intervals[i]

# for key, val in inters.items(): 
#     print(f"Row {key} -> {val}")

for key, val in inters.items(): 
    if len(val) > 1:
        print(f"Row {key} -> {val}")
        y = key 
        x = val[0][1] + 1 
        print(f"Solution Part 2: {x * 4_000_000 + y}")

"""
ninters = {} 
for key, val in inters.items(): 
    print(f"Row {key} -> {val}")
    if len(val) > 1: 
        vals = [] 
        for i in range(len(val) - 1): 
            if val[i][1] == (val[i + 1][0] - 1): 
                vals.append([val[i][0], val[i+1][1]])
    
        ninters[key] = vals  
    else: 
        ninters[key] = val         

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

print(f"Solution Part 1: {count}")
points = []
for x in tqdm.tqdm(range(0, 4000000)): 
    for y in range(0, 4000000): 
        beacon = (x, y)
        for sensor in sensors: 
            md = manhattan((sensor[0], sensor[1]), beacon)
            if md <= sensor[2]: 
                points.append(beacon)

print(len(points))
"""
