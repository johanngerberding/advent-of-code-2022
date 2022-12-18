

def main(): 
    with open("../inputs/013.txt", 'r') as fp: 
        data = [el.strip() for el in fp.readlines()]

    pairs = []
    pair = [] 
    for el in data: 
        if el == '':
            pairs.append(pair) 
            pair = []
        else: 
            pair.append(el)

    for p in pairs: 
        print(p)


if __name__ == "__main__":
    main()