import copy

with open("../inputs/020.txt", 'r') as fp:
    nums = fp.readlines()

nums = [int(n) for n in nums]
sequence = copy.deepcopy(nums)

# print(nums)
for el in sequence:
    # print("-" * 20)
    # print(f"num: {el}")
    pos = nums.index(el)
    # print(f"pos: {pos}")
    new_pos = pos + el
    if new_pos <= 0:
        new_pos = len(nums) - abs(new_pos) - 1
    elif new_pos >= len(nums):
        new_pos = new_pos - len(nums) + 1
    # print(f"new pos: {new_pos}")
    nums.pop(pos)
    nums.insert(new_pos, el)
    # print(nums)

zero = nums.index(0)
print(f"Zero index: {zero}")
res = []
for el in [1000, 2000, 3000]:
    if len(nums) < el:
        rest = el % len(nums)
    else:
        rest = el
    idx = zero + rest
    if idx >= len(nums):
        nidx = idx - len(nums)
    else:
        nidx = idx
    print(f"{str(el)}th: index: {nidx} - number: {nums[nidx]}")
    res.append(nums[nidx])

print(f"Solution Part 1: {sum(res)}")
