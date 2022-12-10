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


def main():
    test = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]

    visible = 2 * len(test) + 2 * (len(test[0]) - 2) 
    for row in range(1, len(test) - 1): 
        for col in range(1, len(test[row]) - 1):  
            vis = check(test, row, col)   
            visible += vis
    
    print(f"Solution Test: {visible}")
    
    inp = "../inputs/008.txt" 
    with open(inp, 'r') as fp: 
        rows = [el.strip() for el in fp.readlines()]

    visible = 2 * len(rows) + 2 * (len(rows[0]) - 2) 
    
    for row in range(1, len(rows) - 1): 
        for col in range(1, len(rows[row]) - 1):  
            vis = check(rows, row, col)   
            visible += vis

    print(f"Solution Part 1: {visible}")


if __name__ == "__main__":
    main()