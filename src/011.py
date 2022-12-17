#!/usr/bin/env python3
from math import trunc 
import tqdm 


class Monkey: 
    def __init__(self): 
        self.items = None 
        self.op = None 
        self.div = None 
        self.true_monkey = None 
        self.false_monkey = None
        self.num_inspects = 0

    def parse(self, info: list): 
        items = info[1][16:].split(',')
        self.items = [int(el.strip()) for el in items]
        self.op = info[2].split(' ')[-2:] 
        self.div = int(info[3].split(' ')[-1]) 
        self.true_monkey = int(info[4].split(' ')[-1]) 
        self.false_monkey = int(info[5].split(' ')[-1])

    def turn(self):
        out = [] 
        for item in self.items:
            self.num_inspects += 1  
            if self.op[0] == '*':
                if self.op[1] == 'old': 
                    wl = item * item 
                else:  
                    wl = item * int(self.op[1])
            elif self.op[0] == '+':
                if self.op[1] == 'old': 
                    wl = item + item 
                else:  
                    wl = item + int(self.op[1]) 
            wl = trunc(wl / 3) 
            if wl % self.div == 0: 
                out.append((self.true_monkey, wl)) 
            else: 
                out.append((self.false_monkey, wl))
        self.items = []
        return out

    def turn2(self):
        out = [] 
        for item in self.items:
            self.num_inspects += 1  
            if self.op[0] == '*':
                wl = item 
                """ 
                if self.op[1] == 'old': 
                    wl = item * item 
                else:  
                    wl = item * int(self.op[1])
                """ 
            elif self.op[0] == '+':
                wl = item + int(self.op[1]) 
            # wl = trunc(wl / 3) 
            if wl % self.div == 0: 
                out.append((self.true_monkey, wl)) 
            else: 
                out.append((self.false_monkey, wl))
        self.items = []
        return out


def main(): 
    inp = "../inputs/011_test.txt"
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]
    """
    monkeys = []
    m = [] 
    for el in data: 
        if el == '': 
            monkeys.append(m) 
            m = [] 
        else: 
            m.append(el)
    monkeys.append(m)

    monks = []
    for monkey in monkeys: 
        m = Monkey() 
        m.parse(monkey)
        monks.append(m)
    
    for i in range(20): 
        print(f"Round {i}")
        for idx, monk in enumerate(monks): 
            print(f"Monkey {idx}: {monk.items}") 
        for monk in monks: 
            moves = monk.turn()
            for mv in moves: 
                monks[mv[0]].items.append(mv[1])

    inspects = []
    for i, monk in enumerate(monks): 
        print(f"Monkey {i}: {monk.num_inspects}")
        inspects.append(monk.num_inspects)

    inspects.sort() 
    result = inspects[-1] * inspects[-2]
    print(f"Solution Part 1: {result}")
    """ 
    monkeys = []
    m = [] 
    for el in data: 
        if el == '': 
            monkeys.append(m) 
            m = [] 
        else: 
            m.append(el)
    monkeys.append(m)

    monks = []
    for monkey in monkeys: 
        m = Monkey() 
        m.parse(monkey)
        monks.append(m)
    
    for i in tqdm.tqdm(range(10000)): 
        # print(f"Round {i}")
        # for idx, monk in enumerate(monks): 
            # print(f"Monkey {idx}: {monk.items}") 
        for monk in monks: 
            moves = monk.turn2()
            for mv in moves: 
                monks[mv[0]].items.append(mv[1])

    inspects = []
    for i, monk in enumerate(monks): 
        print(f"Monkey {i}: {monk.num_inspects}")
        inspects.append(monk.num_inspects)

    inspects.sort() 
    result = inspects[-1] * inspects[-2]
    print(f"Solution Part 2: {result}")


if __name__ == "__main__":
    main()