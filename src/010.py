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

def main():
    inp = "../inputs/010.txt" 
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    cpu = CPU(1) 
    
    for inst in data: 
        cpu.execute(inst)  

    print(f"Solution Part 1: {sum(cpu.strengths)}")



if __name__ == "__main__":
    main()