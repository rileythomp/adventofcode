import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

grid = [list(line) for line in lines]

inity, initx = 0, 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '^':
            inity, initx = y, x
            break

move = 0

seen = set()

cury, curx = inity, initx
while 0 <= cury < len(grid) and 0 <= curx < len(grid[0]):
    if grid[cury][curx] == '#':
        match move:
            case 0: cury += 1
            case 1: curx -= 1
            case 2: cury -= 1
            case 3: curx += 1
        move = (move + 1) % 4
    seen.add((cury, curx))
    match move:
        case 0: cury -= 1
        case 1: curx += 1
        case 2: cury += 1
        case 3: curx -= 1

ans = len(seen)

ans2 = 0
for blocky, blockx in seen:
    grid[blocky][blockx] = '#'
    cury, curx = inity, initx
    move = 0
    seen = set()
    while 0 <= cury < len(grid) and 0 <= curx < len(grid[0]):
        if grid[cury][curx] == '#':
            match move:
                case 0: cury += 1
                case 1: curx -= 1
                case 2: cury -= 1
                case 3: curx += 1
            move = (move + 1) % 4
        if (cury, curx, move) in seen:
            ans2 += 1
            break
        seen.add((cury, curx, move))
        match move:
            case 0: cury -= 1
            case 1: curx += 1
            case 2: cury += 1
            case 3: curx -= 1
    grid[blocky][blockx] = '.'

print(ans)
print(ans2)
