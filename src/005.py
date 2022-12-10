

def main(): 
    inp = "../inputs/005.txt" 
    with open(inp, 'r') as fp: 
        data = [el.rstrip('\n') for el in fp.readlines()]

    sep = data.index('')

    stacks_data = data[:sep]
    instructions_set = data[sep + 1:]
    num_stacks = int(stacks_data[-1].strip()[-1]) 
    stacks_data = stacks_data[:-1] 
    stacks = [[] for _ in range(num_stacks)]
    idxs = [i for i in range(1, len(stacks_data[0]), 4)] 
    
    for data in stacks_data:
        for i, idx in enumerate(idxs):
            el = data[idx]
            if el != ' ':
                stacks[i].append(el)

    for stack in stacks:
        stack.reverse() 

    instructions = [[] for _ in instructions_set]
    for i, instruct in enumerate(instructions_set): 
        insts = instruct.split(' ') 
        for w in insts: 
            if w.isnumeric(): 
                instructions[i].append(int(w))

    for i, inst in enumerate(instructions): 
        number_moves = inst[0]
        from_stack = inst[1] - 1
        to_stack = inst[2] - 1
        for _ in range(number_moves):
            if len(stacks[from_stack]) > 0:  
                el = stacks[from_stack].pop()
                stacks[to_stack].append(el)

    res = ""
    for stack in stacks:
        if len(stack) > 0:  
            res += str(stack[-1])
        else: 
            res += " "
    
    print(f"Solution Part 1: {res}")
    stacks = [[] for _ in range(num_stacks)]
    for data in stacks_data:
        for i, idx in enumerate(idxs):
            el = data[idx]
            if el != ' ':
                stacks[i].append(el)

    for stack in stacks:
        stack.reverse() 

    for i, inst in enumerate(instructions): 
        number_moves = inst[0]
        from_stack = inst[1] - 1
        to_stack = inst[2] - 1

        els = stacks[from_stack][-number_moves:] 
        stacks[from_stack] = stacks[from_stack][:-number_moves]
        stacks[to_stack] += els
        
    res = ""
    for stack in stacks:
        if len(stack) > 0:  
            res += str(stack[-1])
        else: 
            res += " "
    
    print(f"Solution Part 2: {res}")

if __name__ == "__main__":
    main()