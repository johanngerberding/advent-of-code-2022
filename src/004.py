

def main():
    inp = "../inputs/004.txt" 
    
    with open(inp, 'r') as fp: 
        data = fp.readlines()
    
    data = [l.strip() for l in data]
    count = 0 
    for el in data: 
        assignments = el.split(',')
        start1 = int(assignments[0].split('-')[0])
        stop1 = int(assignments[0].split('-')[1])
        start2 = int(assignments[1].split('-')[0])
        stop2 = int(assignments[1].split('-')[1])
        # 1 contains 2 
        if start1 <= start2 and stop1 >= stop2: 
            count += 1 
        # 2 contains 1 
        elif start2 <= start1 and stop2 >= stop1: 
            count += 1
    
    print(f"Solution Part 1: {count}")
    
    count = 0
    for el in data: 
        assignments = el.split(',')
        start1 = int(assignments[0].split('-')[0])
        stop1 = int(assignments[0].split('-')[1])
        start2 = int(assignments[1].split('-')[0])
        stop2 = int(assignments[1].split('-')[1])
        # 1 contains 2 
        if start1 <= stop2 and stop1 >= start2: 
            count += 1 
        elif start2 <= stop1 and stop2 >= start1:
            count += 1 

    print(f"Solution Part 2: {count}")
    


if __name__ == "__main__":
    main()
