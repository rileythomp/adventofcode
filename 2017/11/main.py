import sys
from collections import Counter, defaultdict

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

moves = lines[0].split(',')

dirs = {
    'n':  (1, -1, 0),
    's':  (-1, 1, 0),
    'ne': (1, 0, -1),
    'sw': (-1, 0, 1),
    'nw': (0, 1, -1),
    'se': (0, -1, 1)
}

coords = [0, 0, 0]

ans, ans2 = 0, 0
for move in moves:
    coords = [coords[i] + dirs[move][i] for i in range(3)]
    ans = max([abs(c) for c in coords])
    ans2 = max(ans2, ans)

print(ans)
print(ans2)
