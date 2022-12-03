# 0 when lost, 3 when draw, 6 when win 
# 1 for A/X 
# 2 for B/Y 
# 3 for C/Z 

def result(match: str): 
    if match[0] == 'A': 
        if match[2] == 'X':
            return 3 
        if match[2] == 'Y': 
            return 6
        else: 
            return 0 
    elif match[0] == 'B': 
        if match[2] == 'X':
            return 0 
        if match[2] == 'Y': 
            return 3
        else: 
            return 6
    elif match[0] == 'C': 
        if match[2] == 'X':
            return 6 
        if match[2] == 'Y': 
            return 0
        else: 
            return 3

def get_move(match: str): 
    if match[0] == 'A': 
        if match[2] == 'X':
            return 3 
        if match[2] == 'Y': 
            return 1
        else: 
            return 2 
    elif match[0] == 'B': 
        if match[2] == 'X':
            return 1 
        if match[2] == 'Y': 
            return 2
        else: 
            return 3
    elif match[0] == 'C': 
        if match[2] == 'X':
            return 2 
        if match[2] == 'Y': 
            return 3
        else: 
            return 1


def main(): 
    inp = "../inputs/002.txt"
    with open(inp, 'r') as fp: 
        data = fp.readlines()

    data = [el.strip() for el in data]
    
    score = 0 

    for game in data: 
        res = result(game) 
        if game[2] == 'X': 
            res += 1 
        elif game[2] == 'Y': 
            res += 2 
        elif game[2] == 'Z': 
            res += 3 
        score += res 

    print(f"Solution Part 1: {score}")
    
    score = 0 
    for game in data: 
        move = get_move(game)
        if game[2] == 'X': 
            move += 0 
        elif game[2] == 'Y': 
            move += 3 
        elif game[2] == 'Z': 
            move += 6 
        score += move 
    
    print(f"Solution Part 2: {score}")


if __name__ == "__main__":
    main()
