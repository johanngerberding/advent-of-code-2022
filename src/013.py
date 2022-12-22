from functools import cmp_to_key


def compare(a, b): 
    if type(a) == int: 
        if type(b) == int: 
            return (a > b) - (a < b)
        return compare([a], b)
    if type(b) == int: 
        return compare(a, [b])
    for aa, bb in zip(a, b): 
        if r := compare(aa, bb):
            return r 
    return compare(len(a), len(b))


with open("../inputs/013.txt", 'r') as fp: 
    inp = fp.read()
    part1, part2 = 0, 1 

    for i, pairs in enumerate(inp.split("\n\n")):
        left, right = map(eval, pairs.splitlines())
        if compare(left, right) == -1: 
            part1 += i + 1

    print(f"Solution Part 1: {part1}")

    pairs = [eval(p) for p in inp.splitlines() if p]
    pairs.append([[2]])
    pairs.append([[6]])
    pairs.sort(key=cmp_to_key(compare))

    for i, pair in enumerate(pairs): 
        if pair == [[2]]: 
            part2 *= i + 1
        if pair == [[6]]:
            part2 *= i + 1 
    
    print(f"Solution Part 2: {part2}")