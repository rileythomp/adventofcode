with open('in.txt', 'r') as file:
    data = file.read().splitlines()
    grid = []
    for line in data:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    ans = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '@':
                continue
            n = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[y]):
                        if grid[ny][nx] == '@':
                            n += 1
            if n < 4:
                ans += 1
    print(ans)

def f(grid):
    remove = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '@':
                continue
            n = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[y]):
                        if grid[ny][nx] == '@':
                            n += 1
            if n < 4:
                remove.append((y, x))
    return remove

with open('in.txt', 'r') as file:
    data = file.read().splitlines()
    grid = []
    for line in data:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    ans = 0
    while True:
        remove = f(grid)
        if not remove:
            break
        for (y, x) in remove:
            grid[y][x] = '.'
        ans += len(remove)
    print(ans)
