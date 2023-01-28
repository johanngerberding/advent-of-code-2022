from queue import Queue
import numpy as np

# My notes on this:
# costs: ore [0], clay [1], obsidian [2]
# robots: ore [0], clay[1], obsidian[3], geode [4]
# (type: int, ore: int, clay: int, obsidian: int)
# blueprint: (id, type, ore, clay, obsidian, type, ore, clay, obsidian ...)

# solve this with dynamic programming ??

# sequence of 24 steps
# build up a tree of all possible actions

# inventory of materials
# based on inventory you have different possibilities of how to behave
# possible_actions(inventory) -> what can be done
# my brute force solution didn't work (to slow)
# Solution from here:
# https://github.com/marcodelmastro/AdventOfCode2022/blob/main/Day19.ipynb


def parse(bps: list) -> list:
    blueprints = []
    for bp in bps:
        bp = bp.strip()
        parts = [part for part in bp.split(".") if not part == '']
        els = []
        for part in parts:
            c = [0, 0, 0, 0]
            costs = part[part.index("costs ") + 6:]
            costs = costs.split(" ")
            for i, el in enumerate(costs):
                if el.isnumeric():
                    material = costs[i+1]
                    if material == 'ore':
                        ore = int(el)
                        c[0] = int(ore)
                    elif material == 'clay':
                        clay = int(el)
                        c[1] = int(clay)
                    elif material == 'obsidian':
                        obsidian = int(el)
                        c[2] = int(obsidian)

            els.append(np.array(c))
        blueprints.append(els)
    return blueprints


def hash_state(state: tuple) -> str:
    time, robots, materials = state
    h = str(time) + "_"
    for r in robots:
        h += "_" + str(r)
    h += "_"
    for m in materials:
        h += "_" + str(m)
    return h

def get_max_geodes(bp, timemax=24):
    max_res = np.array([0, 0, 0, 0])
    # compute the maximum amount needed of each resource to build any robot
    for cost in bp:
        for i in range(len(cost)):
            if cost[i] > max_res[i]:
                max_res[i] = cost[i]

    # initial state
    robots = np.array([1, 0, 0, 0])
    materials = np.array([0, 0, 0, 0])
    time = 0
    start = (time, robots, materials)

    # bfs search of state evolutions
    states = {hash_state(start)}
    geodes_max = 0
    q = Queue()
    q.put(start)

    while not q.empty():
        # get state
        time, robots, materials = q.get()

        # compute geodes from current state at end time
        geodes_state = materials[3] + robots[3] * (timemax - time)
        if geodes_state > geodes_max:
            geodes_max = geodes_state

        for i in range(len(bp)):
            cost = bp[i]
            time_needed = [0, 0, 0, 0]

            for j in range(len(cost)):
                if cost[j]:
                    if cost[j] <= materials[j]:
                        continue
                    else:
                        if robots[j]:
                            time_needed[j] = (cost[j] - materials[j]) // robots[j] + int((cost[j] - materials[j]) % robots[j] > 0)
                        else:
                            time_needed[j] = timemax + 1

            dt = max(time_needed)
            if time + dt + 1 + 1 <= timemax:
                materials_new = materials + (dt + 1) * robots - cost
                robots_new = np.copy(robots)
                robots_new[i] += 1

                if not (robots_new <= max_res)[:3].all():
                    continue
                time_left = timemax - (time + dt + 1)
                geodes_new_ideal = (time_left - 1) * time_left // 2

                geodes_final_ideal = materials_new[3] + time_left * robots_new[3] + geodes_new_ideal
                if geodes_final_ideal <= geodes_max:
                    continue

                state_new = (time + dt + 1, robots_new, materials_new)
                h = hash_state(state_new)
                if h not in states:
                    q.put(state_new)
                    states.add(h)

    return geodes_max


with open("../inputs/019.txt", 'r') as fp:
    bps = fp.readlines()

blueprints = parse(bps)
print(blueprints)

# Part 1
q = 0
print("| Blueprint | Geodes (24) | Quality |")
print("|-----------+-------------+---------|")
for i,bp in enumerate(blueprints):
    g = get_max_geodes(bp,24)
    print("| {:9d} | {:11d} | {:7d} | ".format(i+1,g,(i+1)*g))
    q += (i+1)*g
print("\n Sum quality levels: {}".format(q))


p = 1
print("| Blueprint | Geodes (32) |")
print("|-----------+-------------|")
for i,bp in enumerate(blueprints):
    g = get_max_geodes(bp,32)
    print("| {:9d} | {:11d} | ".format(i+1,g))
    p *= g
    if i+1==3:
        break
print("\n Product of max geodes: {}".format(p))
