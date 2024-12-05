import sys
from collections import defaultdict

data = open(sys.argv[1]).read().strip()

lines = data.split("\n")

chunks = data.split("\n\n")

orders = chunks[0].split("\n")

updates = chunks[1].split("\n")

followers = defaultdict(list)
for order in orders:
    n1, n2 = order.split("|")
    followers[int(n1)].append(int(n2))

def ordered(nums):
    seen = {}
    for num in nums:
        seen[num] = True
        follows = followers[num]
        for follow in follows:
            if follow in seen:
                return False
    return True


def reorder(nums):
    while not ordered(nums):
        i = 0
        seen = {}
        while i < len(nums):
            num = nums[i]
            seen[num] = i
            follows = followers[num]
            for follow in follows:
                if follow in seen and seen[follow] < seen[num]:
                    num_at, follow_at = seen[num], seen[follow]
                    nums[num_at], nums[follow_at] = nums[follow_at], nums[num_at]
                    seen[follow], seen[num] = num_at, follow_at
            i += 1
    return nums


ans = 0
ans2 = 0
for update in updates:
    nums = [int(x) for x in update.split(",")]
    if ordered(nums):
        ans += nums[len(nums)//2]
    else:
        nums = reorder(nums)
        ans2 += nums[len(nums)//2]

print(ans)
print(ans2)
