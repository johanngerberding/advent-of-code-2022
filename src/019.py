
# costs: ore [0], clay [1], obsidian [2]
# robots: ore [0], clay[1], obsidian[3], geode [4]
# (type: int, ore: int, clay: int, obsidian: int)
# blueprint: (id, type, ore, clay, obsidian, type, ore, clay, obsidian ...)

# solve this with dynamic programming ??

with open("../inputs/019_test.txt", 'r') as fp:
    bps = fp.readlines()

blueprints = []
for bp in bps:
    bp = bp.strip()
    idx = int(bp[bp.index(' '): bp.index(':')])
    parts = [part for part in bp.split(".") if not part == '']
    els = [idx]
    for part in parts:
        c = [0, 0, 0, 0]
        robots = part.split(" ")
        robot_idx = robots.index("robot") - 1
        robot = robots[robot_idx]
        c[0] = robot
        costs = part[part.index("costs ") + 6:]
        costs = costs.split(" ")
        for i, el in enumerate(costs):
            if el.isnumeric():
                material = costs[i+1]
                if material == 'ore':
                    ore = int(el)
                    c[1] = ore
                elif material == 'clay':
                    clay = int(el)
                    c[2] = clay
                elif material == 'obsidian':
                    obsidian = int(el)
                    c[3] = obsidian

        els += c
    blueprints.append(els)

print(blueprints)