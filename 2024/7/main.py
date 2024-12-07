import itertools
import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

ans = 0
ans2 = 0

for line in lines:
    parts = line.split(": ")
    target = int(parts[0])
    nums = [int(n) for n in parts[1].split()]
    num_ops = len(nums) - 1
    op_ords = itertools.product([0, 1], repeat=num_ops)
    for op_ord in op_ords:
        val = nums[0]
        for i, op in enumerate(op_ord):
            match op:
                case 0: val += nums[i + 1]
                case 1: val *= nums[i + 1]
        if val == target:
            ans += val
            break
    op_ords2 = itertools.product([0, 1, 2], repeat=num_ops)
    for op_ord in op_ords2:
        val = nums[0]
        for i, op in enumerate(op_ord):
            match op:
                case 0: val += nums[i + 1]
                case 1: val *= nums[i + 1]
                case 2: val = int(str(val) + str(nums[i + 1]))
        if val == target:
            ans2 += val
            break
print(ans)
print(ans2)
