

def main(): 
    inp = "../inputs/006.txt" 
    with open(inp, 'r') as fp: 
        data = fp.readlines()[0]

    num_markers = 4
    res = 0
    for i in range(len(data) - num_markers):
        markers = data[i:i+num_markers]
        if len(set(markers)) == num_markers: 
            res = i+num_markers
            break 

    print(f"Solution of Part 1: {res}")

    num_markers = 14
    res = 0
    for i in range(len(data) - num_markers):
        markers = data[i:i+num_markers]
        if len(set(markers)) == num_markers: 
            res = i+num_markers
            break 

    print(f"Solution of Part 2: {res}")

if __name__ == "__main__":
    main()