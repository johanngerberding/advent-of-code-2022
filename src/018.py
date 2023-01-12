
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
for el in data: 
    cube = (int(el[0]), int(el[1]), int(el[2])) 
    cubes[cube] = 6 

print(cubes)

updated = {}
for cube, dof in cubes.items(): 
    ns = neighbors(cube)
    print(f"ns: {ns}")
    c = 0 
    for n in ns: 
        if n in cubes:
            print(f"n in cubes: {n}") 
            c += 1 
    updated[cube] = 6 - c  

dofs = 0 
for cube, dof in updated.items(): 
    dofs += dof 

print(dofs)
# if you add a new cube you have to check for all 6 possible neighbors 