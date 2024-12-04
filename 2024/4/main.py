import sys

data = open(sys.argv[1]).read().strip()

lines = data.split("\n")

grid = [[c for c in line] for line in lines]

xmas = ['X', 'M', 'A', 'S']
samx = xmas[::-1]

ans = 0
ans2 = 0

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if x + 3 < len(row) and \
                [grid[y][x+i] for i in range(4)] in (xmas, samx):
            ans += 1
        if y + 3 < len(grid) and \
                [grid[y+i][x] for i in range(4)] in (xmas, samx):
            ans += 1
        if x + 3 < len(row) and y + 3 < len(grid) and \
                [grid[y+i][x+i] for i in range(4)] in (xmas, samx):
            ans += 1
        if x + 3 < len(row) and y >= 3 and \
                [grid[y-i][x+i] for i in range(4)] in (xmas, samx):
            ans += 1
        if x > 0 and x < len(row)-1 and \
                y > 0 and y < len(grid)-1 and \
                grid[y][x] == 'A' and \
                grid[y-1][x-1]+grid[y+1][x+1] in ('SM', 'MS') and \
                grid[y-1][x+1]+grid[y+1][x-1] in ('SM', 'MS'):
            ans2 += 1

print(ans)
print(ans2)
