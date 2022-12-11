class CPU: 
    def __init__(self, register: int): 
        self.register = register
        self.cycle = 0 
    
    def execute(self, inst): 
        if inst == "noop": 
            self.cycle += 1 
        else: 
            self.cycle += 1 
            self.addx(inst)  

    def addx(self, inst): 
        self.cycle += 1 
        self.register += int(inst.split(" ")[1])

def main():
    inp = "../inputs/010.txt" 
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    register = 1 
    cycle = 0 

    
    strength = [] 
    
    for inst in data: 
        if inst == "noop": 
            cycle += 1  
        else:
            ins = inst.split(" ")[0]
            val = int(inst.split(" ")[1])
            cycle += 1
                
            cycle += 1 
            register += val  




if __name__ == "__main__":
    main()