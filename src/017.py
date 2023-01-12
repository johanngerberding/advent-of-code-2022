import tqdm 

class Instructions:
    def __init__(self, insts: str): 
        self.instructions = insts 
        self.idx = 0
        self.rounds = 0 

    def get_curr(self): 
        return self.instructions[self.idx] 

    def get_next(self):
        if self.idx == len(self.instructions): 
            self.idx = 0 
            self.rounds += 1 
        res = self.instructions[self.idx]
        self.idx += 1 
        return res 

class Chamber:
    def __init__(self): 
        self.width = 7 
        self.height = 0
        self.idx = 0 
        self.occupied = set() 
        self.curr = None 

    def get_idx(self):
        if self.idx == 5:
            self.idx = 0  
        res = self.idx 
        self.idx += 1 
        return res

    def set_figure(self):
        max_occ = max(self.occupied) if len(self.occupied) > 0 else -1 
        self.curr = Figure(self.get_idx(), ((max_occ // 7) + 4) * 7) 
    
    def down(self):
        fut = [el - 7 for el in self.curr.figure] 
        # check for collisions 
        for el in fut: 
            if el in self.occupied: 
                for num in self.curr.figure: 
                    self.occupied.add(num) 
                self.curr = None 
                return False  
        # check for negative values 
        for el in fut: 
            if el < 0:
                for num in self.curr.figure: 
                    self.occupied.add(num)
                self.curr = None  
                return False     
        self.curr.figure = fut 
        return True 

    def right(self):
        for el in self.curr.figure: 
            if el % 7 == 6:
                return False 
        fut = [el + 1 for el in self.curr.figure] 
        for el in fut: 
            if el in self.occupied:
                return False 
        self.curr.figure = fut
        return True 

    def left(self): 
        for el in self.curr.figure: 
            if el % 7 == 0:
                return False  
        fut = [el - 1 for el in self.curr.figure]
        for el in fut: 
            if el in self.occupied:
                return False
        self.curr.figure = fut 
        return True 


class Figure: 
    figures = [
        [2, 3, 4, 5], 
        [3, 9, 10, 11, 17], 
        [2, 3, 4, 11, 18], 
        [2, 9, 16, 23], 
        [2, 3, 9, 10],
    ]

    def __init__(self, idx, row):
        self.row = row 
        self.figure = [row + el for el in self.figures[idx]]


def get_tdv(chamber, instructions):
    height = max(chamber.occupied) // 7 + 4
    upper_row = [height * 7 + i for i in range(7)]
    elems = []
    for upper in upper_row: 
        c = 0
        bound = upper 
        while True:
            c -= 1  
            nelem = bound - 7 
            if nelem in chamber.occupied or nelem < 0: 
                elems.append(c)
                break  
            bound = nelem 
    
    elems += [chamber.idx] 
    ninst = instructions.idx
    elems += [ninst]
    return tuple(elems)



def main(): 
    with open("../inputs/017.txt", 'r') as fp: 
        insts = fp.readline()

    instructions = Instructions(insts)
    chamber = Chamber() 

    topdown = {}
    rocks_height = {} 
    first = True 

    for i in tqdm.tqdm(range(10000)): 
        chamber.set_figure()
        # safe top down view
        if not first:  
            td = get_tdv(chamber, instructions)
            if not td in topdown: 
                topdown[td] = (i, max(chamber.occupied) // 7 + 1)
                rocks_height[i] =  max(chamber.occupied) // 7 + 1
            else:
                rocks = topdown[td][1]
                cycles = (1_000_000_000_000 - topdown[td][0]) 
                reps = int(cycles / (i - topdown[td][0])) 
                rocks += (reps * ((max(chamber.occupied) // 7 + 1) - topdown[td][1])) 
                mod = cycles % (i - topdown[td][0])
                h = rocks_height[mod + topdown[td][0]] 
                h -= topdown[td][1]
                rocks += h 
                print(f"Solution Part 2: {rocks}")
                return 
        first = False  
        while chamber.curr: 
            inst = instructions.get_next()
            if inst == '>': 
                chamber.right()
            elif inst == '<': 
                chamber.left() 
            
            chamber.down()

    print(max(chamber.occupied) // 7 + 1)


if __name__ == "__main__":
    main()  