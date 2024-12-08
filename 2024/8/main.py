import sys
from collections import defaultdict
from itertools import combinations

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

grid = [list(line) for line in lines]


freqs = defaultdict(list)
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != '.':
            freqs[cell].append((y, x))


def in_bounds(y, x):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def get_obstacles(y1, x1, y2, x2, dy, dx):
    return y1-dy, x1-dx, y2+dy, x2+dx


def add_obstacles(seen, y1, x1, y2, x2):
    if in_bounds(y1, x1):
        seen.add((y1, x1))
    if in_bounds(y2, x2):
        seen.add((y2, x2))


seen1 = set()
seen2 = set()
for freq, coords in freqs.items():
    pairs = list(combinations(coords, 2))
    for (y1, x1), (y2, x2) in pairs:
        dy, dx = y2 - y1, x2 - x1
        oy1, ox1, oy2, ox2 = get_obstacles(y1, x1, y2, x2, dy, dx)
        add_obstacles(seen1, oy1, ox1, oy2, ox2)

        add_obstacles(seen2, y1, x1, y2, x2)
        dy, dx = y2 - y1, x2 - x1
        oy1, ox1, oy2, ox2 = get_obstacles(y1, x1, y2, x2, dy, dx)
        while in_bounds(oy1, ox1) or in_bounds(oy2, ox2):
            add_obstacles(seen2, oy1, ox1, oy2, ox2)
            oy1, ox1, oy2, ox2 = get_obstacles(oy1, ox1, oy2, ox2, dy, dx)

print(len(seen1))
print(len(seen2))
