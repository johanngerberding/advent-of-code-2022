import numpy as np 


def check(rows: list, row: int, col: int): 
    height = int(rows[row][col])
    count = 0 
    # left
    left = np.array([int(c) for c in rows[row][:col]])
    left_vis = height <= left
    s = np.sum(left_vis)
    if np.sum(left_vis) == 0: 
        count += 1  
    # right 
    right = np.array([int(c) for c in rows[row][col + 1:]]) 
    right_vis = height <= right
    s = np.sum(right_vis)
    if np.sum(right_vis) == 0: 
        count += 1
    # top 
    top = np.array([int(rows[i][col]) for i in range(row)]) 
    if np.sum(height <= top) == 0: 
        count += 1
    # down
    down = np.array([int(rows[i][col]) for i in range(row + 1, len(rows))]) 
    if np.sum(height <= down) == 0: 
        count += 1

    if count > 0:
        return 1  
    return 0 


def get_score(side): 
    score = 0 
    for el in side: 
        if el:
            score += 1 
        else: 
            score += 1 
            return score  
    return score 


def scenic_score(rows: list, row: int, col: int): 
    height = int(rows[row][col])
    left = np.array([int(c) for c in rows[row][:col]])
    left_vis = height > left 
    left_vis = left_vis[::-1] 
    left_score = get_score(left_vis) 
    right = np.array([int(c) for c in rows[row][col + 1:]]) 
    right_vis = height > right
    right_score = get_score(right_vis) 
    top = np.array([int(rows[i][col]) for i in range(row)]) 
    top_vis = height > top 
    top_vis = top_vis[::-1]
    top_score = get_score(top_vis) 
    down = np.array([int(rows[i][col]) for i in range(row + 1, len(rows))]) 
    down_vis = height > down
    down_score = get_score(down_vis)

    res = left_score * right_score * top_score * down_score 
    # print(f"height: {height} | left: {left_score} | right: {right_score} | top: {top_score} | down: {down_score} = {res}")
    return res 


def main():
    test = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]
    scenic_scores = []
    visible = 2 * len(test) + 2 * (len(test[0]) - 2) 
    for row in range(1, len(test) - 1): 
        for col in range(1, len(test[row]) - 1):  
            vis = check(test, row, col) 
            scenic_scores.append(scenic_score(test, row, col))  
            visible += vis
    
    print(f"Solution Test Part 1: {visible}")
    print(f"Soltiuon Test Part 2: {max(scenic_scores)}") 
    
    inp = "../inputs/008.txt" 
    with open(inp, 'r') as fp: 
        rows = [el.strip() for el in fp.readlines()]

    scenic_scores = []
    visible = 2 * len(rows) + 2 * (len(rows[0]) - 2) 
    
    for row in range(1, len(rows) - 1): 
        for col in range(1, len(rows[row]) - 1):  
            scenic_scores.append(scenic_score(rows, row, col)) 
            vis = check(rows, row, col)   
            visible += vis

    print(f"Solution Part 1: {visible}")
    print(f"Solution Part 2: {max(scenic_scores)}")

if __name__ == "__main__":
    main()