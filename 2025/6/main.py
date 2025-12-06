from collections import defaultdict


def calc_nums(col, op):
    if op == '+':
        return sum(col)
    prod = 1
    for v in col:
        prod *= v
    return prod

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    vals = defaultdict(list)
    for i in range(len(lines)-1):
        line = lines[i]
        nums = [int(x) for x in line.split()]
        for j in range(len(nums)):
            vals[j].append(nums[j])
    ops = lines[-1].split()
    ans = 0
    for i in range(len(ops)):
        ans += calc_nums(vals[i], ops[i])
    print(ans)

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    nums = []
    cur_op = ''
    max_len = max(len(line) for line in lines)
    ans = 0
    for x in range(max_len):
        cur_num = 0
        for y in range(len(lines)):
            if x < len(lines[y]):
                if lines[y][x] in '+*':
                    cur_op = lines[y][x]
                elif lines[y][x] == ' ':
                    pass
                else:
                    cur_num *= 10
                    cur_num += int(lines[y][x])
        if cur_num != 0:
            nums.append(cur_num)
        else:
            ans += calc_nums(nums, cur_op)
            nums = []
    ans += calc_nums(nums, cur_op)
    print(ans)
