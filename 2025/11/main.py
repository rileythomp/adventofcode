with open('in.txt', 'r') as file:
    lines = file.read().splitlines()
    graph = {}
    for line in lines:
        parts = line.split(': ')
        src = parts[0]
        dst = parts[1].split()
        graph[src] = dst
    ans = 0
    queue = [('you', ['you'])]
    while queue:
        cur_node, visited = queue.pop(0)
        for neighbor in graph[cur_node]:
            if neighbor == 'out':
                ans += 1
            elif neighbor not in visited:
                new_visited = visited[:]
                new_visited.append(neighbor)
                queue.append((neighbor, new_visited))
    print(ans)
