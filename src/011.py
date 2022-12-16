#!/usr/bin/env python3

def parse(monkey: list): 
    items = monkey[1][16:].split(',')
    items = [int(el.strip()) for el in items]
    op = monkey[2].split(' ')[-2:] 
    divider = int(monkey[3].split(' ')[-1]) 
    true_monkey = int(monkey[4].split(' ')[-1]) 
    false_monkey = int(monkey[4].split(' ')[-1]) 
    print(items)
    print(op)
    print(divider)



def main(): 
    inp = "../inputs/011.txt"
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    monkeys = []
    m = [] 
    for el in data: 
        if el == '': 
            monkeys.append(m) 
            m = [] 
        else: 
            m.append(el)
    monkeys.append(m)

    for monkey in monkeys: 
        parse(monkey)

if __name__ == "__main__":
    main()