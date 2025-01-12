import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')


def print_board(width, height, bots):
    grid = [['.' for j in range(width)] for i in range(height)]
    for bot in bots:
        px, py, vx, vy = bot
        grid[py][px] = '#'
    for row in grid:
        print(''.join(row))
    print()


bots = []

for line in lines:
    parts = line.split()
    pos = parts[0][2:].split(',')
    px, py = int(pos[0]), int(pos[1])
    vel = parts[1][2:].split(',')
    vx, vy = int(vel[0]), int(vel[1])
    bots.append((px, py, vx, vy))

width = 101
height = 103

seconds = 8000

for second in range(seconds):
    for i, bot in enumerate(bots):
        px, py, vx, vy = bot
        px = (px + vx) % width
        py = (py + vy) % height
        bots[i] = (px, py, vx, vy)
    if second >= seconds - 1000:
        print(second+1)
        print_board(width, height, bots)

quads = [0, 0, 0, 0]

for bot in bots:
    px, py, vx, vy = bot
    if px < width//2 and py < height//2:
        quads[0] += 1
    elif px < width//2 and py > height//2:
        quads[1] += 1
    elif px > width//2 and py < height//2:
        quads[2] += 1
    elif px > width//2 and py > height//2:
        quads[3] += 1

ans = 1
for q in quads:
    ans *= q
print(quads)
print(ans)
