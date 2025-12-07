from collections import defaultdict

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    grid = [[c for c in line] for line in lines]
    beams = set()
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            beams.add((0, i))

    ans = 0
    for i in range(1, len(grid)):
        splitters = []
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                splitters.append(j)
        new_beams = set()
        while beams:
            cur_beam_y, cur_beam_x = beams.pop()
            next_beam_y, new_beam_x = cur_beam_y + 1, cur_beam_x
            if new_beam_x in splitters:
                new_beams.add((next_beam_y, new_beam_x - 1))
                new_beams.add((next_beam_y, new_beam_x + 1))
                ans += 1
            else:
                new_beams.add((next_beam_y, new_beam_x))
        beams = new_beams
    print(ans)

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    grid = [[c for c in line] for line in lines]
    beams = {}
    for x in range(len(grid[0])):
        if grid[0][x] == 'S':
            beams[(0, x)] = 1
    for y in range(1, len(grid)):
        splitters = []
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                splitters.append(x)
        new_beams = defaultdict(int)
        for cur_beam, cur_paths in beams.items():
            cur_beam_y, cur_beam_x = cur_beam
            next_beam_y, new_beam_x = cur_beam_y + 1, cur_beam_x
            if new_beam_x in splitters:
                new_beams[(next_beam_y, new_beam_x-1)] = new_beams[(next_beam_y, new_beam_x-1)] + cur_paths
                new_beams[(next_beam_y, new_beam_x+1)] = new_beams[(next_beam_y, new_beam_x+1)] + cur_paths
            else:
                new_beams[(next_beam_y, new_beam_x)] = new_beams[(next_beam_y, new_beam_x)] + cur_paths
        beams = new_beams
    print(sum(beams.values()))
