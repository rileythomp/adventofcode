
import sys 
from collections import defaultdict

data = open(sys.argv[1]).read()

lines = data.split("\n")

containers = [int(line) for line in lines]

liters = 150
queue = [(liters-container, 1, containers[i+1:]) for i, container in enumerate(containers)] 

ans = 0
ans2 = 0
cur_min = 10**10
while queue:
    liters, num_containers, containers = queue.pop(0)
    for i, container in enumerate(containers):
        if liters - container == 0:
            ans += 1
            if num_containers+1 < cur_min: cur_min, ans2 = num_containers+1, 0
            if num_containers+1 == cur_min: ans2 += 1
        elif liters - container > 0:
            queue.append((liters-container, num_containers+1, containers[i+1:]))
print(ans)
print(ans2)
