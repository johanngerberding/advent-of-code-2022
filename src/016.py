from collections import deque


class PressureMonitor: 
    def __init__(self):
        self.pressure = 0 
        self.time = 0
        self.history = [0] 
    
    def update(self): 
        self.history.append(self.pressure)


class Valve:
    def __init__(self, name: str, flow_rate: int, connections: list, pm: PressureMonitor): 
        self.name = name  
        self.flow_rate = flow_rate
        self.adjs = connections
        self.pm = pm
        self.open = False
        self.travel_count = 0  

    def __str__(self): 
        return f"Valve {self.name} | Flow rate: {self.flow_rate} | Connections: {self.adjs}"
    
    def opening(self):
        self.travel_count += 1 
        if not self.open: 
            self.pm.time += 1 
            self.open = True 
            print(f"Mins: {self.pm.time} | Opening valve {self.name} | pressure: {self.pm.pressure}") 
            self.pm.pressure += self.flow_rate 
            self.pm.update()


def get_next(valves: dict, valve: str) -> str: 
    """Return next non opened adjacent valve. 
    If all are open, return the one with the minimum visits""" 
    adjs = valves[valve].adjs   
    for adj in adjs: 
        if not valves[adj].open:
            return adj

    tcounts = [adj.travel_count for adj in adjs]
    min_count = min(tcounts)

    return adjs[tcounts.index(min_count)]



def dfs(valves: dict, root: str, visited: set, mins: int): 
    valve = valves[root] 
    visited.add(valve.name)
    valve.pm.time += 1
    valve.pm.update()
    print(f"Mins: {valve.pm.time} | Moving to valve {valve.name} | pressure: {valve.pm.pressure}") 
    if valve.pm.time >= mins: 
        return  
    valve.opening()
    if valve.pm.time >= mins: 
        return
    for adj in valve.adjs: 
        if adj not in visited: 
            dfs(valves, adj, visited, mins) 


def parse(line: str): 
    line = line.split(";") 
    name = line[0].split(" ")[1]
    rate = int(line[0].split(" ")[-1].split("=")[1])
    if "valves" in line[1]: 
        adjs = [el.strip() for el in line[1].split("valves")[1].split(",")]
    elif "valve" in line[1]: 
        adjs = [line[1].split("valve")[1].strip()]
    return name, Valve(name, rate, adjs, pm)

with open("../inputs/016_test.txt", 'r') as fp: 
    data = [el.strip() for el in fp.readlines()]

pm = PressureMonitor()

valves = {} 
for line in data: 
    name, valve = parse(line)
    valves[name] = valve 

for valve in valves.values(): 
    print(valve)

mins = 30 
root = "AA"
visited = set()

dfs(valves, root, visited, mins) 