

class PressureMonitor: 
    def __init__(self):
        self.pressure = 0 
        self.time = 0 


class Valve:
    def __init__(self, name: str, flow_rate: int, connections: list, pm: PressureMonitor): 
        self.name = name  
        self.flow_rate = flow_rate
        self.adjs = connections
        self.pm = pm

    def __str__(self): 
        return f"Valve {self.name} | Flow rate: {self.flow_rate} | Connections: {self.adjs}"

def parse(line: str): 
    line = line.split(";") 
    name = line[0].split(" ")[1]
    rate = int(line[0].split(" ")[-1].split("=")[1])
    if "valves" in line[1]: 
        adjs = [el.strip() for el in line[1].split("valves")[1].split(",")]
    elif "valve" in line[1]: 
        adjs = [line[1].split("valve")[1].strip()]
    return Valve(name, rate, adjs, pm)

with open("../inputs/016.txt", 'r') as fp: 
    data = [el.strip() for el in fp.readlines()]

pm = PressureMonitor()

valves = []
for line in data: 
    valves.append(parse(line))

for valve in valves: 
    print(valve)

# exhaustive search, check all possible ways for 30 mins 