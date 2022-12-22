

with open("../inputs/014.txt", 'r') as fp: 
    data = [el.strip() for el in fp.readlines()]

rocks = {}
min_x = 100000
max_y = -1 
max_x = -1

for line in data: 
    parts = line.split("->")
    parts = [el.strip().split(",") for el in parts] 

    coords = []

    for points in parts: 
        x = int(points[0])
        y = int(points[1])
        coords.append((x, y))

        if x < min_x: 
            min_x = x 

        if x > max_x: 
            max_x = x 
        
        if y > max_y:
            max_y = y 

    for i in range(len(coords) - 1): 
        start = coords[i]
        stop = coords[i + 1]
        if start[0] == stop[0]: 
            # same x
            for j in range(min(start[1], stop[1]), max(start[1], stop[1]) + 1):
                rocks[(start[0], j)] = True   
        elif start[1] == stop[1]:
            # same y 
            for j in range(min(start[0], stop[0]), max(start[0], stop[0]) + 1):
                rocks[j, (start[1])] = True
        else: 
            print("We have a problem")


sand = (500, 0)
overflow = False
sand_count = 0 
while not overflow:
    if sand[0] > max_x or sand[0] < min_x or sand[1] > max_y: 
        overflow = True  
    
    future = (sand[0], sand[1] + 1)
    if rocks.get(future): 
        # check left down 
        left = (future[0] - 1, future[1])
        if rocks.get(left):
            # check right down
            right = (future[0] + 1, future[1])
            if rocks.get(right): 
                rocks[sand] = True 
                sand_count += 1  
                print(f"Sand stopped: {sand}")
                sand = (500, 0) 
            else: 
                sand = right
        else: 
            sand = left 
    else: 
        sand = future

print(f"Solution Part 1: {sand_count}") 