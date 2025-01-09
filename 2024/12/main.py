import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

grid = [list(line) for line in lines]

seen = set()
regions = []

nbrs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if (y, x) in seen:
            continue
        seen.add((y, x))
        region = []
        queue = [(y, x)]
        while queue:
            cury, curx = queue.pop(0)
            region.append((cury, curx))
            for dy, dx in nbrs:
                nbry, nbrx = cury+dy, curx+dx
                if 0 <= nbry < len(grid) and 0 <= nbrx < len(grid[0]) and \
                    grid[nbry][nbrx] == cell and \
                        (nbry, nbrx) not in seen:
                    queue.append((nbry, nbrx))
                    seen.add((nbry, nbrx))
        regions.append(region)


def calc_area_perim(region):
    area = len(region)
    miny, maxy = 10**10, 0
    minx, maxx = 10**10, 0
    for y, x in region:
        miny = min(miny, y)
        maxy = max(maxy, y)
        minx = min(minx, x)
        maxx = max(maxx, x)
    region_id = grid[region[0][0]][region[0][1]]
    perim = 0
    for y in range(miny, maxy+1):
        have_seen_cell = False
        for x in range(minx, maxx+1):
            if grid[y][x] == region_id and (y, x) in region:
                if not have_seen_cell:
                    perim += 2
                have_seen_cell = True
            else:
                have_seen_cell = False
    for x in range(minx, maxx+1):
        have_seen_cell = False
        for y in range(miny, maxy+1):
            if grid[y][x] == region_id and (y, x) in region:
                if not have_seen_cell:
                    perim += 2
                have_seen_cell = True
            else:
                have_seen_cell = False
    return area, perim


ans = 0
for region in regions:
    area, perim = calc_area_perim(region)
    ans += (area * perim)

print(ans)


def calc_area_sides(region):
    region_id = grid[region[0][0]][region[0][1]]
    region = sorted(region)
    print(region_id, region)
    return 0, 0


ans2 = 0
for region in regions:
    area, sides = calc_area_sides(region)
    ans += (area * sides)

print(ans2)
