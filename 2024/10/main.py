import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

grid = [[int(n) for n in line] for line in lines]
ans = 0
ans2 = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != 0:
            continue
        queue = [(cell, (y, x))]
        seen = set()
        while queue:
            val, (cury, curx) = queue.pop(0)
            if val == 9:
                if (cury, curx) not in seen:
                    ans += 1
                    seen.add((cury, curx))
                ans2 += 1
                continue
            nbrs = [(cury, curx-1), (cury, curx+1), (cury-1, curx), (cury+1, curx)]
            for ny, nx in nbrs:
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                    if val + 1 == grid[ny][nx]:
                        queue.append((val + 1, (ny, nx)))

print(ans)
print(ans2)
