import sys 
from collections import defaultdict

data = open(sys.argv[1]).read()

lines = data.split("\n")

graph = defaultdict(dict)

for line in lines: 
    words = line.split() 
    p1, p2 = words[0], words[-1][:-1]
    num = int(words[3])
    if words[2] == 'lose':
        num = -num
    graph[p1][p2] = num

from itertools import permutations 

perms = permutations(graph.keys(), len(graph))

def happiness(perm):
    happiness = 0
    for i in range(len(perm)):
        happiness += graph[perm[i]][perm[i-1]]
        happiness += graph[perm[i]][perm[(i+1)%len(perm)]]
    return happiness

ans = 0 
for perm in perms:
    ans = max(ans, happiness(perm))
print(ans)

graph['me'] = {}
for key in graph:
    graph[key]['me'] = 0
    graph['me'][key] = 0

perms = permutations(graph.keys(), len(graph))

ans = 0
for perm in perms:
    ans = max(ans, happiness(perm))
print(ans)