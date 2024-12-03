
import sys 

data = open(sys.argv[1]).read()

lines = data.split("\n")

grid = [[c for c in line] for line in lines]
grid2 = [[c for c in line] for line in lines]

corners = [(0, 0), (0, len(grid[0])-1), (len(grid)-1, 0), (len(grid)-1, len(grid[0])-1)]
for x, y in corners:
    grid2[y][x] = "#"

steps = 100
nbrs = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]
for i in range(steps):
    new_grid = [[c for c in line] for line in grid]
    new_grid2 = [[c for c in line] for line in grid2]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # if (y, x) in corners:
            #     continue
            if cell == "#":
                new_grid[y][x] = "#" if 2 <= len([1 for on in [0 <= x+dx < len(row) and 0 <= y+dy < len(grid) and grid[y+dy][x+dx] == "#" for dx, dy in nbrs] if on]) <= 3 else "."
                if (y, x) not in corners:
                    # continue
                    new_grid2[y][x] = "#" if 2 <= len([1 for on in [0 <= x+dx < len(row) and 0 <= y+dy < len(grid) and grid2[y+dy][x+dx] == "#" for dx, dy in nbrs] if on]) <= 3 else "."
            else:
                new_grid[y][x] = "#" if len([1 for on in [0 <= x+dx < len(row) and 0 <= y+dy < len(grid) and grid[y+dy][x+dx] == "#" for dx, dy in nbrs] if on]) == 3 else "."
                if (y, x) not in corners:
                    # continue
                    new_grid2[y][x] = "#" if len([1 for on in [0 <= x+dx < len(row) and 0 <= y+dy < len(grid) and grid2[y+dy][x+dx] == "#" for dx, dy in nbrs] if on]) == 3 else "."
    grid = new_grid
    grid2 = new_grid2

print(len([1 for row in grid for c in row if c == "#"]))
print(len([1 for row in grid2 for c in row if c == "#"]))
