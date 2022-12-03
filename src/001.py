

def main(): 
    inp = "../inputs/001.txt" 
    calories = [] 
    with open(inp, 'r') as fp: 
        data = fp.readlines() 
    data = [el.strip() for el in data] 
    s = 0  
    for el in data: 
        if el.isnumeric(): 
            s += int(el) 
        else: 
            calories.append(s)
            s = 0 
    
    print(f"Solution Part 1: {max(calories)}") 
    calories.sort() 
    print(f"Solution Part 2: {sum(calories[-3:])}")


if __name__ == "__main__":
    main()
