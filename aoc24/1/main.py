import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

lefts = []
rights = []

for line in lines:
    vals = line.split(' ')
    left, right = int(vals[0]), int(vals[3])
    lefts.append(left)
    rights.append(right)

sorted_lefts = sorted(lefts)
sorted_rights = sorted(rights)

print(sum(abs(sorted_lefts[i] - sorted_rights[i]) for i in range(len(sorted_lefts))))

ans = 0
for sl in sorted_lefts:
    sl_count = 0
    for sr in sorted_rights:
        if sl == sr:
            sl_count += 1
    ans += sl_count*sl

print(ans)
