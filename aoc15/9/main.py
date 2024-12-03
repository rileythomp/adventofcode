import sys 

data = open(sys.argv[1]).read().strip() 

lines = data.split("\n")

from collections import defaultdict

graph = defaultdict(list)

for line in lines:
    vals = line.split() 
    a, b = vals[0], vals[2]
    dist = int(vals[4])
    graph[a].append((b, dist))
    graph[b].append((a, dist))

ans = 10**10
ans2 = 0

x = defaultdict(int)
for start, nbrs in graph.items():
    queue = [(start, 0, set([start]))]
    while len(queue) > 0:
        node, dist, visited = queue.pop(0)
        if len(visited) == len(graph):
            ans = min(ans, dist)
            ans2 = max(ans2, dist)
        for nbr, d in graph[node]:
            if nbr not in visited:
                queue.append((nbr, dist + d, visited | set([nbr])))

print(ans)
print(ans2)