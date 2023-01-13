from collections import deque

def neighbors(xyz: tuple) -> list:
    return [
        (xyz[0], xyz[1], xyz[2] + 1), 
        (xyz[0], xyz[1], xyz[2] - 1), 
        (xyz[0] + 1, xyz[1], xyz[2]), 
        (xyz[0] - 1, xyz[1], xyz[2]), 
        (xyz[0], xyz[1] + 1, xyz[2]), 
        (xyz[0], xyz[1] - 1, xyz[2]),
    ]


with open("../inputs/018.txt", 'r') as fp: 
    data = [el.strip().split(',') for el in fp.readlines()]

cubes = {}
min_x, min_y, min_z = 100, 100, 100 
max_x, max_y, max_z = -1, -1, -1

for el in data: 
    x, y, z = (int(el[0]), int(el[1]), int(el[2])) 
    cube = (x, y, z) 
    min_x = x if x < min_x else min_x 
    max_x = x if x > max_x else max_x
    min_y = y if y < min_y else min_y 
    max_y = y if y > max_y else max_y
    min_z = z if z < min_z else min_z 
    max_z = z if z > max_z else max_z
    cubes[cube] = 6 

updated = {}
for cube, dof in cubes.items(): 
    ns = neighbors(cube)
    c = 0 
    for n in ns: 
        if n in cubes:
            c += 1 
    updated[cube] = 6 - c  

dofs = 0 
for cube, dof in updated.items(): 
    dofs += dof 

print(f"Solution Part 1: {dofs}")

out = [] 
for x in range(min_x - 1, max_x + 2): 
    for y in range(min_y - 1, max_y + 2): 
        for z in range(min_z - 1, max_z + 2): 
            if (x, y, z) not in updated: 
                out.append((x, y, z))

print(len(out))

out_rocks = set(out)
adjs = deque([out[0]]) 

rocks = []

while True: 
    adj = adjs.pop()
    rocks.append(adj)
    if adj in out_rocks: 
        out_rocks.remove(adj)
    # print(f"len out rocks: {len(out_rocks)}") 
    ns = neighbors(adj)
    # print(ns) 
    for n in ns: 
        if n in out_rocks: 
            adjs.append(n)
    # print(adjs)
    # print(f"len adjs: {len(adjs)}") 
    if len(adjs) == 0: 
        break 
     
inner = list(set(out).difference(set(rocks)))

# check if they are connected and then calculate the surface area 
cubes = {rock: 6 for rock in inner}
updated = {}
for cube, dof in cubes.items(): 
    ns = neighbors(cube)
    c = 0 
    for n in ns: 
        if n in cubes:
            c += 1 
    updated[cube] = 6 - c  

dofs_inner = 0 
for cube, dof in updated.items(): 
    dofs_inner += dof 

print(f"Solution Part 2: {dofs - dofs_inner}")
