import itertools
import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')


def check_equations(target, nums, ops):
    op_ords = itertools.product(ops, repeat=len(nums) - 1)
    for op_ord in op_ords:
        val = nums[0]
        for i, op in enumerate(op_ord):
            match op:
                case 0: val += nums[i + 1]
                case 1: val *= nums[i + 1]
                case 2: val = int(str(val) + str(nums[i + 1]))
        if val == target:
            return val
    return 0


ans = 0
ans2 = 0

for line in lines:
    parts = line.split(": ")
    target = int(parts[0])
    nums = [int(n) for n in parts[1].split()]
    ans += check_equations(target, nums, [0, 1])
    ans2 += check_equations(target, nums, [0, 1, 2])

print(ans)
print(ans2)
