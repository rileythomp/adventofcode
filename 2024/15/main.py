import sys

data = open(sys.argv[1]).read().strip()
groups = data.split('\n\n')

grid = [list(row) for row in groups[0].split('\n')]

moves = list(''.join(groups[1].split('\n')))

ry, rx = 0, 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '@':
            ry, rx = y, x

for move in moves:
    match move:
        case '>':
            px = rx + 1
            while grid[ry][px] != '.' and grid[ry][px] != '#':
                px += 1
            if grid[ry][px] == '.':
                for i in range(px, rx, -1):
                    grid[ry][i] = grid[ry][i-1]
                    grid[ry][i-1] = '.'
                rx += 1
        case '<':
            px = rx - 1
            while grid[ry][px] != '.' and grid[ry][px] != '#':
                px -= 1
            if grid[ry][px] == '.':
                for i in range(px, rx):
                    grid[ry][i] = grid[ry][i+1]
                    grid[ry][i+1] = '.'
                rx -= 1
        case '^':
            py = ry - 1
            while grid[py][rx] != '.' and grid[py][rx] != '#':
                py -= 1
            if grid[py][rx] == '.':
                for i in range(py, ry):
                    grid[i][rx] = grid[i+1][rx]
                    grid[i+1][rx] = '.'
                ry -= 1
        case 'v':
            py = ry + 1
            while grid[py][rx] != '.' and grid[py][rx] != '#':
                py += 1
            if grid[py][rx] == '.':
                for i in range(py, ry, -1):
                    grid[i][rx] = grid[i-1][rx]
                    grid[i-1][rx] = '.'
                ry += 1

ans = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 'O':
            ans += 100*y + x
print(ans)

grid = [list(row) for row in groups[0].split('\n')]
grid2 = []

for y, row in enumerate(grid):
    row2 = []
    for x, c in enumerate(row):
        match c:
            case '#':
                row2.extend(['#', '#'])
            case 'O':
                row2.extend(['[', ']'])
            case '.':
                grid[y][x] = '..'
                row2.extend(['.', '.'])
            case '@':
                row2.extend(['@', '.'])
    grid2.append(row2)

grid = grid2

ry, rx = 0, 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '@':
            ry, rx = y, x

for move_idx, move in enumerate(moves):
    match move:
        case '>':
            px = rx + 1
            while grid[ry][px] != '.' and grid[ry][px] != '#':
                px += 1
            if grid[ry][px] == '.':
                for i in range(px, rx, -1):
                    grid[ry][i] = grid[ry][i-1]
                    grid[ry][i-1] = '.'
                rx += 1
        case '<':
            px = rx - 1
            while grid[ry][px] != '.' and grid[ry][px] != '#':
                px -= 1
            if grid[ry][px] == '.':
                for i in range(px, rx):
                    grid[ry][i] = grid[ry][i+1]
                    grid[ry][i+1] = '.'
                rx -= 1
        case '^':
            ny = ry - 1
            next_cell = grid[ny][rx]
            if next_cell == '.':
                grid[ny][rx] = grid[ry][rx]
                grid[ry][rx] = '.'
                ry -= 1
            elif next_cell in '[]':
                frontier = []
                queue = [(ny, rx), (ny, rx + {'[': 1, ']': -1}[next_cell])]
                seen = set([(ry, rx)] + queue)
                while queue:
                    cury, curx = queue.pop(0)
                    nexty = cury - 1
                    if grid[nexty][curx] in '[]' and (nexty, curx) not in seen:
                        queue.append((nexty, curx))
                        seen.add((nexty, curx))
                        nbr = (nexty, curx+{'[': 1, ']': -1}[grid[nexty][curx]])
                        queue.append(nbr)
                        seen.add(nbr)
                    else:
                        frontier.append((cury, curx))
                for y, x in frontier:
                    if grid[y-1][x] == '#':
                        break
                else:
                    seen = sorted(seen)
                    for y, x in seen:
                        grid[y-1][x], grid[y][x] = grid[y][x], '.'
                    ry -= 1

        case 'v':
            ny = ry + 1
            next_cell = grid[ny][rx]
            if next_cell == '.':
                grid[ny][rx] = grid[ry][rx]
                grid[ry][rx] = '.'
                ry += 1
            elif next_cell in '[]':
                frontier = []
                queue = [(ny, rx), (ny, rx + {'[': 1, ']': -1}[next_cell])]
                seen = set([(ry, rx)] + queue)
                while queue:
                    cury, curx = queue.pop(0)
                    nexty = cury + 1
                    if grid[nexty][curx] in '[]' and (nexty, curx) not in seen:
                        queue.append((nexty, curx))
                        seen.add((nexty, curx))
                        nbr = (nexty, curx+{'[': 1, ']': -1}[grid[nexty][curx]])
                        queue.append(nbr)
                        seen.add(nbr)
                    else:
                        frontier.append((cury, curx))
                frontier = sorted(frontier)
                for y, x in frontier:
                    if grid[y+1][x] == '#':
                        break
                else:
                    seen = sorted(seen, reverse=True)
                    for y, x in seen:
                        grid[y+1][x], grid[y][x] = grid[y][x], '.'
                    ry += 1

ans2 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '[':
            ans2 += 100*y + x
print(ans2)
