
def main(): 
    
    scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    inp = "../inputs/003.txt" 
    with open(inp, 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]
    
    res = 0 
    for el in data: 
        comp1 = set(el[:len(el)//2])
        comp2 = set(el[len(el)//2:])
        inter = comp1.intersection(comp2) 
        assert len(inter) == 1 
        elem = list(inter)[0]
        res += (scores.index(elem) + 1)
    
    print(f"Solution Part 1: {res}")
    
    res = 0 
    for i in range(3, len(data) + 1, 3):
        r1 = set(data[i-3])
        r2 = set(data[i-2])
        r3 = set(data[i-1])
        inter = r1 & r2 & r3 
        assert len(inter) == 1
        elem = list(inter)[0] 
        res += (scores.index(elem) + 1) 
     
    print(f"Solution Part 2: {res}")


if __name__ == "__main__": 
    main()
