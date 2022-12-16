class CPU: 
    def __init__(self, register: int): 
        self.register = register
        self.cycle = 0
        self.strengths = [] 
    
    def execute(self, inst): 
        if inst == "noop": 
            self.increment_cycle()
        else: 
            self.increment_cycle() 
            self.addx(inst)  

    def addx(self, inst): 
        self.increment_cycle() 
        self.register += int(inst.split(" ")[1])
    
    def increment_cycle(self): 
        self.cycle += 1
        if self.cycle in [20, 60, 100, 140, 180, 220]: 
            self.strengths.append(self.register * self.cycle) 


class CPU2: 
    def __init__(self):
        self.register = 1 
        self.cycle = 0 
        self.pixels = []
        self.row = [] 
    
    def execute(self, inst): 
        if inst == "noop": 
            self.increment_cycle()
        else: 
            self.increment_cycle() 
            self.addx(inst)  

    def addx(self, inst): 
        self.increment_cycle() 
        self.register += int(inst.split(" ")[1])
    
    def increment_cycle(self): 
        if self.in_range(): 
            self.row.append('#')
        else: 
            self.row.append('.') 
        self.cycle += 1
        if self.cycle == 40: 
            self.pixels.append(self.row)
            self.row = []
            self.cycle = 0 
         
    def in_range(self): 
        if self.cycle >= self.register - 1 and self.cycle <= self.register + 1: 
            return True 
        return False 

    def render(self): 
        for row in self.pixels: 
            line = ""
            for p in row: 
                line += p 
            print(line)

def main():
    inp = "../inputs/010.txt" 
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    cpu = CPU(1) 
    
    for inst in data: 
        cpu.execute(inst)  

    print(f"Solution Part 1: {sum(cpu.strengths)}")

    cpu2 = CPU2()

    for inst in data: 
        cpu2.execute(inst)
    
    cpu2.render()



if __name__ == "__main__":
    main()