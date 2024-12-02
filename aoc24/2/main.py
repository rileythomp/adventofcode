import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

ans = 0
for line in lines:
    nums = [int(n) for n in line.split()]
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        broke = False
        for i in range(1, len(nums)):
            if not (3 >= abs(nums[i] - nums[i-1]) >= 1):
                broke = True
                break
        if not broke:
            ans += 1

print(ans)


ans = 0
for line in lines:
    nums = [int(n) for n in line.split()]
    can_be_made_safe = False
    for i, num in enumerate(nums):
        new_nums = nums[:i] + nums[i+1:]
        if new_nums == sorted(new_nums) or new_nums == sorted(new_nums, reverse=True):
            broke = False
            for j in range(1, len(new_nums)):
                if not (3 >= abs(new_nums[j] - new_nums[j-1]) >= 1):
                    broke = True
                    break
            if not broke:
                can_be_made_safe = True
                break
    if can_be_made_safe:
        ans += 1
print(ans)
